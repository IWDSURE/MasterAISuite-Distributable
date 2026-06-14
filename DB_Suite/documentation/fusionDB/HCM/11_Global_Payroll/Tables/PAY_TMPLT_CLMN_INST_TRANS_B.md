# PAY_TMPLT_CLMN_INST_TRANS_B

This Table Holds the clmn instances for template data

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltclmninsttransb-16554.html#paytmpltclmninsttransb-16554](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltclmninsttransb-16554.html#paytmpltclmninsttransb-16554)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_CLMN_INST_TRANS_B_PK | CLMN_INST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CLMN_INST_ID | NUMBER |  | 18 | Yes | CLMN_INST_ID |  |
| BASE_CLMN_INST_ID | NUMBER |  | 18 |  | BASE_CLMN_INST_ID |  |
| BASE_COL_VALUE | VARCHAR2 | 200 |  |  | BASE_COL_VALUE |  |
| ROW_INST_ID | NUMBER |  | 18 | Yes | ROW_INST_ID |  |
| COL_ID | NUMBER |  | 18 | Yes | COL_ID |  |
| RENAME_FLAG | VARCHAR2 | 1 |  |  | RENAME_FLAG |  |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |  |
| USE_EXISTING_REC | VARCHAR2 | 1 |  |  | USE_EXISTING_REC |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| COL_CLOB_VALUE | CLOB |  |  |  | COL_CLOB_VALUE |  |
| SURROGATE_KEY_VALUE | VARCHAR2 | 200 |  |  | SURROGATE_KEY_VALUE |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_CLMN_INST_TRANS_B_F1 | Non Unique | Default | ROW_INST_ID |
| PAY_TMPLT_CLMN_INST_TRANS_B_PK | Unique | Default | CLMN_INST_ID |
| PAY_TMPLT_CLMN_INST_TRANS_N20 | Non Unique | Default | SGUID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
