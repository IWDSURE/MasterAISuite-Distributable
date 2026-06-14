# CMP_CWB_PROMOTIONS

Stores promotions given to employees through compensatoin workbench. For example, job, position or grade change.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpromotions-14984.html#cmpcwbpromotions-14984](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpromotions-14984.html#cmpcwbpromotions-14984)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PROMOTIONS_PK | PROMOTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROMOTION_ID | NUMBER |  | 18 | Yes | PROMOTION_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASG_CHANGE_DATE | DATE |  |  |  | ASG_CHANGE_DATE |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| GRADE_MIN_VAL | NUMBER |  |  |  | GRADE_MIN_VAL |
| GRADE_MID_POINT | NUMBER |  |  |  | GRADE_MID_POINT |
| GRADE_MAX_VAL | NUMBER |  |  |  | GRADE_MAX_VAL |
| PROM_ORIG_UPDATED_BY | NUMBER |  | 18 |  | PROM_ORIG_UPDATED_BY |
| PROM_UPDATE_DATE | DATE |  |  |  | PROM_UPDATE_DATE |
| PROM_UPDATED_BY | NUMBER |  | 18 |  | PROM_UPDATED_BY |
| NEW_ASSIGNMENT_OVN | NUMBER |  | 9 |  | NEW_ASSIGNMENT_OVN |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ASSIGNMENT_NAME | VARCHAR2 | 80 |  |  | ASSIGNMENT_NAME |
| GRADE_STEP_ID | NUMBER |  | 18 |  | GRADE_STEP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PROMOTIONS_PK | Unique | Default | PROMOTION_ID |
| CMP_CWB_PROMOTIONS_U1 | Unique | Default | ASSIGNMENT_ID, ASG_CHANGE_DATE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
