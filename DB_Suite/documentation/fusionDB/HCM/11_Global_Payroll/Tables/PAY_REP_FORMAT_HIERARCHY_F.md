# PAY_REP_FORMAT_HIERARCHY_F

PAY_REP_FORMAT_HIERARCHY_F is a date effective table that hold information about the hierarchy of payroll reports.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrepformathierarchyf-18020.html#payrepformathierarchyf-18020](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrepformathierarchyf-18020.html#payrepformathierarchyf-18020)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REP_FORMAT_HIERARCHY_F_PK | REP_FORMAT_HIERARCHY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REP_FORMAT_HIERARCHY_ID | NUMBER |  | 18 | Yes | REP_FORMAT_HIERARCHY_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| REPORT_FORMAT_MAPPING_ID | NUMBER |  | 18 | Yes | REPORT_FORMAT_MAPPING_ID |  |
| CHILD_REP_FORMAT_MAP_ID | NUMBER |  | 18 | Yes | CHILD_REP_FORMAT_MAP_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_REP_FORMAT_HIERARCHY_F_PK | Unique | Default | REP_FORMAT_HIERARCHY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
