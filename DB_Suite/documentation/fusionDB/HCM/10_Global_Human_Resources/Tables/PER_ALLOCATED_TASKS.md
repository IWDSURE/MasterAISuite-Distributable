# PER_ALLOCATED_TASKS

This table records the tasks within an allocated checklist to a person. These may be copied from templates in PER_TASKS_IN_CHECKLIST, but it is possible to override with values specific to the particular allocation.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocatedtasks-17736.html#perallocatedtasks-17736](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocatedtasks-17736.html#perallocatedtasks-17736)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOCATED_TASKS_PK | ALLOCATED_TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ALLOCATED_TASK_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| SURVEY_RESPONSE_ID | NUMBER |  | 18 |  | SURVEY_RESPONSE_ID |  |
| REMINDER_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for reminder. |  |
| STAGE_ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 |  | STAGE_ALLOCATED_CHECKLIST_ID |  |
| PROCESSING_MODE | VARCHAR2 | 30 |  |  | Identifies if the task need to be processed with SOA/ESS. |  |
| NEXT_REMINDER_DATE | DATE |  |  |  | Identifies the date on which the next reminder for this task need to be sent. |  |
| REMINDER_COUNT | NUMBER |  | 5 |  | Number of reminders sent. |  |
| ATTACHMENT_DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Stores Document type for attachment |  |
| ATT_DOCUMENTS_OF_RECORD_ID | NUMBER |  | 18 |  | Stores Document of record Id |  |
| DOCUMENTS_OF_RECORD_ID | NUMBER |  | 18 |  | Foreign key to HR_DOCUMENTS_OF_RECORD.DOCUMENTS_OF_RECORD_ID. Stores the reference of the document of record |  |
| SIGNER_ADDRESS | VARCHAR2 | 120 |  |  | Stores the Internet Protocol Address of the signer |  |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 |  | Corresponding Checklist Template Task Id. |  |
| RESP_PERFORMER_AVAILABILITY | VARCHAR2 | 30 |  |  | Indicates performer availability of selected performer type. |  |
| DEFAULT_PERF_RESP_TYPE | VARCHAR2 | 30 |  |  | Indicates the Performer type of the defaulted person. |  |
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 | Yes | Identifier of the allocated checklist to which the task belongs |  |
| TASK_NAME | VARCHAR2 | 240 |  |  | Name of the Allocated Task |  |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of the Allocated Task |  |
| MANDATORY_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether the task is mandatory to be completed |  |
| STATUS | VARCHAR2 | 60 |  |  | The status of the task. System Lookup: PER_CHECKLIST_TASK_STATUS
Values -
COM - Completed
INI - Initiated
INP - In Progress
OUT - Outstanding
REJ - Rejected
SUS - Suspended
WIT - Withdrawn
WAI - Deferred to date
DEP - Dependent of other tasks to be completed. |  |
| PERFORMER_ORIG_SYSTEM | VARCHAR2 | 240 |  |  | Username for the Performer of the task |  |
| PERFORMER_ORIG_SYS_ID | NUMBER |  | 18 |  | Person Id for the Performer of the task |  |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | Denotes the Responsibility Type this Task has to be performed by. |  |
| RESPONSIBILITY_TYPE_GUID | VARCHAR2 | 4000 |  |  | The Global User Ids of the  Responsible Persons this Task has to be performed by. |  |
| TASK_OWNER_PERSON_ID | NUMBER |  | 18 |  | PersonId for the Owner of the task |  |
| TASK_OWNER_USERNAME | VARCHAR2 | 240 |  |  | User name for the owner of the task |  |
| TASK_PERFORMERS | VARCHAR2 | 4000 |  |  | Stores guid of all performers |  |
| TASK_OWNERS | VARCHAR2 | 4000 |  |  | Stores guid of all owners |  |
| TASK_SEQUENCE | NUMBER |  | 9 |  | Obsolete. |  |
| TASK_PERCENTAGE_COMPLETE | NUMBER |  | 3 |  | Completion Percentage of the Allocated Task |  |
| TARGET_START_DATE | DATE |  |  |  | Target Start Date for the task |  |
| TARGET_END_DATE | DATE |  |  |  | Target End Date for the task |  |
| ACTUAL_START_DATE | DATE |  |  |  | Actual Start Date for the task |  |
| ACTUAL_END_DATE | DATE |  |  |  | Actual End Date for the task |  |
| ACTION_URL | VARCHAR2 | 1000 |  |  | This is a drill down URL for this task |  |
| TASK_COMMENTS | VARCHAR2 | 4000 |  |  | Comments by the Task Performer about this Task |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Task Attributes (PER_PERSON_ALLOCATED_TASKS_DFF) |
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
| ACTION_TYPE | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_TASK_ACTION_TYPES
Values: ORA_NONE - None
ORA_EXTERNAL_URL - External URL
ORA_APP_PROCESS - Application Task
ORA_DOC_RECORD - Document of Record
ORA_CUSTOM_FORM - Custom Form |  |
| TASK_CONFIGURATION | VARCHAR2 | 4000 |  |  | Task Configuration |  |
| TASK_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to PER_TASK_ACTIONS_B.TASK_ACTION_ID
Task Definition to use when Action Type = Application Task |  |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Document Type associated with this task when Action Type = Document of Record |  |
| FLEX_CONTEXT_CODE | VARCHAR2 | 80 |  |  | Flexfield Context Code when the Action Type = Custom Form |  |
| DEF_ALLOCATION_DATE | DATE |  |  |  | Deferred Allocation Date |  |
| DEPENDENT_ON_TASKS | VARCHAR2 | 4000 |  |  | Comma seperated list of all ALLOCATED_TASK_IDs based on which the current task will be unblocked. |  |
| ACTIVATION_ELIGY_PRFL_ID | NUMBER |  | 18 |  | ACTIVATION_ELIGY_PRFL_ID |  |
| REMINDER_RECURRENCE | VARCHAR2 | 30 |  |  | Reminder recurrence (NEVER, EVERY, 1 .. 10). Default NEVER |  |
| REMINDER_DURATION | VARCHAR2 | 30 |  |  | Reminder duration P<Num Days>D |  |
| REMINDER_RELATIVE_TO | VARCHAR2 | 30 |  |  | Reminder relative to ASSIGNED or DUE |  |
| GENERATE_ATOM_FEED | VARCHAR2 | 30 |  |  | Identifies if ATOM feed needs to be generated |  |
| TARGET_DURATION | NUMBER |  | 9 |  | Task expiration duration |  |
| TARGET_DURATION_UOM | VARCHAR2 | 30 |  |  | System Lookup: CHECKLIST_QUALIFYING_UNITS
Values: D - Days
W - Weeks
M - Months
Task expiration duration unit of measure. |  |
| TASK_DELAY_DURATION | NUMBER |  | 9 |  | TASK_DELAY_DURATION |  |
| TASK_DELAY_DURATION_UOM | NUMBER |  | 9 |  | Task extension duration |  |
| MEETING_OFFSET | NUMBER |  | 9 |  | Meeting Offset from Action Date |  |
| MEETING_TIME | VARCHAR2 | 10 |  |  | Meeting Time |  |
| EXPIRY_DAYS | NUMBER |  | 9 |  | Expiry Days |  |
| CONTACT_DETAILS | VARCHAR2 | 1000 |  |  | CONTACT_DETAILS |  |
| DETAIL_CHECKLIST_ID | NUMBER |  | 18 |  | DETAIL_CHECKLIST_ID |  |
| DETAIL_ALLOC_CHECKLIST_ID | NUMBER |  | 18 |  | DETAIL_ALLOC_CHECKLIST_ID |  |
| OWNER_RESP_TYPE | VARCHAR2 | 30 |  |  | OWNER_RESP_TYPE |  |
| OWNER_RESP_TYPE_USERS | VARCHAR2 | 4000 |  |  | OWNER_RESP_TYPE_USERS |  |
| ABS_ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 |  | ABS_ALLOCATED_CHECKLIST_ID |  |
| TASK_ACTION_CODE | VARCHAR2 | 240 |  |  | Contains the action code associated with the task. |  |
| SIGN_TEMPLATE | VARCHAR2 | 240 |  |  | Stores the e-signature template details for action type = ORA_CHK_ESIGN |  |
| SIGN_DOCUMENT | VARCHAR2 | 400 |  |  | Stores the e-signature document details for action type = ORA_CHK_ESIGN |  |
| COMPLETED_BY | VARCHAR2 | 64 |  |  | User name of the user who completed the task |  |
| COMPLETION_DATE | DATE |  |  |  | The date on which the task is completed. |  |
| ESIGN_TYPE | VARCHAR2 | 30 |  |  | Specifies Esignature Type |  |
| SIGN_DATE | DATE |  |  |  | Specifies Sign Date |  |
| SIGNER_NAME | VARCHAR2 | 120 |  |  | Specifies Signer Name |  |
| SIGNER_EMAIL | VARCHAR2 | 400 |  |  | Specifies Email Id of Signer |  |
| DOCUMENT_ENTITY_ID | NUMBER |  | 18 |  | Specifies Document Entity Id |  |
| REOPEN_DATE | DATE |  |  |  | Specifies Task Reopen Date |  |
| REOPENED_BY | VARCHAR2 | 64 |  |  | Specifies Name of the Person Who reopened task |  |
| REPORT_PATH | VARCHAR2 | 1000 |  |  | It contains the BI Publisher report folder path followed by the report name concatenated with a / symbol with optionally a list of parameters in the format of  parameter_name is equals to parameter value . The first parameter is prefixed with ? and & to denote each additional parameter |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Stores the Questionnaire Identifier for the Questionnaire associated with this task |  |
| ERROR_DETAILS | VARCHAR2 | 4000 |  |  | Details of any integration errors |  |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |  |
| LEARN_CONTENT_TYPE | VARCHAR2 | 80 |  |  | LEARN_CONTENT_TYPE |  |
| REPORT_PARAMETERS | VARCHAR2 | 4000 |  |  | REPORT_PARAMETERS |  |
| ANALYTICS_PATH | VARCHAR2 | 1000 |  |  | Report path for analytics task type |  |
| ENABLE_TASK_EXPIRY | VARCHAR2 | 4 |  |  | ENABLE_TASK_EXPIRY |  |
| EXPIRY_RELATIVE_TO | VARCHAR2 | 30 |  |  | EXPIRY_RELATIVE_TO |  |
| EXPIRY_DATE | DATE |  |  |  | EXPIRY_DATE |  |
| TASK_FEATURE1 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE2 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE3 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE4 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE5 | VARCHAR2 | 4000 |  |  | Stores the Task feature |  |
| TASK_FEATURE_DETAILS | CLOB |  |  |  | Stores the Task feature details |  |
| REASSIGNED_DATE | DATE |  |  |  | Stores the Reassigned date |  |
| REASSIGNED_BY | VARCHAR2 | 64 |  |  | Stores guid of Reassigned By |  |
| TASK_INITIATOR | VARCHAR2 | 64 |  |  | Stores guid of Initiator |  |
| TASK_INITIATOR_PERSON_ID | NUMBER |  | 18 |  | Person Id for the Initiator of the task |  |
| COMBINED_NOTIFICATION_ID | NUMBER |  | 18 |  | Stores the combined notification id |  |
| SYNCH_HISTORY | VARCHAR2 | 4000 |  |  | SYNCH_HISTORY |  |
| VIDEO_TYPE | VARCHAR2 | 80 |  |  | VIDEO_TYPE |  |
| DISPLAY_OPTIONS | VARCHAR2 | 4000 |  |  | DISPLAY_OPTIONS |  |
| VIDEO_URL | VARCHAR2 | 1000 |  |  | VIDEO_URL |  |
| LEARN_ENROLLMENT_ID | NUMBER |  | 18 |  | Identifier to the learn enrollment |  |
| LEARN_COMMUNITY_ID | NUMBER |  | 18 |  | Identifier to the learn community |  |
| LEARN_ENROLLMENT_TYPE | VARCHAR2 | 80 |  |  | LEARN_ENROLLMENT_TYPE |  |
| ATOM_FEED_CONFIGURATION | VARCHAR2 | 4000 |  |  | ATOM_FEED_CONFIGURATION |  |
| EMBED_TASK_ACTION_CODE | VARCHAR2 | 240 |  |  | EMBED_TASK_ACTION_CODE |  |
| ESIGN_SIGNATURE | CLOB |  |  |  | ESIGN_SIGNATURE |  |
| CONTENT_PROVIDER_CODE | VARCHAR2 | 240 |  |  | CONTENT_PROVIDER_CODE |  |
| EMBED_APP_TASK_TYPE_ID | NUMBER |  | 18 |  | EMBED_APP_TASK_TYPE_ID |  |
| OBJECT_GROUP_CODE | VARCHAR2 | 64 |  |  | OBJECT_GROUP_CODE |  |
| ANALYTICS_SUB_TYPE | VARCHAR2 | 80 |  |  | ANALYTICS_SUB_TYPE |  |
| REMINDER_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | REMINDER_CONTENT_TYPE |  |
| REMINDER_CONTENT_DEFN_ID | NUMBER |  | 18 |  | REMINDER_CONTENT_DEFN_ID |  |
| GUIDED_JOURNEY_CODE | VARCHAR2 | 240 |  |  | GUIDED_JOURNEY_CODE |  |
| GUIDED_JOURNEY_TASK_CODES | VARCHAR2 | 4000 |  |  | GUIDED_JOURNEY_TASK_CODES |  |
| ALLOCATION_TIMEZONE | VARCHAR2 | 50 |  |  | ALLOCATION_TIMEZONE |  |
| DOCUMENT_TYPE_TAGS | VARCHAR2 | 2000 |  |  | DOCUMENT_TYPE_TAGS |  |
| ATTACHMENT_TYPE_TAGS | VARCHAR2 | 2000 |  |  | ATTACHMENT_TYPE_TAGS |  |
| NOTES_TYPE | VARCHAR2 | 30 |  |  | NOTES_TYPE |  |
| NOTES_REPORT_PATH | VARCHAR2 | 1000 |  |  | NOTES_REPORT_PATH |  |
| COMPLETE_WORKFLOW_CODE | VARCHAR2 | 200 |  |  | COMPLETE_WORKFLOW_CODE |  |
| SAVE_WORKFLOW_CODE | VARCHAR2 | 200 |  |  | SAVE_WORKFLOW_CODE |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALLOCATED_TASKS_N1 | Non Unique | Default | ALLOCATED_CHECKLIST_ID |
| PER_ALLOCATED_TASKS_N10 | Non Unique | Default | NEXT_REMINDER_DATE |
| PER_ALLOCATED_TASKS_N2 | Non Unique | Default | ACTUAL_END_DATE |
| PER_ALLOCATED_TASKS_N3 | Non Unique | Default | ABS_ALLOCATED_CHECKLIST_ID |
| PER_ALLOCATED_TASKS_N4 | Non Unique | Default | DETAIL_ALLOC_CHECKLIST_ID |
| PER_ALLOCATED_TASKS_N5 | Non Unique | Default | UPPER("RESPONSIBILITY_TYPE_GUID") |
| PER_ALLOCATED_TASKS_N6 | Non Unique | Default | PERFORMER_ORIG_SYS_ID |
| PER_ALLOCATED_TASKS_N7 | Non Unique | Default | UPPER("PERFORMER_ORIG_SYSTEM") |
| PER_ALLOCATED_TASKS_N8 | Non Unique | Default | TASK_PERFORMERS |
| PER_ALLOCATED_TASKS_N9 | Non Unique | Default | DEF_ALLOCATION_DATE |
| PER_ALLOCATED_TASKS_PK | Unique | Default | ALLOCATED_TASK_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
