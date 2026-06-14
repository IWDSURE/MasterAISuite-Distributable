# IRC_DIAG_BKP_ROWS

This table stores backup data for diagnostic framework script execution runs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdiagbkprows-8388.html#ircdiagbkprows-8388](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdiagbkprows-8388.html#ircdiagbkprows-8388)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DIAG_BKP_ROWS_PK | BKP_ROW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BKP_ROW_ID | NUMBER |  | 18 | Yes | Identifier of the backup row. System generated value. |
| TEST_ID | VARCHAR2 | 32 |  |  | Identifier of the diagnostic test. |
| EXECUTION_ID | VARCHAR2 | 32 |  |  | Identifier of the diagnostic test run. |
| RUN_NAME | VARCHAR2 | 240 |  |  | User name of the diagnostic test run. |
| RUN_STATUS | VARCHAR2 | 32 |  |  | Status of the diagnostic test run. |
| COMMENTS | VARCHAR2 | 1000 |  |  | Comments for the backup table row. |
| SKID | NUMBER |  | 18 |  | SKID to store the surrogate key of the transaction table row being backed up. |
| XML_DATA | CLOB |  |  |  | XML representation of the table row being backed up in the diagnostic run. |
| OBJECT_NAME | VARCHAR2 | 30 |  | Yes | Table name of the transaction table being backed up. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise of the diagnostic test run. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DIAG_BKP_ROWS_N1 | Non Unique | Default | OBJECT_NAME, SKID |
| IRC_DIAG_BKP_ROWS_PK | Unique | Default | BKP_ROW_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
