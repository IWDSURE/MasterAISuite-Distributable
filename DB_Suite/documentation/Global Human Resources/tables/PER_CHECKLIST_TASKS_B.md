# PER_CHECKLIST_TASKS_B

PER_CHECKLIST_TASKS_B : This table is base table for checklist tasks

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklisttasksb-25891.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklisttasksb-25891.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_TASKS_B_PK | CHECKLIST_TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_TASK_ID | NUMBER |  | 18 | Yes | Primary Key |
| REMINDER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for reminder. |
| TASK_LEVEL_CODE | VARCHAR2 | 30 |  |  | TASK_LEVEL_CODE |
| TASK_LEVEL_VALUE | NUMBER |  | 18 |  | TASK_LEVEL_VALUE |
| ATTACHMENT_DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Stores document type for attachment |
| CHECKLIST_TASK_CODE | VARCHAR2 | 240 |  | Yes | Unique Checklist Task Code |
| TASK_CATEGORY | VARCHAR2 | 30 |  |  | Task Category.
Extensible Lookup: ORA_CHK_TASK_CATEGORY |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ELIGY_PRFL.ELIGY_PRFL_ID (Eligibility Profile for Checklist) |
| MANDATORY_FLAG | VARCHAR2 | 30 |  |  | System Lookup: YES_NO
Values: Y - Yes
N - No
Identifies if the task is a mandatory task. |
| TARGET_DURATION | NUMBER |  | 9 |  | Task expiration duration |
| TARGET_DURATION_UOM | VARCHAR2 | 30 |  |  | System Lookup: CHECKLIST_QUALIFYING_UNITS
Values: D - Days
W - Weeks
M - Months
Task expiration duration unit of measure. |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | User Defined Lookup: PER_RESPONSIBILITY_TYPES
Area of Responsibility Performer Type
System Lookup: ORA_PER_CHECKLIST_PERFORMERS
Values: ORA_INITIATOR - Initiator
ORA_LN_MGR - Line Manager
ORA_WORKER - Worker
ORA_ADHOC_USER - Adhoc User |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_TASK_STATUS
Values: ORA_ACTIVE - Active
ORA_INACTIVE - In active |
| TASK_DELAY_DURATION_UOM | VARCHAR2 | 30 |  |  | System Lookup: CHECKLIST_QUALIFYING_UNITS
Values: D - Days
W - Weeks
M - Months
Task extension duration unit of measure. |
| TASK_DELAY_DURATION | NUMBER |  | 9 |  | Task extension duration |
| ACTION_TYPE | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_TASK_ACTION_TYPES
Values: ORA_NONE - None
ORA_EXTERNAL_URL - External URL (Default)
ORA_APP_TASK - Application Task
ORA_DOC_RECORD - Document of Record
ORA_CUSTOM_FORM - Custom Form
ORA_EVENT - Meeting / Event
ORA_CHECKLIST - Checklist |
| ADHOC_USER_GUID | VARCHAR2 | 64 |  |  | Specific User - Foreign Key to PER_USERS.USER_GUID |
| TASK_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to PER_TASK_ACTIONS_B.TASK_ACTION_ID
Task Definition to use when Action Type = Application Task |
| FLEX_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Flexfield Context Code when the Action Type = Custom Form |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Document Type associated with this task when Action Type = Document of Record |
| TASK_CONFIGURATION | VARCHAR2 | 4000 |  |  | Task Configuration |
| ACTIVATION_ELIGY_PRFL_ID | NUMBER |  | 18 |  | ACTIVATION_ELIGY_PRFL_ID |
| REMINDER_RECURRENCE | VARCHAR2 | 30 |  |  | When reminder needs to be sent for the task
System Lookup: ORA_CHK_REM_RECURRENCE
Values: ORA_NEVER - Never
ORA_EVERY - Every
ORA_1 - Once
ORA_2 - Twice
ORA_3 - Thrice
ORA_4 - Four times
ORA_5 - Five times
ORA_6 - Six times
ORA_7 - Seven times
ORA_8 - Eight times
ORA_9 - Nine times
ORA_10 - Ten times |
| REMINDER_DURATION | NUMBER |  | 3 |  | Reminder Duration (in days) |
| REMINDER_RELATIVE_TO | VARCHAR2 | 30 |  |  | Reminders need to be sent relative to
System Lookup: ORA_CHK_REM_RELATIVE_TO
Value: ORA_ASSIGNED - After Assigned Date
ORA_DUE - Before Due Date |
| GENERATE_ATOM_FEED | VARCHAR2 | 30 |  |  | Identifies if ATOM feed needs to be generated |
| OWNER_RESP_TYPE | VARCHAR2 | 30 |  |  | User Defined Lookup: PER_RESPONSIBILITY_TYPES
Area of Responsibility Performer Type
System Lookup: ORA_PER_CHECKLIST_PERFORMERS
Values: ORA_INITIATOR - Initiator
ORA_LN_MGR - Line Manager
ORA_WORKER - Worker
ORA_ADHOC_USER - Adhoc User |
| OWNER_USER_GUID | VARCHAR2 | 64 |  |  | Specific Owner User - Foreign Key to PER_USERS.USER_GUID |
| MEETING_OFFSET | NUMBER |  | 9 |  | Meeting Offset from Action Date |
| MEETING_TIME | VARCHAR2 | 10 |  |  | Meeting Time |
| ENABLE_TASK_EXPIRY | VARCHAR2 | 4 |  |  | Whether task expiry is supported or not.
System Lookup: YES_NO
Y - Yes
N - No |
| EXPIRY_AFTER_DAYS | NUMBER |  | 9 |  | Expiry Days |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Enterprise |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | SDF: Unique Seed Data GUID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign Key to FND_TERRITORIES.TERRITORY_CODE |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | Foreign Key to HR_ALL_ORGANIZATION_UNITS.ORGANIZATION_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Foreign Key to HR_ALL_ORGANIZATION_UNITS.ORGANIZATION_ID |
| TASK_ACTION_CODE | VARCHAR2 | 240 |  |  | Contains the action code associated with the task. |
| SIGN_TEMPLATE | VARCHAR2 | 240 |  |  | Stores the e-signature template for action type = ORA_CHK_ESIGN |
| ESIGN_TYPE | VARCHAR2 | 30 |  |  | Specifies ESignature Type |
| REPORT_PATH | VARCHAR2 | 1000 |  |  | It contains the BI Publisher report folder path followed by the report name concatenated with a / symbol with optionally a list of parameters in the format of  parameter_name is equals to parameter value . The first parameter is prefixed with ? and & to denote each additional parameter |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Stores the Questionnaire Identifier for the Questionnaire associated with this task |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |
| LEARN_CONTENT_TYPE | VARCHAR2 | 80 |  |  | LEARN_CONTENT_TYPE |
| REPORT_PARAMETERS | VARCHAR2 | 4000 |  |  | REPORT_PARAMETERS |
| ANALYTICS_PATH | VARCHAR2 | 1000 |  |  | Report path for analytics task type |
| EXPIRY_RELATIVE_TO | VARCHAR2 | 30 |  |  | EXPIRY_RELATIVE_TO |
| TASK_FEATURE1 | VARCHAR2 | 4000 |  |  | Stores the Task feature |
| TASK_FEATURE2 | VARCHAR2 | 4000 |  |  | Stores the Task feature |
| TASK_FEATURE3 | VARCHAR2 | 4000 |  |  | Stores the Task feature |
| TASK_FEATURE4 | VARCHAR2 | 4000 |  |  | Stores the Task feature |
| TASK_FEATURE5 | VARCHAR2 | 4000 |  |  | Stores the Task feature |
| TASK_FEATURE_DETAILS | CLOB |  |  |  | Stores the Task feature details |
| VIDEO_TYPE | VARCHAR2 | 80 |  |  | VIDEO_TYPE |
| DISPLAY_OPTIONS | VARCHAR2 | 4000 |  |  | DISPLAY_OPTIONS |
| VIDEO_URL | VARCHAR2 | 1000 |  |  | VIDEO_URL |
| LEARN_ENROLLMENT_ID | NUMBER |  | 18 |  | Identifier to the learn enrollment |
| LEARN_COMMUNITY_ID | NUMBER |  | 18 |  | Identifier to the learn community |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| LEARN_ENROLLMENT_TYPE | VARCHAR2 | 80 |  |  | LEARN_ENROLLMENT_TYPE |
| ATOM_FEED_CONFIGURATION | VARCHAR2 | 4000 |  |  | ATOM_FEED_CONFIGURATION |
| EMBED_TASK_ACTION_CODE | VARCHAR2 | 240 |  |  | EMBED_TASK_ACTION_CODE |
| CONTENT_PROVIDER_CODE | VARCHAR2 | 240 |  |  | CONTENT_PROVIDER_CODE |
| EMBED_APP_TASK_TYPE_ID | NUMBER |  | 18 |  | EMBED_APP_TASK_TYPE_ID |
| CHECKLIST_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_CATEGORY |
| CHECKLIST_SUB_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_SUB_CATEGORY |
| ANALYTICS_SUB_TYPE | VARCHAR2 | 80 |  |  | ANALYTICS_SUB_TYPE |
| REMINDER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | REMINDER_CONTENT_TYPE |
| REMINDER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | REMINDER_CONTENT_DEFN_ID |
| GUIDED_JOURNEY_CODE | VARCHAR2 | 240 |  |  | GUIDED_JOURNEY_CODE |
| GUIDED_JOURNEY_TASK_CODES | VARCHAR2 | 4000 |  |  | GUIDED_JOURNEY_TASK_CODES |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CHECKLIST_TASKS_B_N1 | Non Unique | Default | TASK_LEVEL_CODE, TASK_LEVEL_VALUE |
| PER_CHECKLIST_TASKS_B_N20 | Non Unique | Default | SGUID |
| PER_CHECKLIST_TASKS_B_PK | Unique | FUSION_TS_TX_DATA | CHECKLIST_TASK_ID, ORA_SEED_SET1 |
| PER_CHECKLIST_TASKS_B_PK1 | Unique | FUSION_TS_TX_DATA | CHECKLIST_TASK_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
