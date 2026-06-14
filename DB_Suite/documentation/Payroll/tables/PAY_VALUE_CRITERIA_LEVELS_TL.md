# PAY_VALUE_CRITERIA_LEVELS_TL

This translates the default levels of the Value by Criteria Tree

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluecriterialevelstl-12929.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluecriterialevelstl-12929.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_VALUE_CRITERIA_LEVELS_PK | VALUE_CRITERIA_LEVEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| VALUE_CRITERIA_LEVEL_ID | NUMBER |  | 18 | Yes | COLUMN1 |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| LABEL | VARCHAR2 | 256 |  |  | LABEL |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_VALUE_CRIT_LVL_TL_U1 | Unique | Default | VALUE_CRITERIA_LEVEL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
