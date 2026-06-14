# PAY_TMPLT_CLMN_INST_TRANS_F

This Table Holds the clmn instances for template data

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltclmninsttransf-23103.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltclmninsttransf-23103.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CLMN_INST_TRANS_B_F_PK | CLMN_INST_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLMN_INST_ID | NUMBER |  | 18 | Yes | CLMN_INST_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| COL_ID | NUMBER |  | 18 | Yes | COL_ID |
| BASE_CLMN_INST_ID | NUMBER |  | 18 |  | BASE_CLMN_INST_ID |
| BASE_COL_VALUE | VARCHAR2 | 4000 |  |  | BASE_COL_VALUE |
| ROW_INST_ID | NUMBER |  | 18 | Yes | ROW_INST_ID |
| RENAME_FLAG | VARCHAR2 | 1 |  |  | RENAME_FLAG |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| USE_EXISTING_REC | VARCHAR2 | 1 |  |  | USE_EXISTING_REC |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COL_CLOB_VALUE | CLOB |  |  |  | COL_CLOB_VALUE |
| SURROGATE_KEY_VALUE | VARCHAR2 | 200 |  |  | SURROGATE_KEY_VALUE |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TMPLT_CLMN_INST_SGUID_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_TMPLT_CLMN_INST_TRANS_F_F1 | Non Unique | Default | ROW_INST_ID |
| PAY_TMPLT_CLMN_INST_TRANS_F_U1 | Unique | Default | CLMN_INST_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_TMPLT_CLMN_INST_TRAN_F_U11 | Unique | Default | CLMN_INST_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
