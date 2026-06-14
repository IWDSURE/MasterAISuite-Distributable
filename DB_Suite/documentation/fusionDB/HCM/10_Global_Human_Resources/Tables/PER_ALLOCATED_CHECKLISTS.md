# PER_ALLOCATED_CHECKLISTS

This table records the checklists allocated to a person. These may be copied from templates in PER_CHECKLISTS, but it is possible to override with values specific to the particular allocation.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocatedchecklists-31189.html#perallocatedchecklists-31189](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocatedchecklists-31189.html#perallocatedchecklists-31189)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOCATED_CHECKLISTS_PK | ALLOCATED_CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 | Yes | Allocated Checklist Identifier |  | Active |
| CHECKLIST_ALLOCATION_ID | NUMBER |  | 18 |  | CHECKLIST_ALLOCATION_ID |  |  |
| SECURITY_ENABLED | VARCHAR2 | 4 |  |  | SECURITY_ENABLED |  |  |
| CHECKLIST_LEVEL_CODE | VARCHAR2 | 30 |  |  | CHECKLIST_LEVEL_CODE |  |  |
| ACCESS_GROUP_ID | NUMBER |  |  |  | ACCESS_GROUP_ID |  |  |
| INITIATOR_PERSON_ID | NUMBER |  | 18 |  | Initiator person. |  |  |
| INITIATOR_USER | VARCHAR2 | 64 |  |  | Initiator user. |  |  |
| SELF_ASSIGNED_FLAG | VARCHAR2 | 4 |  |  | If checklist is self assigned. |  |  |
| OBJECT_ID | NUMBER |  | 18 |  | OBJECT_ID |  |  |
| ALLOCATION_NOTIFIED_FLAG | VARCHAR2 | 4 |  |  | Indicates if a checklist assigned notification is sent. |  |  |
| PROCESSING_MODE | VARCHAR2 | 30 |  |  | Identifies if the checklist need to be processed with SOA/ESS. |  |  |
| DEF_COMPLETION_DATE | DATE |  |  |  | Date on which the checklist completion is deferred. |  |  |
| ASSIGNED_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for welcome notification. |  |  |
| FCL_TEMPLATE_ID | NUMBER |  | 18 |  | FCL_TEMPLATE_ID |  |  |
| COMBINED_TASK_TEMPLATE_ID | NUMBER |  | 18 |  | Alert template for combined notification. |  |  |
| BACKGROUND_THUMBNAIL_URL | VARCHAR2 | 4000 |  |  | BACKGROUND_THUMBNAIL_URL |  |  |
| BACKGROUND_IMAGE_URL | VARCHAR2 | 4000 |  |  | Background Image URL |  |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from legal entity. |  |  |
| CHECKLIST_INSTANCE | VARCHAR2 | 20 |  |  | CHECKLIST_INSTANCE |  |  |
| CHECKLIST_ID | NUMBER |  | 18 |  | Template Checklist Identifier |  | Active |
| PERSON_ID | NUMBER |  | 18 |  | Person Identifier for whom this checklist has been allocated |  | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |  |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Identifier for whom this checklist has been allocated |  | Active |
| CHECKLIST_NAME | VARCHAR2 | 240 |  |  | Name of the Allocated Checklist |  | Active |
| DESCRIPTION | VARCHAR2 | 360 |  |  | Description of the Allocated Checklist |  | Active |
| CHECKLIST_CATEGORY | VARCHAR2 | 60 |  |  | Category of the Allocated Checklist |  | Active |
| CHECKLIST_STATUS | VARCHAR2 | 60 |  |  | The status of the checklist. System Lookup: PER_CHECKLIST_TASK_STATUS
Values -
COM - Completed
INI - Initiated
DEF - Deferred |  |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Allocated Checklist Attributes (PER_ALLOCATED_CHECKLISTS_DFF) |  |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield structure defining column |  | Active |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer-Descriptive Flexfield Segment |  | Active |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |  |
| EVENT_DATE | DATE |  |  |  | Date when this event was raised |  |  |
| ALLOCATION_DATE | DATE |  |  |  | Date on which this checklist is allocated |  |  |
| ACTION_DATE | DATE |  |  |  | Date as of which the action on the employee record is active. |  |  |
| COMPLETED_ON | VARCHAR2 | 30 |  |  | System Lookup: ORA_CHK_CHECKLIST_CMP_ON
Values: ORA_MAND_COMPLETE- All mandatory tasks are complete.
ORA_MAND_WITH_OFFSET - All mandatory tasks complete with a grace period.
ORA_ALL_COMPLETE - All tasks are complete. |  |  |
| COMPLETION_OFFSET_DAYS | NUMBER |  | 5 |  | COMPLETION_OFFSET_DAYS |  |  |
| COMPLETION_DATE | DATE |  |  |  | Expected/Actual Completion Date |  |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | The instance of the action associated with this checklist. |  |  |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | The worker employment |  |  |
| ALLOCATION_DETAILS | VARCHAR2 | 4000 |  |  | The checklist allocation details |  |  |
| CHECKLIST_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to PER_CHECKLIST_ACTIONS.CHECKLIST_ACTION_ID |  |  |
| CHECKLIST_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_CHECKLIST_ACT_OCCURRENCES.CHECKLIST_ACTION_OCCURRENCE_ID |  |  |
| CHECKLIST_SUB_CATEGORY | VARCHAR2 | 60 |  |  | CHECKLIST_SUB_CATEGORY |  |  |
| BACKGROUND_IMAGE | BLOB |  |  |  | BACKGROUND_IMAGE |  |  |
| CROPPED_BACKGROUND_IMAGE | BLOB |  |  |  | CROPPED_BACKGROUND_IMAGE |  |  |
| CHECKLIST_FEATURE1 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE2 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE3 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE4 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE5 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE6 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE7 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE8 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE9 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE10 | VARCHAR2 | 4000 |  |  | Stores the Checklist feature |  |  |
| CHECKLIST_FEATURE_DETAILS | CLOB |  |  |  | Stores the Checklist feature details |  |  |
| ARCHIVE_OFFSET | NUMBER |  | 5 |  | ARCHIVE_OFFSET |  |  |
| PURGE_OFFSET | NUMBER |  | 5 |  | PURGE_OFFSET |  |  |
| SYNCH_HISTORY | VARCHAR2 | 4000 |  |  | SYNCH_HISTORY |  |  |
| CONTEXTUAL_ACTION | VARCHAR2 | 240 |  |  | CONTEXTUAL_ACTION |  |  |
| CONTEXT | VARCHAR2 | 240 |  |  | CONTEXT |  |  |
| ALL_ROLES_VIEW_ASSIGNED | VARCHAR2 | 4 |  |  | ALL_ROLES_VIEW_ASSIGNED |  |  |
| RECURRENT_FLAG | VARCHAR2 | 4 |  | Yes | RECURRENT_FLAG |  |  |
| GENERATE_ATOM_FEED | VARCHAR2 | 30 |  |  | Identifies if ATOM feed needs to be generated |  |  |
| ATOM_FEED_CONFIGURATION | VARCHAR2 | 4000 |  |  | ATOM_FEED_CONFIGURATION |  |  |
| ALLOCATION_METHOD | VARCHAR2 | 80 |  |  | ALLOCATION_METHOD |  |  |
| ALLOCATION_SOURCE | VARCHAR2 | 30 |  |  | ALLOCATION_SOURCE |  |  |
| OBJECT_REFERENCE_ID | NUMBER |  | 18 |  | OBJECT_REFERENCE_ID |  |  |
| SUBJECT_TYPE | VARCHAR2 | 240 |  | Yes | SUBJECT_TYPE |  |  |
| SUBJECT_KEY | VARCHAR2 | 240 |  |  | SUBJECT_KEY |  |  |
| ENABLE_MULTI_PERFORMER | VARCHAR2 | 4 |  | Yes | ENABLE_MULTI_PERFORMER |  |  |
| OBJECT_REFERENCE_KEY | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_KEY |  |  |
| DISPLAY_TYPE | VARCHAR2 | 30 |  | Yes | DISPLAY_TYPE |  |  |
| JOURNEY_DISPLAY_MODE | VARCHAR2 | 30 |  | Yes | JOURNEY_DISPLAY_MODE |  |  |
| ASSIGNED_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | ASSIGNED_CONTENT_TYPE |  |  |
| ASSIGNED_CONTENT_DEFN_ID | NUMBER |  | 18 |  | ASSIGNED_CONTENT_DEFN_ID |  |  |
| FCL_CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | FCL_CONTENT_TYPE |  |  |
| FCL_CONTENT_DEFN_ID | NUMBER |  | 18 |  | FCL_CONTENT_DEFN_ID |  |  |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | LEVEL_CODE |  |  |
| LEVEL_VALUE | NUMBER |  | 18 |  | LEVEL_VALUE |  |  |
| ACCESS_LEVEL | VARCHAR2 | 30 |  |  | ACCESS_LEVEL |  |  |
| ALLOCATION_TIMEZONE | VARCHAR2 | 50 |  |  | ALLOCATION_TIMEZONE |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALLOCATED_CHECKLISTS_N1 | Non Unique | Default | DEF_COMPLETION_DATE |
| PER_ALLOCATED_CHECKLISTS_N2 | Non Unique | Default | PERSON_ID, CHECKLIST_ID |
| PER_ALLOCATED_CHECKLISTS_N3 | Non Unique | Default | ALLOCATION_DATE |
| PER_ALLOCATED_CHECKLISTS_PK | Unique | FUSION_TS_TX_IDX | ALLOCATED_CHECKLIST_ID |
| PER_ALLOCATED_CHECKLISTS_U1 | Unique | Default | PERSON_ID, CHECKLIST_CATEGORY, CHECKLIST_NAME, CHECKLIST_INSTANCE, ALLOCATED_CHECKLIST_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
