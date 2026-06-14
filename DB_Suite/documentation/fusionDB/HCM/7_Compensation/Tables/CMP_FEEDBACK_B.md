# CMP_FEEDBACK_B

Stores feedback details for a plan.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpfeedbackb-4796.html#cmpfeedbackb-4796](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpfeedbackb-4796.html#cmpfeedbackb-4796)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_FEEDBACK_B_PK | FEEDBACK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_ID | NUMBER |  | 18 | Yes | FEEDBACK_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| RATING_ENABLED_FLAG | VARCHAR2 | 1 |  |  | RATING_ENABLED_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_FEEDBACK_B_N1 | Non Unique | Default | PLAN_ID |
| CMP_FEEDBACK_B_UK1 | Unique | Default | FEEDBACK_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
