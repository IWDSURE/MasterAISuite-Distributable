# IRC_SQL_TRACKING

Table used for tracking upgrade SQL execution in Fusion Recruiting application.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsqltracking-25053.html#ircsqltracking-25053](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsqltracking-25053.html#ircsqltracking-25053)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SQL_TRACKING_PK | SQL_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SQL_TRACKING_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| SQL_BLOCK_IDENTIFIER | VARCHAR2 | 300 |  | Yes | Identifier for identifying the SQL Block Tracking Recrod. Used for searching. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | Description of the SQL Block. Information for developers only. |
| STATUS | VARCHAR2 | 60 |  | Yes | Execution Status of the SQL Block. Information for developers only. |
| EXEC_START_TIME | TIMESTAMP |  |  |  | Execution Start time of the SQL Block. Information for developers only. |
| EXEC_END_TIME | TIMESTAMP |  |  |  | Execution End time of the SQL Block. Information for developers only. |
| ADDITIONAL_DETAILS | CLOB |  |  |  | Stores addtional details captured during the execution of the SQL Block. Information for developers only. |
| TRACKING_ATTR1 | VARCHAR2 | 1000 |  |  | To capture additional details. Information for developers only. |
| TRACKING_ATTR2 | VARCHAR2 | 1000 |  |  | To capture additional details. Information for developers only. |
| TRACKING_ATTR3 | VARCHAR2 | 1000 |  |  | To capture additional details. Information for developers only. |
| TRACKING_ATTR4 | VARCHAR2 | 1000 |  |  | To capture additional details. Information for developers only. |
| TRACKING_ATTR5 | VARCHAR2 | 1000 |  |  | To capture additional details. Information for developers only. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SQL_TRACKING_PK | Unique | FUSION_TS_SEED | SQL_TRACKING_ID, ORA_SEED_SET1 |
| IRC_SQL_TRACKING_PK1 | Unique | FUSION_TS_SEED | SQL_TRACKING_ID, ORA_SEED_SET2 |
| IRC_SQL_TRACKING_UK1 | Unique | FUSION_TS_SEED | SQL_BLOCK_IDENTIFIER, ORA_SEED_SET1 |
| IRC_SQL_TRACKING_UK11 | Unique | FUSION_TS_SEED | SQL_BLOCK_IDENTIFIER, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
