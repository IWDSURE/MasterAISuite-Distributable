# CMP_TCS_FEEDBACK_B

Table holds Feedback information

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsfeedbackb-22139.html#cmptcsfeedbackb-22139](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsfeedbackb-22139.html#cmptcsfeedbackb-22139)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_FEEDBACK_B_PK | FEEDBACK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_ID | NUMBER |  | 18 | Yes | FEEDBACK_ID |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 |  | STMT_PERD_ID |
| RATING_ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | RATING_ENABLED_FLAG |
| QUESTION1_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Feedback Required Flag 1 |
| QUESTION2_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Feedback Required Flag 2 |
| QUESTION3_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Feedback Required Flag 3 |
| QUESTION4_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Feedback Required Flag 4 |
| QUESTION5_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Feedback Required Flag 1 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_FEEDBACK_UK1 | Unique | Default | FEEDBACK_ID |
| CMP_TCS_FEEDBACK_UK2 | Unique | Default | STMT_ID, STMT_PERD_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
