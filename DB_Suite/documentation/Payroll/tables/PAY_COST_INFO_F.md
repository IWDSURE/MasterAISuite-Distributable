# PAY_COST_INFO_F

This table contains costing attrinutes for each classification.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostinfof-7286.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostinfof-7286.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COST_INFO_F_PK | COST_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COST_INFO_ID | NUMBER |  | 18 | Yes | COST_INFO_ID |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | SOURCE_TYPE |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| COSTABLE_TYPE | VARCHAR2 | 30 |  |  | COSTABLE_TYPE |
| DISTRIBUTION_SET_ID | NUMBER |  | 18 |  | DISTRIBUTION_SET_ID |
| COSTED_FLAG | VARCHAR2 | 30 |  |  | COSTED_FLAG |
| COSTED_HOURS | VARCHAR2 | 30 |  |  | COSTED_HOURS |
| TRANSFER_TO_GL_FLAG | VARCHAR2 | 30 |  |  | TRANSFER_TO_GL_FLAG |
| TRANSFER_TO_PROJ_FLAG | VARCHAR2 | 30 |  |  | TRANSFER_TO_PROJ_FLAG |
| COST_CLASSIFICATION_ID | NUMBER |  | 18 |  | COST_CLASSIFICATION_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COST_CLEARED_PAYMENT | VARCHAR2 | 30 |  |  | COST_CLEARED_PAYMENT |
| COST_MANUAL_PAYMENT | VARCHAR2 | 30 |  |  | COST_MANUAL_PAYMENT |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_COST_INFO_F_FK1 | Unique | Default | SOURCE_ID, SOURCE_TYPE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_COST_INFO_F_PK | Unique | Default | COST_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
