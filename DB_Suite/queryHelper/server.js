require('dotenv').config();
const express = require('express');
const cors = require('cors');
const oracledb = require('oracledb');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3005;

app.use(cors());
app.use(express.json());
app.use(express.static('../public'));

// Oracle Connection Config
const dbConfig = {
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  connectString: process.env.DB_DSN
};

async function query(sql, params = []) {
  let conn;
  try {
    conn = await oracledb.getConnection(dbConfig);
    const result = await conn.execute(sql, params, { 
      outFormat: oracledb.OUT_FORMAT_OBJECT,
      fetchInfo: { 
        "DESCRIPTION": { type: oracledb.STRING }, 
        "COMMENTS": { type: oracledb.STRING }, 
        "METADATA": { type: oracledb.STRING },
        "VIEW_QUERY": { type: oracledb.STRING }
      }
    });
    return result.rows;
  } catch (err) {
    console.error('[Database Query Error]', err.message);
    console.error('SQL:', sql);
    console.error('Params:', params);
    throw err;
  } finally {
    if (conn) await conn.close();
  }
}

// --- API Endpoints ---

// 1. List Modules
app.get('/api/modules', async (req, res) => {
  try {
    const rows = await query('SELECT * FROM QH_MODULES ORDER BY NAME');
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 2. List Tables by Module
app.get('/api/tables', async (req, res) => {
  const { module_id } = req.query;
  try {
    const rows = await query('SELECT TABLE_ID, TABLE_NAME, OBJECT_TYPE, DESCRIPTION FROM QH_TABLES WHERE MODULE_ID = :1 ORDER BY TABLE_NAME', [module_id]);
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 3. Get Table Details
app.get('/api/table/:name', async (req, res) => {
  try {
    // Explicitly select columns to avoid ORA-40478 with large JSON/Vector columns
    const tableInfo = await query(`
      SELECT TABLE_ID, MODULE_ID, TABLE_NAME, DESCRIPTION, OBJECT_TYPE, VIEW_QUERY, IMPORTANCE, CREATED_AT 
      FROM QH_TABLES 
      WHERE TABLE_NAME = :1
    `, [req.params.name.toUpperCase()]);
    
    if (tableInfo.length === 0) return res.status(404).json({ error: 'Object not found' });

    const columns = await query('SELECT * FROM QH_COLUMNS WHERE TABLE_ID = :1 ORDER BY COLUMN_NAME', [tableInfo[0].TABLE_ID]);
    
    res.json({
      ...tableInfo[0],
      COLUMNS: columns
    });
  } catch (err) {
    console.error('[Get Details Error]', err);
    res.status(500).json({ error: err.message });
  }
});

// 4. Semantic Search (Hybrid Metadata + KB2 Context)
app.get('/api/search', async (req, res) => {
  const { q } = req.query;
  if (!q) return res.status(400).json({ error: 'Search term required' });

  try {
    console.log(`[Search] Query: ${q}`);
    
    // Step 1: Keyword Search (Fast)
    // Split query by spaces and create OR conditions for each word
    const words = q.split(/\s+/);
    let whereClause = "";
    let params = [];
    
    for (let i = 0; i < words.length; i++) {
        if (i > 0) whereClause += " OR ";
        whereClause += `(UPPER(TABLE_NAME) LIKE UPPER(:${i*2+1}) OR DBMS_LOB.INSTR(UPPER(DESCRIPTION), UPPER(:${i*2+2})) > 0)`;
        params.push(`%${words[i]}%`, `%${words[i]}%`);
    }

    const keywordResults = await query(`
      SELECT TABLE_ID, TABLE_NAME, DESCRIPTION, 'KEYWORD' as MATCH_TYPE 
      FROM QH_TABLES 
      WHERE ${whereClause}
      FETCH FIRST 10 ROWS ONLY
    `, params);

    // Step 2: Semantic Metadata Search (Native Oracle Vector Search)
    let semanticMetaResults = [];
    try {
      // Get embedding from KB2 sidecar for the user's query
      const embedResp = await axios.get(`http://localhost:5002/embed?text=${encodeURIComponent(q)}`);
      if (embedResp.data.vec) {
        const queryVec = JSON.stringify(embedResp.data.vec);
        semanticMetaResults = await query(`
          SELECT TABLE_ID, TABLE_NAME, DESCRIPTION, 'SEMANTIC' as MATCH_TYPE,
                 VECTOR_DISTANCE(VEC, VECTOR(:1, 768, FLOAT32), COSINE) as DISTANCE
          FROM QH_TABLES
          WHERE VEC IS NOT NULL
          ORDER BY DISTANCE
          FETCH FIRST 15 ROWS ONLY
        `, [queryVec]);
      }
    } catch (e) {
      console.warn('[Semantic Meta Search] Failed (Is sidecar running?):', e.message);
    }

    res.json({
      keyword: keywordResults,
      semanticMetadata: semanticMetaResults
    });
  } catch (err) {
    console.error('[Search Error]', err);
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`[Query Helper API] Running on http://localhost:${PORT}`);
});
