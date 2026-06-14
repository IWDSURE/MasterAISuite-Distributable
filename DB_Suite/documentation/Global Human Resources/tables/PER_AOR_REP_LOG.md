# PER_AOR_REP_LOG

This table holds log information of Refresh representatives ESS Job run which calculates the assignment representatives .

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorreplog-23469.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorreplog-23469.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_REP_PK | LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOG_ID | NUMBER |  | 18 | Yes | This is primary key identifier |
| LOG_DATE | TIMESTAMP |  |  |  | This is a system timestamp |
| AOR_REQUEST_ID | NUMBER |  |  |  | This is an area of responsibility request id used for this log row. |
| PROCEDURE_NAME | VARCHAR2 | 64 |  |  | This is a PLSQL procedure name. |
| INSTANCE | NUMBER |  |  |  | This is a database instance |
| SID | NUMBER |  |  |  | This is a database system identifier |
| MODULE | VARCHAR2 | 64 |  |  | This is a module name |
| ACTION | VARCHAR2 | 64 |  |  | This is an action name |
| CLIENT_IDENTIFIER | VARCHAR2 | 64 |  |  | This is a client identifier |
| MSG | VARCHAR2 | 1000 |  |  | This is a log message. |
| START_ROWID | ROWID |  |  |  | This is a start rowid |
| END_ROWID | ROWID |  |  |  | This is a end rowid |
| REPROWS_INSERTED | NUMBER |  |  |  | Number of representative rows inserted |
| SCOPE_ATTRS_LIST | VARCHAR2 | 4000 |  |  | This is list of score attributes combination |
| SQL_ID | VARCHAR2 | 13 |  |  | This is a sql id |
| ELAPSED_SEC | NUMBER |  |  |  | This is an elapsed seconds |
| SQL_STMT | CLOB |  |  |  | This is a SQL statement |
| ERROR_FLAG | VARCHAR2 | 1 |  |  | This is an error flag |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_AOR_REP_LOG_PK | Unique | Default | LOG_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
