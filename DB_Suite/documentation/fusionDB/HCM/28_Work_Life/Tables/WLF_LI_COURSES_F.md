# WLF_LI_COURSES_F

A course is the highest level of learning that can be prescribed to a learner.It also contains the objectives and competencies a learner will achieve by completing any class that belongs underneath. It is an object in the catalog, and resid

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicoursesf-7337.html#wlflicoursesf-7337](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicoursesf-7337.html#wlflicoursesf-7337)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_COURSES_F_PK | COURSE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COURSE_ID | NUMBER |  | 18 | Yes | COURSE_ID |
| DFLT_FACILITATOR_TYPE | VARCHAR2 | 30 |  |  | DFLT_FACILITATOR_TYPE |
| DFLT_FACILITATOR_ID | NUMBER |  | 18 |  | DFLT_FACILITATOR_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| COURSE_TYPE | VARCHAR2 | 30 |  |  | Course Type |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |
| EXPENSES_ALLOWED | VARCHAR2 | 30 |  |  | EXPENSES_ALLOWED |
| INTENDED_AUDIENCE | VARCHAR2 | 4000 |  |  | INTENDED_AUDIENCE |
| MAXIMUM_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_ATTENDEES |
| MAXIMUM_INTERNAL_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_INTERNAL_ATTENDEES |
| MINIMUM_ATTENDEES | NUMBER |  | 9 |  | MINIMUM_ATTENDEES |
| PROFESSIONAL_CREDIT_TYPE | VARCHAR2 | 30 |  |  | PROFESSIONAL_CREDIT_TYPE |
| PROFESSIONAL_CREDITS | NUMBER |  |  |  | PROFESSIONAL_CREDITS |
| SUCCESS_CRITERIA | VARCHAR2 | 30 |  |  | SUCCESS_CRITERIA |
| USER_STATUS | VARCHAR2 | 30 |  |  | USER_STATUS |
| INVENTORY_ITEM_ID | NUMBER |  | 18 |  | INVENTORY_ITEM_ID |
| EFFORT | VARCHAR2 | 30 |  |  | EFFORT |
| EFFORT_UOM | VARCHAR2 | 30 |  |  | EFFORT_UOM |
| INV_ORGANIZATION_ID | NUMBER |  | 18 |  | INV_ORGANIZATION_ID |
| MINIMUM_TRAINING_HOURS | NUMBER |  | 9 |  | MINIMUM_TRAINING_HOURS |
| MAXIMUM_TRAINING_HOURS | NUMBER |  | 9 |  | MAXIMUM_TRAINING_HOURS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CRS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CRS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER1 |
| CRS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER2 |
| CRS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER3 |
| CRS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER4 |
| CRS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER5 |
| CRS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER6 |
| CRS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER7 |
| CRS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER8 |
| CRS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER9 |
| CRS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER10 |
| CRS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER11 |
| CRS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER12 |
| CRS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER13 |
| CRS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER14 |
| CRS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER15 |
| CRS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER16 |
| CRS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER17 |
| CRS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER18 |
| CRS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER19 |
| CRS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | CRS_ATTRIBUTE_NUMBER20 |
| CRS_ATTRIBUTE_DATE1 | DATE |  |  |  | CRS_ATTRIBUTE_DATE1 |
| CRS_ATTRIBUTE_DATE2 | DATE |  |  |  | CRS_ATTRIBUTE_DATE2 |
| CRS_ATTRIBUTE_DATE3 | DATE |  |  |  | CRS_ATTRIBUTE_DATE3 |
| CRS_ATTRIBUTE_DATE4 | DATE |  |  |  | CRS_ATTRIBUTE_DATE4 |
| CRS_ATTRIBUTE_DATE5 | DATE |  |  |  | CRS_ATTRIBUTE_DATE5 |
| CRS_ATTRIBUTE_DATE6 | DATE |  |  |  | CRS_ATTRIBUTE_DATE6 |
| CRS_ATTRIBUTE_DATE7 | DATE |  |  |  | CRS_ATTRIBUTE_DATE7 |
| CRS_ATTRIBUTE_DATE8 | DATE |  |  |  | CRS_ATTRIBUTE_DATE8 |
| CRS_ATTRIBUTE_DATE9 | DATE |  |  |  | CRS_ATTRIBUTE_DATE9 |
| CRS_ATTRIBUTE_DATE10 | DATE |  |  |  | CRS_ATTRIBUTE_DATE10 |
| CRS_ATTRIBUTE_DATE11 | DATE |  |  |  | CRS_ATTRIBUTE_DATE11 |
| CRS_ATTRIBUTE_DATE12 | DATE |  |  |  | CRS_ATTRIBUTE_DATE12 |
| CRS_ATTRIBUTE_DATE13 | DATE |  |  |  | CRS_ATTRIBUTE_DATE13 |
| CRS_ATTRIBUTE_DATE14 | DATE |  |  |  | CRS_ATTRIBUTE_DATE14 |
| CRS_ATTRIBUTE_DATE15 | DATE |  |  |  | CRS_ATTRIBUTE_DATE15 |
| DFLT_OFFERING_PRC_RULE_ID | NUMBER |  | 18 |  | Identifier of default pricing rule for offering. Foreign key to WLF_PRICING_RULES_F. |
| DFLT_ILT_PRC_RULE_ID | NUMBER |  | 18 |  | Identifier of default pricing rule for instructor lead offering. Foreign key to WLF_PRICING_RULES_F. |
| DFLT_SP_PRC_RULE_ID | NUMBER |  | 18 |  | Identifier of default pricing rule for self paced offering. Foreign key to WLF_PRICING_RULES_F. |
| DFLT_BLENDED_PRC_RULE_ID | NUMBER |  | 18 |  | Identifier of default pricing rule for blended offering. Foreign key to WLF_PRICING_RULES_F. |
| ENABLE_CAPACITY | VARCHAR2 | 1 |  |  | Enable capacity for learning item |
| ENABLE_WAITLIST | VARCHAR2 | 1 |  |  | Enable waitlist mode for learning assignments |
| WAITLIST_MGMT_MODE | VARCHAR2 | 64 |  |  | Mode for managing waitlisted assignments |
| SEAT_EXPIRATION_DAYS | NUMBER |  | 9 |  | Offered seat expiration days |
| WAITLIST_EXPIRE_DAYS | NUMBER |  | 9 |  | Number of days for waitlist assignment to expire |
| EXPIRE_WAITLIST | VARCHAR2 | 1 |  |  | Flag to determine if waitlist assignments can be expired |
| PAYMENT_RULE_ID | NUMBER |  | 18 |  | Identifier of Payment Type Rule. Foreign key to WLF_PAYMENT_RULES_F table. |
| IS_FORUM_DEFAULT_OVERRIDDEN | VARCHAR2 | 30 |  |  | Determines whether or not system default values for forum/conversations are overriden at learning item level |
| WAITLIST_RULE | VARCHAR2 | 30 |  |  | Waitlisting rule on who can add learners to waitlist |
| WAITLIST_MAXIMUM_ENABLED | VARCHAR2 | 30 |  |  | Property to represent if waitlist maximum capacity is enabled |
| WAITLIST_MAXIMUM | NUMBER |  | 18 |  | Property to represent Maximum waitlist setting |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_COURSES_F_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_COURSES_F_U1 | Unique | Default | COURSE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
