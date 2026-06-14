# HRA_EVAL_STEPS_

This table stores evaluation steps

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalsteps-14731.html#hraevalsteps-14731](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalsteps-14731.html#hraevalsteps-14731)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_STEPS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVAL_STEP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVAL_STEP_ID | NUMBER |  | 18 | Yes | Primary key of Steps |
| NOTIFIED_DATE | DATE |  |  |  | Date when the alert notification was sent. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| EVALUATION_ID | NUMBER |  | 18 |  | Primary key of Evaluation. |
| EVAL_PARTICIPANT_ID | NUMBER |  | 18 |  | Indicates the participant ID in a particular evaluation |
| PARENT_STEP_ID | NUMBER |  | 18 |  | Indicatest the parent step ID to the current step |
| STEP_COMPLETED_BY | NUMBER |  | 18 |  | Indicates the ID of person who completed this step |
| STEP_COMPLETION_DATE | TIMESTAMP |  |  |  | Indicatest the date on which this step is completed |
| SEQUENCE_NUMBER | NUMBER |  | 18 |  | Indicates the processing sequence for the step |
| STEP_CODE | VARCHAR2 | 30 |  |  | Indicates the step code for the evaluation |
| STEP_STATUS | VARCHAR2 | 30 |  |  | Indicaties the step status of the evaluation |
| DUE_DATE | DATE |  |  |  | This is the due date of the step code |
| CRITICAL_ALERT_DAYS | NUMBER |  | 18 |  | Indicates the number of critical alert days before a notification is sent for this step |
| STANDARD_ALERT_DAYS | NUMBER |  | 18 |  | Indicates the number of standard alert days before a notification is sent for this step |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| STEP_SUB_STATUS | VARCHAR2 | 30 |  |  | Sub status of the step. |
| ACTION_REASON | VARCHAR2 | 30 |  |  | Reason for performing the action on the step. |
| ACTION_PERFORMED_BY | NUMBER |  | 18 |  | Stores the Person Id of the person performing the action. |
| ACTION_PERFORMED_DATE | TIMESTAMP |  |  |  | Timestamp when the action was performed |
| STEP_UPD_ACTION_CODE | VARCHAR2 | 30 |  |  | Action Code for performing the action on the evaluation step. |
| STEP_UPD_ACTION_REASON | VARCHAR2 | 30 |  |  | Reason for performing the action on the evaluation step. |
| STEP_UPD_ACTION_PERFORMED_BY | NUMBER |  | 18 |  | Stores the Person Id of the person performing the action on the evaluation step. |
| STEP_UPD_ACTION_PERFORMED_DATE | TIMESTAMP |  |  |  | Timestamp when the action was performed on the evaluation step. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_STEPSN1_ | Non Unique | Default | EVAL_STEP_ID, LAST_UPDATE_DATE |
| HRA_EVAL_STEPS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, EVAL_STEP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
