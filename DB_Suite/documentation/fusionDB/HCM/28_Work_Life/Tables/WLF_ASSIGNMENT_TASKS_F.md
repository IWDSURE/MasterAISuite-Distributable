# WLF_ASSIGNMENT_TASKS_F

Table for course-class Assignment Reconciliation work.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmenttasksf-7044.html#wlfassignmenttasksf-7044](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmenttasksf-7044.html#wlfassignmenttasksf-7044)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ASSIGNMENT_TASKS_F_PK | ASSIGNMENT_TASK_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_TASK_ID | NUMBER |  | 18 | Yes | System generated unique identifier to represent a row. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PARENT_TASK_ID | NUMBER |  | 18 |  | Parent Task Id (in Hierarchical case). |
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 |  | Assignment Record Id (referential key from assignment records table). |
| TASK_OWNER_ID | NUMBER |  | 18 |  | Who is responsible to finish the task , mostly PERSON_ID, could be learner, learner manger,Learn Admin, AOR id, or any other groups that is maintained. |
| TASK_OWNER_TYPE | VARCHAR2 | 30 |  |  | ORA_PERSON ( most of the time it is PERSON), could be SYSTEM if you want to track Notification generation as well. Could be Areas of Responsibility, Access group. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | What learning item needs to be acted on , for example classId(class learning item id) in class preferences use case. |
| TASK_STATUS | VARCHAR2 | 30 |  |  | Stores status of the task. |
| ACCESS_ALLOWED_ON_DATE | TIMESTAMP |  |  |  | The date on which assignment task access has been given to the learner |
| COMPLETION_DATE | TIMESTAMP |  |  |  | Completion date of the task. |
| SOURCE_OBJECT_ID | NUMBER |  | 18 |  | To track the source of the record creation for this table , similar to assignment records table. |
| SOURCE_OBJECT_TYPE | VARCHAR2 | 30 |  |  | To track the source of the record creation for this table , similar to assignment records table. |
| SOURCE_OBJECT_CODE | VARCHAR2 | 30 |  |  | To track the source of the record creation for this table , similar to assignment records table. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| IS_OPEN | VARCHAR2 | 1 |  |  | Column value represent whether activity is open for learner to start or not. |
| SECTION_LI_ID | NUMBER |  | 18 |  | Column value represents section learning item id of the activity |
| LEARNING_ITEM_TYPE | VARCHAR2 | 32 |  |  | Column value represent learning item type of activity |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| NOTES | VARCHAR2 | 4000 |  |  | Notes by the admin for a learner activity task |
| SCORE | NUMBER |  | 9 |  | Score acheived by  a learner activity task |
| EFFORT | NUMBER |  | 9 |  | ACTUAL EFFORT learner has spent on a activity task |
| EFFORT_UOM | VARCHAR2 | 30 |  |  | Unit of measure for effort |
| TASK_SUB_STATUS | VARCHAR2 | 30 |  |  | Substatus of the task. |
| TRAINING_EFFORT | NUMBER |  | 9 |  | TRAINING EFFORT learner has spent on a activity task |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason for completion |
| VILT_URL | VARCHAR2 | 1000 |  |  | Learner vilt URL |
| VILT_CALL_TIME | TIMESTAMP |  |  |  | VILT Call time |
| VILT_CALL_STATUS | VARCHAR2 | 30 |  |  | VILT call status |
| VILT_CALL_LOG | VARCHAR2 | 1000 |  |  | VILT call log |
| EXEMPTED_ON_DATE | TIMESTAMP |  |  |  | Date on which exemption given for this Task or Activity |
| REQ_ACT_COMPLETION_COUNT | NUMBER |  | 8 |  | Represent the count of activities required to complete section. |
| COMPLETED_ACTIVITY_COUNT | NUMBER |  | 8 |  | Represents the activities that are completed for this section. |
| REQUIRED_PREDECESSOR | NUMBER |  | 18 |  | A predecessor task that needs to be completed for learner to access current task. |
| TASK_COMPLETION_RULE | VARCHAR2 | 30 |  |  | Represents whether current task is required or optional to complete the section |
| TASK_POSITION | NUMBER |  | 38 |  | Represents the activity or section position  in catalog definition |
| LI_DEF_USED_DATE | TIMESTAMP |  |  |  | Represents the timestamp of the learning item change used for this assignment task creation/update |
| START_DATE | TIMESTAMP |  |  |  | Represents the start date of activity attempt |
| ASSIGNMENT_TASK_NUMBER | VARCHAR2 | 30 |  |  | UserKey to uniquely identify assignment task |
| ACTIVITY_DEFINITION | CLOB |  |  |  | Represents activity definition object. |
| EXPIRATION_DATE | DATE |  |  |  | The date that the assignment will expire. |
| TASK_TYPE | VARCHAR2 | 30 |  |  | Represents type of task related to Example task is created for Rating activity  or Evaluation activity. |
| INCOMPLETE_DATE | TIMESTAMP |  |  |  | Represents the date when assignment task entered to Incomplete status |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ASSIGNMENT_TASKS_F_N1 | Non Unique | Default | ASSIGNMENT_RECORD_ID |
| WLF_ASSIGNMENT_TASKS_F_N10 | Non Unique | WLF_ASSIGNMENT_TASKS_F_N10 | SOURCE_OBJECT_ID |
| WLF_ASSIGNMENT_TASKS_F_N11 | Non Unique | Default | UPPER("ASSIGNMENT_TASK_NUMBER") |
| WLF_ASSIGNMENT_TASKS_F_N2 | Non Unique | Default | TASK_OWNER_ID, TASK_OWNER_TYPE |
| WLF_ASSIGNMENT_TASKS_F_N3 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_ASSIGNMENT_TASKS_F_N4 | Non Unique | Default | TASK_SUB_STATUS, TASK_STATUS |
| WLF_ASSIGNMENT_TASKS_F_N5 | Non Unique | Default | TASK_STATUS, TASK_SUB_STATUS |
| WLF_ASSIGNMENT_TASKS_F_U1 | Unique | Default | ASSIGNMENT_TASK_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
