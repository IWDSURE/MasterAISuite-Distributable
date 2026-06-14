# PER_CHECKLISTS_B_

This table records the checklist templates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistsb-30577.html#perchecklistsb-30577](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistsb-30577.html#perchecklistsb-30577)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLISTS_B_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_ID | NUMBER |  | 18 | Yes | System-generated primary key column. Surrogate Key |
| ACCESS_LEVEL | VARCHAR2 | 30 |  |  | ACCESS_LEVEL |
| SECURITY_ENABLED | VARCHAR2 | 4 |  |  | SECURITY_ENABLED |
| ACCESS_GROUP_ID | NUMBER |  | 18 |  | ACCESS_GROUP_ID |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | LEVEL_CODE |
| LEVEL_VALUE | NUMBER |  | 18 |  | LEVEL_VALUE |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| PROCESSING_MODE | VARCHAR2 | 30 |  |  | Identifies if the task need to be processed with SOA/ESS. |
| ASSIGNED_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for welcome notification. |
| FCL_TEMPLATE_ID | NUMBER |  | 18 |  | FCL_TEMPLATE_ID |
| COMBINED_TASK_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for combined notification. |
| BACKGROUND_THUMBNAIL_URL | VARCHAR2 | 4000 |  |  | BACKGROUND_THUMBNAIL_URL |
| EVALUATION_MODE | VARCHAR2 | 10 |  |  | Evaluation Mode. |
| BACKGROUND_IMAGE_URL | VARCHAR2 | 4000 |  |  | Background Image URL |
| CHECKLIST_CATEGORY | VARCHAR2 | 60 |  |  | Signifies category of the checklist. For example ONBOARD or OFFBOARD. |
| EVENT_REASON_ID | NUMBER |  |  |  | Action that results in the checklist template getting automatically allocated to the person experiencing the action. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code derived from Legal Entity |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_STATUS
Values: ORA_DRAFT - Draft
ORA_ACTIVE - Active
ORA_INACTIVE - In active |
| ALLOW_ALLOCATION_CREATE | VARCHAR2 | 30 |  |  | Indicates that this  checklist can be used for creation of allocated checklist. |
| ALLOW_ALLOCATION_UPDATE | VARCHAR2 | 30 |  |  | Indicates that this  checklist can be used for updation of allocated checklist. |
| ALLOW_ALLOCATION_DELETE | VARCHAR2 | 30 |  |  | Indicates that this  checklist can be used for deletion of allocated checklist. |
| CHECKLIST_CODE | VARCHAR2 | 240 |  |  | Checklist template code |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ELIGY_PRFL.ELIGY_PRFL_ID (Eligibility Profile for Checklist) |
| ALLOCATED_ON | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_ALCTD_ON
Values: ORA_IMMEDIATE - Immediate
ORA_EVENT_DATE - On or after event date |
| OFFSET_DAYS | NUMBER |  | 5 |  | Offset days for allocation of checklist w.r.t to the event date. |
| DATE_FROM | DATE |  |  |  | Checklist active from date |
| DATE_TO | DATE |  |  |  | Checklist active up to date. |
| COMPLETED_ON | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_CMP_ON
Values: ORA_MAND_COMPLETE- All mandatory tasks are complete.
ORA_MAND_WITH_OFFSET - All mandatory tasks complete with a grace period.
ORA_ALL_COMPLETE - All tasks are complete. |
| COMPLETION_OFFSET_DAYS | NUMBER |  | 5 |  | Offset days for checklist completion w.r.t the last mandatory task completion date |
| TRIGGER_TYPE | VARCHAR2 | 30 |  |  | Valid values are

ORA_EMPL_ACTION - Employment Action

ORA_CHECKLIST_ACTION - Checklist Action |
| CHECKLIST_SUB_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_SUB_CATEGORY |
| BACKGROUND_IMAGE | BLOB |  |  |  | BACKGROUND_IMAGE |
| CROPPED_BACKGROUND_IMAGE | BLOB |  |  |  | CROPPED_BACKGROUND_IMAGE |
| CHECKLIST_FEATURE1 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE2 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE3 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE4 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE5 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE6 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE7 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE8 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE9 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE10 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |
| CHECKLIST_FEATURE_DETAILS | CLOB |  |  |  | Stores the Checklist feature details |
| ARCHIVE_OFFSET | NUMBER |  | 5 |  | ARCHIVE_OFFSET |
| PURGE_OFFSET | NUMBER |  | 5 |  | PURGE_OFFSET |
| CONTEXTUAL_ACTION | VARCHAR2 | 240 |  |  | CONTEXTUAL_ACTION |
| CONTEXT | VARCHAR2 | 240 |  |  | CONTEXT |
| RAW_IMAGE_CONTENT_ID | VARCHAR2 | 30 |  |  | RAW_IMAGE_CONTENT_ID |
| RAW_IMAGE_URL | VARCHAR2 | 4000 |  |  | RAW_IMAGE_URL |
| BACKGROUND_IMAGE_CONTENT_ID | VARCHAR2 | 30 |  |  | BACKGROUND_IMAGE_CONTENT_ID |
| IMAGE_FILE_NAME | VARCHAR2 | 2048 |  |  | IMAGE_FILE_NAME |
| ALL_ROLES_VIEW_ASSIGNED | VARCHAR2 | 4 |  |  | ALL_ROLES_VIEW_ASSIGNED |
| RECURRENT_FLAG | VARCHAR2 | 4 |  |  | RECURRENT_FLAG |
| GENERATE_ATOM_FEED | VARCHAR2 | 30 |  |  | GENERATE_ATOM_FEED |
| ATOM_FEED_CONFIGURATION | VARCHAR2 | 4000 |  |  | ATOM_FEED_CONFIGURATION |
| OBJECT_REFERENCE_ID | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID |
| OBJECT_REFERENCE_ID1 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID1 |
| OBJECT_REFERENCE_ID2 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID2 |
| OBJECT_REFERENCE_KEY1 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY1 |
| OBJECT_REFERENCE_KEY2 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY2 |
| SUBJECT_TYPE | VARCHAR2 | 240 |  |  | SUBJECT_TYPE |
| USER_GUID | VARCHAR2 | 64 |  |  | USER_GUID |
| TASK_GROUP | VARCHAR2 | 30 |  |  | TASK_GROUP |
| OBJECT_REFERENCE_KEY | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY |
| DISPLAY_TYPE | VARCHAR2 | 30 |  |  | DISPLAY_TYPE |
| ENABLE_EXTERNAL_FLAG | VARCHAR2 | 30 |  |  | ENABLE_EXTERNAL_FLAG |
| JOURNEY_DISPLAY_MODE | VARCHAR2 | 30 |  |  | JOURNEY_DISPLAY_MODE |
| ASSIGNED_CONTENT_TYPE | VARCHAR2 | 30 |  |  | ASSIGNED_CONTENT_TYPE |
| ASSIGNED_CONTENT_DEFN_ID | NUMBER |  | 18 |  | ASSIGNED_CONTENT_DEFN_ID |
| FCL_CONTENT_TYPE | VARCHAR2 | 30 |  |  | FCL_CONTENT_TYPE |
| FCL_CONTENT_DEFN_ID | NUMBER |  | 18 |  | FCL_CONTENT_DEFN_ID |
| ALLOCATION_CONTROL_CODE | VARCHAR2 | 30 |  |  | ALLOCATION_CONTROL_CODE |
| ALLOCATION_TIMEZONE | VARCHAR2 | 50 |  |  | ALLOCATION_TIMEZONE |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PCBN1_ | Non Unique | Default | CHECKLIST_ID, LAST_UPDATE_DATE |
| PER_CHECKLISTS_B_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, CHECKLIST_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
