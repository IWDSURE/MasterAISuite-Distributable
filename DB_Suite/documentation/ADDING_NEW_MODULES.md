# Scaling the Query Helper: Adding New Pillars (Finance, SCM, etc.)

The Query Helper is designed to be pillar-agnostic. Follow these steps to ingest and enable semantic search for new modules.

## 1. Directory Structure
Place your new documentation in a sibling folder to `HCM` within the `fusionDB` directory.
*   `DB/documentation/fusionDB/FIN` (Finance)
*   `DB/documentation/fusionDB/SCM` (Supply Chain)

Ensure each pillar follows the hierarchical structure: `{Module}/Tables/{Table}.json`.

## 2. Technical Ingestion
Update the `ingest_metadata.py` script to include your new pillar.
1.  Locate the `HCM_BASE_PATH` variable in `DB/queryHelper/ingest_metadata.py`.
2.  Change it to the root of the new pillar (e.g., `.../fusionDB/FIN`).
3.  Run the script: `python ingest_metadata.py`.
    *   *Note:* This script performs a `DELETE` on tables before ingestion. If you want to **merge** HCM and Finance, I recommend creating a `PILLAR` column in the `QH_MODULES` table and updating the script to filter by pillar.

## 3. Semantic Upgrade
Once the structural metadata is in Oracle, you must generate vectors for the new tables.
1.  Ensure the **KB Sidecar** is running.
2.  Run the semantic upgrade: `python upgrade_semantic.py`.
3.  The script will automatically find all tables with a `NULL` vector and generate embeddings for them using the warm AI model.

## 4. UI Organization (Optional)
If you add multiple pillars, you can update the `QH_MODULES` table to include a `PILLAR` name (e.g., "Finance"). 
Then, update `index.html` to group the sidebar by Pillar.

### Recommended SQL for Multi-Pillar Support:
```sql
ALTER TABLE QH_MODULES ADD (PILLAR VARCHAR2(50) DEFAULT 'HCM');
-- After ingestion of Finance:
UPDATE QH_MODULES SET PILLAR = 'FIN' WHERE PATH LIKE '%/fusionDB/FIN/%';
```

---
*Query Helper: A Scalable Metadata Brain*

