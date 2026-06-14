# PER_CHECKLISTS_B

This table records the checklist templates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistsb-25500.html#perchecklistsb-25500](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistsb-25500.html#perchecklistsb-25500)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLISTS_B_PK | CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| CHECKLIST_ID | NUMBER |  | 18 | Yes | System-generated primary key column. Surrogate Key |  |
| ACCESS_LEVEL | VARCHAR2 | 30 |  |  | ACCESS_LEVEL |  |
| SECURITY_ENABLED | VARCHAR2 | 4 |  |  | SECURITY_ENABLED |  |
| ACCESS_GROUP_ID | NUMBER |  | 18 |  | ACCESS_GROUP_ID |  |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | LEVEL_CODE |  |
| LEVEL_VALUE | NUMBER |  | 18 |  | LEVEL_VALUE |  |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |  |
| PROCESSING_MODE | VARCHAR2 | 30 |  |  | Identifies if the task need to be processed with SOA/ESS. |  |
| ASSIGNED_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for welcome notification. |  |
| FCL_TEMPLATE_ID | NUMBER |  | 18 |  | FCL_TEMPLATE_ID |  |
| COMBINED_TASK_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for combined notification. |  |
| BACKGROUND_THUMBNAIL_URL | VARCHAR2 | 4000 |  |  | BACKGROUND_THUMBNAIL_URL |  |
| EVALUATION_MODE | VARCHAR2 | 10 |  |  | Evaluation Mode. |  |
| BACKGROUND_IMAGE_URL | VARCHAR2 | 4000 |  |  | Background Image URL |  |
| CHECKLIST_CATEGORY | VARCHAR2 | 60 |  | Yes | Signifies category of the checklist. For example ONBOARD or OFFBOARD. |  |
| EVENT_REASON_ID | NUMBER |  |  |  | Action that results in the checklist template getting automatically allocated to the person experiencing the action. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
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
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code derived from Legal Entity |  |
| ACTIVE_INACTIVE_FLAG | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_STATUS
Values: ORA_DRAFT - Draft
ORA_ACTIVE - Active
ORA_INACTIVE - In active |  |
| ALLOW_ALLOCATION_CREATE | VARCHAR2 | 30 |  |  | Indicates that this  checklist can be used for creation of allocated checklist. |  |
| ALLOW_ALLOCATION_UPDATE | VARCHAR2 | 30 |  |  | Indicates that this  checklist can be used for updation of allocated checklist. |  |
| ALLOW_ALLOCATION_DELETE | VARCHAR2 | 30 |  |  | Indicates that this  checklist can be used for deletion of allocated checklist. |  |
| CHECKLIST_CODE | VARCHAR2 | 240 |  |  | Checklist template code |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Checklist Attributes (PER_CHECKLISTS_DFF) |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ELIGY_PRFL.ELIGY_PRFL_ID (Eligibility Profile for Checklist) |  |
| ALLOCATED_ON | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_ALCTD_ON
Values: ORA_IMMEDIATE - Immediate
ORA_EVENT_DATE - On or after event date |  |
| OFFSET_DAYS | NUMBER |  | 5 |  | Offset days for allocation of checklist w.r.t to the event date. |  |
| DATE_FROM | DATE |  |  |  | Checklist active from date |  |
| DATE_TO | DATE |  |  |  | Checklist active up to date. |  |
| COMPLETED_ON | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_CMP_ON
Values: ORA_MAND_COMPLETE- All mandatory tasks are complete.
ORA_MAND_WITH_OFFSET - All mandatory tasks complete with a grace period.
ORA_ALL_COMPLETE - All tasks are complete. |  |
| COMPLETION_OFFSET_DAYS | NUMBER |  | 5 |  | Offset days for checklist completion w.r.t the last mandatory task completion date |  |
| TRIGGER_TYPE | VARCHAR2 | 30 |  |  | Valid values are

ORA_EMPL_ACTION - Employment Action

ORA_CHECKLIST_ACTION - Checklist Action |  |
| CHECKLIST_SUB_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_SUB_CATEGORY |  |
| BACKGROUND_IMAGE | BLOB |  |  |  | BACKGROUND_IMAGE |  |
| CROPPED_BACKGROUND_IMAGE | BLOB |  |  |  | CROPPED_BACKGROUND_IMAGE |  |
| CHECKLIST_FEATURE1 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE2 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE3 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE4 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE5 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE6 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE7 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE8 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE9 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE10 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |
| CHECKLIST_FEATURE_DETAILS | CLOB |  |  |  | Stores the Checklist feature details |  |
| ARCHIVE_OFFSET | NUMBER |  | 5 |  | ARCHIVE_OFFSET |  |
| PURGE_OFFSET | NUMBER |  | 5 |  | PURGE_OFFSET |  |
| CONTEXTUAL_ACTION | VARCHAR2 | 240 |  |  | CONTEXTUAL_ACTION |  |
| CONTEXT | VARCHAR2 | 240 |  |  | CONTEXT |  |
| RAW_IMAGE_CONTENT_ID | VARCHAR2 | 30 |  |  | RAW_IMAGE_CONTENT_ID |  |
| RAW_IMAGE_URL | VARCHAR2 | 4000 |  |  | RAW_IMAGE_URL |  |
| BACKGROUND_IMAGE_CONTENT_ID | VARCHAR2 | 30 |  |  | BACKGROUND_IMAGE_CONTENT_ID |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |
| IMAGE_FILE_NAME | VARCHAR2 | 2048 |  |  | IMAGE_FILE_NAME |  |
| ALL_ROLES_VIEW_ASSIGNED | VARCHAR2 | 4 |  |  | ALL_ROLES_VIEW_ASSIGNED |  |
| RECURRENT_FLAG | VARCHAR2 | 4 |  | Yes | RECURRENT_FLAG |  |
| GENERATE_ATOM_FEED | VARCHAR2 | 30 |  |  | GENERATE_ATOM_FEED |  |
| ATOM_FEED_CONFIGURATION | VARCHAR2 | 4000 |  |  | ATOM_FEED_CONFIGURATION |  |
| OBJECT_REFERENCE_ID | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID |  |
| OBJECT_REFERENCE_ID1 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID1 |  |
| OBJECT_REFERENCE_ID2 | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID2 |  |
| OBJECT_REFERENCE_KEY1 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY1 |  |
| OBJECT_REFERENCE_KEY2 | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY2 |  |
| SUBJECT_TYPE | VARCHAR2 | 240 |  | Yes | SUBJECT_TYPE |  |
| USER_GUID | VARCHAR2 | 64 |  |  | USER_GUID |  |
| TASK_GROUP | VARCHAR2 | 30 |  |  | TASK_GROUP |  |
| OBJECT_REFERENCE_KEY | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY |  |
| DISPLAY_TYPE | VARCHAR2 | 30 |  | Yes | DISPLAY_TYPE |  |
| ENABLE_EXTERNAL_FLAG | VARCHAR2 | 30 |  | Yes | ENABLE_EXTERNAL_FLAG |  |
| JOURNEY_DISPLAY_MODE | VARCHAR2 | 30 |  | Yes | JOURNEY_DISPLAY_MODE |  |
| ASSIGNED_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | ASSIGNED_CONTENT_TYPE |  |
| ASSIGNED_CONTENT_DEFN_ID | NUMBER |  | 18 |  | ASSIGNED_CONTENT_DEFN_ID |  |
| FCL_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | FCL_CONTENT_TYPE |  |
| FCL_CONTENT_DEFN_ID | NUMBER |  | 18 |  | FCL_CONTENT_DEFN_ID |  |
| ALLOCATION_CONTROL_CODE | VARCHAR2 | 30 |  | Yes | ALLOCATION_CONTROL_CODE |  |
| ALLOCATION_TIMEZONE | VARCHAR2 | 50 |  |  | ALLOCATION_TIMEZONE |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLISTS_B_N1 | Non Unique | Default | LEVEL_CODE, LEVEL_VALUE |
| PER_CHECKLISTS_B_N2 | Non Unique | Default | CHECKLIST_CODE |
| PER_CHECKLISTS_B_N20 | Non Unique | Default | SGUID |
| PER_CHECKLISTS_B_PK | Unique | FUSION_TS_TX_IDX | CHECKLIST_ID, ORA_SEED_SET1 |
| PER_CHECKLISTS_B_PK1 | Unique | FUSION_TS_TX_IDX | CHECKLIST_ID, ORA_SEED_SET2 |
| PER_CHECKLISTS_B_U1 | Unique | Default | BUSINESS_GROUP_ID, LEVEL_CODE, LEVEL_VALUE, CHECKLIST_CATEGORY, CHECKLIST_CODE, LEGISLATION_CODE, ORA_SEED_SET1 |
| PER_CHECKLISTS_B_U11 | Unique | Default | BUSINESS_GROUP_ID, LEVEL_CODE, LEVEL_VALUE, CHECKLIST_CATEGORY, CHECKLIST_CODE, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
