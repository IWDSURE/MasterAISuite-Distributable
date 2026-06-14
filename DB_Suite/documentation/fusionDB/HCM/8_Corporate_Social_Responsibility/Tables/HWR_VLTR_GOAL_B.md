# HWR_VLTR_GOAL_B

This table stores base goal information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoalb-28936.html#hwrvltrgoalb-28936](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrgoalb-28936.html#hwrvltrgoalb-28936)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_GOAL_B_PK | GOAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | GOAL_ID |  |
| HCM_PERSON_ID | NUMBER |  | 18 |  | HCM_PERSON_ID |  |
| LOWER_BOUND | NUMBER |  | 18 |  | LOWER_BOUND |  |
| UPPER_BOUND | NUMBER |  | 18 |  | UPPER_BOUND |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| VOLUNTEER_ID | NUMBER |  | 18 |  | VOLUNTEER_ID | Obsolete |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_GOAL_B_U1 | Unique | FUSION_TS_TX_IDX | GOAL_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
