# CMP_TCS_STMT_FEEDBACK_B

This tabnle stores run time setup data for feedback

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtfeedbackb-8632.html#cmptcsstmtfeedbackb-8632](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtfeedbackb-8632.html#cmptcsstmtfeedbackb-8632)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_FB_B_PK | STMT_FEEDBACK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_FEEDBACK_ID | NUMBER |  | 18 | Yes | STMT_FEEDBACK_ID |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| QUESTION1_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | QUESTION1_REQUIRED_FLAG |
| QUESTION2_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | QUESTION2_REQUIRED_FLAG |
| QUESTION3_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | QUESTION3_REQUIRED_FLAG |
| QUESTION4_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | QUESTION4_REQUIRED_FLAG |
| QUESTION5_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | QUESTION5_REQUIRED_FLAG |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_FB_B_FK1 | Non Unique | Default | PERD_RUN_ID, STMT_ID, STMT_PERD_ID |
| CMP_TCS_STMT_FB_B_FK2 | Non Unique | Default | STMT_PERD_ID |
| CMP_TCS_STMT_FB_B_UK1 | Unique | Default | STMT_FEEDBACK_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
