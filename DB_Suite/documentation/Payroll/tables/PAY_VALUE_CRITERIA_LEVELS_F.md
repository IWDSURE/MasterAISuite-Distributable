# PAY_VALUE_CRITERIA_LEVELS_F

This defined the default levels of the Value by Criteria Tree

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluecriterialevelsf-26025.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluecriterialevelsf-26025.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| VALUE_CRITERIA_LEVEL_ID | NUMBER |  | 18 | Yes | VALUE_CRITERIA_LEVEL_ID |  |
| VO_NAME | VARCHAR2 | 256 |  |  | VO_NAME |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| VALUE_DEFN_ID | NUMBER |  | 18 | Yes | VALUE_DEFN_ID |  |
| CRITERIA_LEVEL | NUMBER |  | 18 | Yes | CRITERIA_LEVEL |  |
| DATABASE_ITEM_ID | NUMBER |  | 18 | Yes | DATABASE_ITEM_ID |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Forrign Key to PER_LEGISLATIVE_DATA_GROUPS |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign Key to FND_TERITORIES |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
