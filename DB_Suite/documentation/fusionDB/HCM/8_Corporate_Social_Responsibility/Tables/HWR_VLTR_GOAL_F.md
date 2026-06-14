# HWR_VLTR_GOAL_F

This table stores goal effectivity information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoalf-11222.html#hwrvltrgoalf-11222](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoalf-11222.html#hwrvltrgoalf-11222)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_GOAL_F_PK | GOAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | This is column stores unique goal ID field |
| GOAL_METRIC | VARCHAR2 | 50 |  | Yes | This is column stores the metric of the goal. |
| LOWER_BOUND | NUMBER |  |  |  | This stores the lower bound of the goal metric. |
| UPPER_BOUND | NUMBER |  |  |  | This stores the upper bound value for the Goal Metric |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| UNITS | VARCHAR2 | 50 |  |  | This stores the units to be used for reading the goals |
| FREQUENCY | VARCHAR2 | 50 |  |  | This stores the frequency of the wellness user data goal. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_GOAL_F_U1 | Unique | FUSION_TS_TX_IDX | GOAL_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
