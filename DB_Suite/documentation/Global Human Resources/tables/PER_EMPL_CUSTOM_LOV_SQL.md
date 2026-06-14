# PER_EMPL_CUSTOM_LOV_SQL

This table stores customer sql.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplcustomlovsql-21310.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplcustomlovsql-21310.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EMPL_CUSTOM_LOV_SQL_PK | CUSTOM_SQL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CUSTOM_SQL_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate Key. |
| MODULE | VARCHAR2 | 60 |  | Yes | Module Name |
| LOV_NAME | VARCHAR2 | 60 |  | Yes | Lov Name |
| ACTIVE_STATUS | VARCHAR2 | 3 |  |  | Status: 'A' indicates active. 'I' indicates inactive |
| VALIDATION_TYPE | VARCHAR2 | 240 |  |  | Current it only have one value: EXISTS |
| VALIDATE_LOV_COL_NAME | VARCHAR2 | 240 |  |  | Join column in exists where clause. |
| WHERE_CLAUSE | VARCHAR2 | 4000 |  |  | Where clause |
| WHERE_EXT_CLAUSE | VARCHAR2 | 4000 |  |  | Where extension clause |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Business Group Id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EMPL_CUSTOM_LOV_SQL_U1 | Unique | Default | CUSTOM_SQL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
