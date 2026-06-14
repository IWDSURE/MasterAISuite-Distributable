# WLF_LI_CLASSES_F

Table to store details of classes, enrollment and dates.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliclassesf-17347.html#wlfliclassesf-17347](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliclassesf-17347.html#wlfliclassesf-17347)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_CLASSES_F_PK | CLASS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASS_ID | NUMBER |  | 18 | Yes | CLASS_ID |
| COORDINATOR_ID | NUMBER |  | 18 |  | COORDINATOR |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEMS_ID |
| COURSE_LEARNING_ITEM_ID | NUMBER |  | 18 |  | COURSE_LEARNING_ITEM_ID |
| ENROLMENT_END_DATE | DATE |  |  |  | ENROLMENT_END_DATE |
| ENROLMENT_START_DATE | DATE |  |  |  | ENROLMENT_START_DATE |
| USER_STATUS | VARCHAR2 | 80 |  |  | USER_STATUS |
| MAXIMUM_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_ATTENDEES |
| SUPPLIER_ID | NUMBER |  | 18 |  | SUPPLIER_ID |
| FACILITATOR_TYPE | VARCHAR2 | 30 |  |  | FACILITATOR_TYPE |
| MAXIMUM_INTERNAL_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_INTERNAL_ATTENDEES |
| MINIMUM_ATTENDEES | NUMBER |  | 9 |  | MINIMUM_ATTENDEES |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| TIMEZONE | VARCHAR2 | 30 |  |  | TIMEZONE |
| DELIVERY_MODE | VARCHAR2 | 30 |  |  | DELIVERY_MODE |
| RELATED_CONTENT_ID | NUMBER |  | 18 |  | RELATED_CONTENT_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CLS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER1 |
| CLS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER2 |
| CLS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER3 |
| CLS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER4 |
| CLS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER5 |
| CLS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER6 |
| CLS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER7 |
| CLS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER8 |
| CLS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER9 |
| CLS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER10 |
| CLS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER11 |
| CLS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER12 |
| CLS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER13 |
| CLS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER14 |
| CLS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER15 |
| CLS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER16 |
| CLS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER17 |
| CLS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER18 |
| CLS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER19 |
| CLS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER20 |
| CLS_ATTRIBUTE_DATE1 | DATE |  |  |  | CLS_ATTRIBUTE_DATE1 |
| CLS_ATTRIBUTE_DATE2 | DATE |  |  |  | CLS_ATTRIBUTE_DATE2 |
| CLS_ATTRIBUTE_DATE3 | DATE |  |  |  | CLS_ATTRIBUTE_DATE3 |
| CLS_ATTRIBUTE_DATE4 | DATE |  |  |  | CLS_ATTRIBUTE_DATE4 |
| CLS_ATTRIBUTE_DATE5 | DATE |  |  |  | CLS_ATTRIBUTE_DATE5 |
| CLS_ATTRIBUTE_DATE6 | DATE |  |  |  | CLS_ATTRIBUTE_DATE6 |
| CLS_ATTRIBUTE_DATE7 | DATE |  |  |  | CLS_ATTRIBUTE_DATE7 |
| CLS_ATTRIBUTE_DATE8 | DATE |  |  |  | CLS_ATTRIBUTE_DATE8 |
| CLS_ATTRIBUTE_DATE9 | DATE |  |  |  | CLS_ATTRIBUTE_DATE9 |
| CLS_ATTRIBUTE_DATE10 | DATE |  |  |  | CLS_ATTRIBUTE_DATE10 |
| CLS_ATTRIBUTE_DATE11 | DATE |  |  |  | CLS_ATTRIBUTE_DATE11 |
| CLS_ATTRIBUTE_DATE12 | DATE |  |  |  | CLS_ATTRIBUTE_DATE12 |
| CLS_ATTRIBUTE_DATE13 | DATE |  |  |  | CLS_ATTRIBUTE_DATE13 |
| CLS_ATTRIBUTE_DATE14 | DATE |  |  |  | CLS_ATTRIBUTE_DATE14 |
| CLS_ATTRIBUTE_DATE15 | DATE |  |  |  | CLS_ATTRIBUTE_DATE15 |
| SELF_COMPLETE_FLAG | VARCHAR2 | 1 |  |  | Indicate whether learner is allowed to mark himself completed to the class |
| ENABLE_CAPACITY | VARCHAR2 | 1 |  |  | Enable capacity for learning item |
| ENABLE_WAITLIST | VARCHAR2 | 1 |  |  | Enable waitlist mode for learning assignments |
| WAITLIST_MGMT_MODE | VARCHAR2 | 64 |  |  | Mode for managing waitlisted assignments |
| SEAT_EXPIRATION_DAYS | NUMBER |  | 9 |  | Offered seat expiration days |
| WAITLIST_EXPIRE_DAYS | NUMBER |  | 9 |  | Number of days for waitlist assignment to expire |
| EXPIRE_WAITLIST | VARCHAR2 | 1 |  |  | Flag to determine if waitlist assignments can be expired |
| REMAINING_SEATS | NUMBER |  | 18 |  | REMAINING_SEATS |
| PRIMARY_INSTRUCTOR_ID | NUMBER |  | 18 |  | This column represents primary instructor for an
offering |
| PRIMARY_CLASSROOM_ID | NUMBER |  | 18 |  | This column represents primary classroom for an
offering |
| PRIMARY_CLASSROOM_TYPE | VARCHAR2 | 30 |  |  | This column represents primary class room type |
| IS_FORUM_DEFAULT_OVERRIDDEN | VARCHAR2 | 30 |  |  | Determines whether or not the system default values for forum/conversations are overriden at learning item level |
| AUTO_COMPLETION_RULE_ENABLED | VARCHAR2 | 1 |  |  | Flag to indicate if Automated completion based on % of total duration is enabled for VILT activities. |
| AUTO_COMPLETION_RULE_VALUE | NUMBER |  | 3 |  | The minimum attendance duration required by learner to automatically trigger VILT activity completion. This is a percentage value between 1-100 if enabled. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_CLASSES_F_N1 | Non Unique | Default | RELATED_CONTENT_ID |
| WLF_LI_CLASSES_F_N2 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_CLASSES_F_N3 | Non Unique | Default | COURSE_LEARNING_ITEM_ID |
| WLF_LI_CLASSES_F_N4 | Non Unique | Default | DELIVERY_MODE |
| WLF_LI_CLASSES_F_N5 | Non Unique | Default | ENABLE_CAPACITY |
| WLF_LI_CLASSES_F_U1 | Unique | Default | CLASS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
