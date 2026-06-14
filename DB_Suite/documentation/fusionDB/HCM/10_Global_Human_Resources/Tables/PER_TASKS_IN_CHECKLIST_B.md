# PER_TASKS_IN_CHECKLIST_B

This table records the tasks within the checklist templates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasksinchecklistb-8695.html#pertasksinchecklistb-8695](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasksinchecklistb-8695.html#pertasksinchecklistb-8695)

## Primary Key

| Name | Columns |
|------|----------|
| PER_TASKS_IN_CHECKLIST_B_PK | TASK_IN_CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | System generated part of the primary key. Surrogate key. |  |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |  |
| REMINDER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for reminder. |  |
| ATTACHMENT_DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Stores document type for attachment |  |
| TASK_IN_CHECKLIST_CODE | VARCHAR2 | 240 |  |  | Checklist task code |  |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  |  | Activate ir deactivate a template task in case if it is not suitable for deletion. |  |
| ALLOW_ALLC_TASK_CREATE | VARCHAR2 | 30 |  |  | Indicates that this checklist can be used for creation of allocated checklist task. |  |
| ALLOW_ALLC_TASK_UPDATE | VARCHAR2 | 30 |  |  | Indicates that this checklist can be used for updation of allocated checklist task. |  |
| ALLOW_ALLC_TASK_DELETE | VARCHAR2 | 30 |  |  | Indicates that this checklist can be used for deletion of allocated checklist task. |  |
| TASK_DELAY_DURATION_UOM | VARCHAR2 | 30 |  |  | Delay duration unit of measure.(days, weeks or months) |  |
| TASK_DELAY_DURATION | NUMBER |  | 9 |  | Delay duration for task. |  |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | Identifier for the checklist holding the task |  |
| ELIGIBILITY_OBJECT_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIG_OBJ_F.ELIG_OBJ_ID |  |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | Identifier for the eligibility profile |  |
| AME_ATTRIBUTE_IDENTIFIER | VARCHAR2 | 30 |  |  | AME Attribute Identifier corresponding to the AME condition |  |
| MANDATORY_FLAG | VARCHAR2 | 30 |  |  | Denotes whether this task is mandatory or not. |  |
| TARGET_DURATION | NUMBER |  | 9 |  | Target Duration for the task |  |
| TARGET_DURATION_UOM | VARCHAR2 | 30 |  |  | Target Duration Unit of measure (Days. Weeks, Months) |  |
| TASK_SEQUENCE | NUMBER |  | 9 |  | Obsolete |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield structure defining column |  |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | User Defined Lookup: PER_RESPONSIBILITY_TYPES
Area of Responsibility Performer Type
System Lookup: ORA_PER_CHECKLIST_PERFORMERS
Values: ORA_INITIATOR - Initiator
ORA_LN_MGR - Line Manager
ORA_WORKER - Worker
ORA_ADHOC_USER - Adhoc User |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Task Attributes (PER_TASKS_IN_CHECKLIST_DFF) |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ADHOC_USER_GUID | VARCHAR2 | 64 |  |  | Specific User - Foreign Key to PER_USERS.USER_GUID |  |
| ACTION_TYPE | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_TASK_ACTION_TYPES
Values: ORA_NONE - None
ORA_EXTERNAL_URL - External URL (Default)
ORA_APP_PROCESS - Application Task
ORA_DOC_RECORD - Document of Record
ORA_CUSTOM_FORM - Custom Form |  |
| TASK_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to PER_TASK_ACTIONS_B.TASK_ACTION_ID
Task Definition to use when Action Type = Application Task |  |
| FLEX_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Flexfield Context Code when the Action Type = Custom Form |  |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Document Type associated with this task when Action Type = Document of Record |  |
| TASK_CONFIGURATION | VARCHAR2 | 4000 |  |  | Task Configuration |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ACTIVATION_ELIGY_PRFL_ID | NUMBER |  | 18 |  | ACTIVATION_ELIGY_PRFL_ID |  |
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
ORA_10 - Ten times |  |
| REMINDER_DURATION | NUMBER |  | 3 |  | Reminder Duration (in days) |  |
| REMINDER_RELATIVE_TO | VARCHAR2 | 30 |  |  | Reminders need to be sent relative to
System Lookup: ORA_CHK_REM_RELATIVE_TO
Value: ORA_ASSIGNED - After Assigned Date
ORA_DUE - Before Due Date |  |
| OWNER_RESP_TYPE | VARCHAR2 | 30 |  |  | User Defined Lookup: PER_RESPONSIBILITY_TYPES
Area of Responsibility Performer Type
System Lookup: ORA_PER_CHECKLIST_PERFORMERS
Values: ORA_INITIATOR - Initiator
ORA_LN_MGR - Line Manager
ORA_WORKER - Worker
ORA_ADHOC_USER - Adhoc User |  |
| OWNER_USER_GUID | VARCHAR2 | 64 |  |  | Specific Owner User - Foreign Key to PER_USERS.USER_GUID |  |
| GENERATE_ATOM_FEED | VARCHAR2 | 30 |  |  | Identifies if ATOM feed needs to be generated |  |
| MEETING_OFFSET | NUMBER |  | 9 |  | Meeting Offset from Action Date |  |
| MEETING_TIME | VARCHAR2 | 10 |  |  | Meeting Time |  |
| ENABLE_TASK_EXPIRY | VARCHAR2 | 4 |  |  | Whether task expiry is supported or not.
System Lookup: YES_NO
Y - Yes
N - No |  |
| EXPIRY_AFTER_DAYS | NUMBER |  | 9 |  | Expiry Days |  |
| TASK_CATEGORY | VARCHAR2 | 30 |  |  | Task Category.
Extensible Lookup: ORA_CHK_TASK_CATEGORY |  |
| DETAIL_CHECKLIST_ID | NUMBER |  | 18 |  | Detail Checklist when Action Type is ORA_CHECKLIST |  |
| CONTACT_DETAILS | VARCHAR2 | 1000 |  |  | CONTACT_DETAILS |  |
| TASK_ACTION_CODE | VARCHAR2 | 240 |  |  | Contains the action code associated with the task. |  |
| SIGN_TEMPLATE | VARCHAR2 | 240 |  |  | Stores the e-signature template for action type = ORA_CHK_ESIGN |  |
| ESIGN_TYPE | VARCHAR2 | 30 |  |  | Specifies Esignature Type |  |
| REPORT_PATH | VARCHAR2 | 1000 |  |  | It contains the BI Publisher report folder path followed by the report name concatenated with a / symbol with optionally a list of parameters in the format of  parameter_name is equals to parameter value . The first parameter is prefixed with ? and & to denote each additional parameter |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Stores the Questionnaire Identifier for the Questionnaire associated with this task |  |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |  |
| LEARN_CONTENT_TYPE | VARCHAR2 | 80 |  |  | LEARN_CONTENT_TYPE |  |
| REPORT_PARAMETERS | VARCHAR2 | 4000 |  |  | REPORT_PARAMETERS |  |
| ANALYTICS_PATH | VARCHAR2 | 1000 |  |  | Report path for analytics task type |  |
| EXPIRY_RELATIVE_TO | VARCHAR2 | 30 |  |  | EXPIRY_RELATIVE_TO |  |
| TASK_FEATURE1 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE2 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE3 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE4 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE5 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE_DETAILS | CLOB |  |  |  | Stores the Task feature details |  |
| VIDEO_TYPE | VARCHAR2 | 80 |  |  | VIDEO_TYPE |  |
| DISPLAY_OPTIONS | VARCHAR2 | 4000 |  |  | DISPLAY_OPTIONS |  |
| VIDEO_URL | VARCHAR2 | 1000 |  |  | VIDEO_URL |  |
| LEARN_ENROLLMENT_ID | NUMBER |  | 18 |  | Identifier to the learn enrollment |  |
| LEARN_COMMUNITY_ID | NUMBER |  | 18 |  | Identifier to the learn community |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |
| LEARN_ENROLLMENT_TYPE | VARCHAR2 | 80 |  |  | LEARN_ENROLLMENT_TYPE |  |
| ATOM_FEED_CONFIGURATION | VARCHAR2 | 4000 |  |  | ATOM_FEED_CONFIGURATION |  |
| EMBED_TASK_ACTION_CODE | VARCHAR2 | 240 |  |  | EMBED_TASK_ACTION_CODE |  |
| CONTENT_PROVIDER_CODE | VARCHAR2 | 240 |  |  | CONTENT_PROVIDER_CODE |  |
| EMBED_APP_TASK_TYPE_ID | NUMBER |  | 18 |  | EMBED_APP_TASK_TYPE_ID |  |
| DW_INSTRUCTION_ID | NUMBER |  | 18 |  | DW_INSTRUCTION_ID |  |
| ANALYTICS_SUB_TYPE | VARCHAR2 | 80 |  |  | ANALYTICS_SUB_TYPE |  |
| REMINDER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | REMINDER_CONTENT_TYPE |  |
| REMINDER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | REMINDER_CONTENT_DEFN_ID |  |
| BACKGROUND_IMAGE_URL | VARCHAR2 | 4000 |  |  | BACKGROUND_IMAGE_URL |  |
| RAW_IMAGE_URL | VARCHAR2 | 4000 |  |  | RAW_IMAGE_URL |  |
| BACKGROUND_IMAGE_CONTENT_ID | VARCHAR2 | 30 |  |  | BACKGROUND_IMAGE_CONTENT_ID |  |
| RAW_IMAGE_CONTENT_ID | VARCHAR2 | 30 |  |  | RAW_IMAGE_CONTENT_ID |  |
| IMAGE_FILE_NAME | VARCHAR2 | 2048 |  |  | IMAGE_FILE_NAME |  |
| GUIDED_JOURNEY_CODE | VARCHAR2 | 240 |  |  | GUIDED_JOURNEY_CODE |  |
| GUIDED_JOURNEY_TASK_CODES | VARCHAR2 | 4000 |  |  | GUIDED_JOURNEY_TASK_CODES |  |
| DOCUMENT_TYPE_TAGS | VARCHAR2 | 2000 |  |  | DOCUMENT_TYPE_TAGS |  |
| ATTACHMENT_TYPE_TAGS | VARCHAR2 | 2000 |  |  | ATTACHMENT_TYPE_TAGS |  |
| DATE_FROM | DATE |  |  |  | DATE_FROM |  |
| DATE_TO | DATE |  |  |  | DATE_TO |  |
| NOTES_TYPE | VARCHAR2 | 30 |  |  | NOTES_TYPE |  |
| NOTES_REPORT_PATH | VARCHAR2 | 1000 |  |  | NOTES_REPORT_PATH |  |
| COMPLETE_WORKFLOW_CODE | VARCHAR2 | 200 |  |  | COMPLETE_WORKFLOW_CODE |  |
| SAVE_WORKFLOW_CODE | VARCHAR2 | 200 |  |  | SAVE_WORKFLOW_CODE |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_TASKS_IN_CHECKLIST_B_N20 | Non Unique | Default | SGUID |
| PER_TASKS_IN_CHECKLIST_B_PK | Unique | FUSION_TS_TX_DATA | TASK_IN_CHECKLIST_ID, ORA_SEED_SET1 |
| PER_TASKS_IN_CHECKLIST_B_PK1 | Unique | FUSION_TS_TX_DATA | TASK_IN_CHECKLIST_ID, ORA_SEED_SET2 |
| PER_TASKS_IN_CHECKLIST_B_U1 | Unique | Default | CHECKLIST_ID, TASK_IN_CHECKLIST_CODE, ORA_SEED_SET1 |
| PER_TASKS_IN_CHECKLIST_B_U11 | Unique | Default | CHECKLIST_ID, TASK_IN_CHECKLIST_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
