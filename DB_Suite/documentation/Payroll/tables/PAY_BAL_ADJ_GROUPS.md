# PAY_BAL_ADJ_GROUPS

This table contains definitions that correspond to balance adjustment payroll actions. It is a child table of PAY_BAL_ADJ_HEADERS.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjgroups-15762.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybaladjgroups-15762.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ADJ_GROUPS_PK | BAL_ADJ_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_ADJ_GROUP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BAL_ADJ_BATCH_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_BAL_ADJ_HEADERS. |
| BATCH_GROUP_STATUS | VARCHAR2 | 30 |  | Yes | Batch Group Status. Unprocessed, Processing, Complete, Incomplete. |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | Payroll action created by the system. |
| CONSOLIDATION_SET_ID | NUMBER |  | 18 |  | CONSOLIDATION_SET_ID |
| PAYROLL_ID | NUMBER |  | 18 | Yes | PAYROLL_ID |
| EFFECTIVE_DATE | DATE |  |  | Yes | EFFECTIVE_DATE |
| ADJUSTMENT_TYPE | VARCHAR2 | 30 |  | Yes | Type of Balance Adjustment. |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element Type that triggers the balance adjustment formula process. |
| PERSON_GROUP_ID | NUMBER |  | 18 |  | Object Group that represents a person group. Foreign key to PAY_OBJECT_GROUPS. |
| PREPAY_FLAG | VARCHAR2 | 30 |  |  | PREPAY_FLAG |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID |
| BALANCE_ADJ_COST_FLAG | VARCHAR2 | 30 |  |  | BALANCE_ADJ_COST_FLAG |
| DATE_EARNED | DATE |  |  |  | Date Earned. |
| PROCESS_REASON | VARCHAR2 | 30 |  |  | Process Reason |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_ADJ_GROUPS_FK1 | Non Unique | Default | BAL_ADJ_BATCH_ID |
| PAY_BAL_ADJ_GROUPS_FK2 | Non Unique | Default | PAYROLL_ACTION_ID |
| PAY_BAL_ADJ_GROUPS_PK | Unique | Default | BAL_ADJ_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
