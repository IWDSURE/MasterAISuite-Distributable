# WLF_LI_SPECIALIZATIONS_F

A specialization is the highest level of learning that can be prescribed to a learner.It is an object in the catalog.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflispecializationsf-27454.html#wlflispecializationsf-27454](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflispecializationsf-27454.html#wlflispecializationsf-27454)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_SPECIALIZATIONS_F_PK | SPECIALIZATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SPECIALIZATION_ID | NUMBER |  | 18 | Yes | SPECIALIZATION_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SPECL_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| SPECL_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SPECL_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER1 |
| SPECL_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER2 |
| SPECL_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER3 |
| SPECL_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER4 |
| SPECL_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER5 |
| SPECL_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER6 |
| SPECL_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER7 |
| SPECL_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER8 |
| SPECL_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER9 |
| SPECL_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER10 |
| SPECL_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER11 |
| SPECL_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER12 |
| SPECL_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER13 |
| SPECL_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER14 |
| SPECL_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER15 |
| SPECL_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER16 |
| SPECL_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER17 |
| SPECL_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER18 |
| SPECL_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER19 |
| SPECL_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | SPECL_ATTRIBUTE_NUMBER20 |
| SPECL_ATTRIBUTE_DATE1 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE1 |
| SPECL_ATTRIBUTE_DATE2 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE2 |
| SPECL_ATTRIBUTE_DATE3 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE3 |
| SPECL_ATTRIBUTE_DATE4 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE4 |
| SPECL_ATTRIBUTE_DATE5 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE5 |
| SPECL_ATTRIBUTE_DATE6 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE6 |
| SPECL_ATTRIBUTE_DATE7 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE7 |
| SPECL_ATTRIBUTE_DATE8 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE8 |
| SPECL_ATTRIBUTE_DATE9 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE9 |
| SPECL_ATTRIBUTE_DATE10 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE10 |
| SPECL_ATTRIBUTE_DATE11 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE11 |
| SPECL_ATTRIBUTE_DATE12 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE12 |
| SPECL_ATTRIBUTE_DATE13 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE13 |
| SPECL_ATTRIBUTE_DATE14 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE14 |
| SPECL_ATTRIBUTE_DATE15 | DATE |  |  |  | SPECL_ATTRIBUTE_DATE15 |
| MINIMUM_TRAINING_HOURS | NUMBER |  | 9 |  | MINIMUM_TRAINING_HOURS |
| MAXIMUM_TRAINING_HOURS | NUMBER |  | 9 |  | MAXIMUM_TRAINING_HOURS |
| IS_FORUM_DEFAULT_OVERRIDDEN | VARCHAR2 | 30 |  |  | Determines whether or not the system default values for forum/conversations are overriden at learning item level |
| SEQUENCE_ENABLED | VARCHAR2 | 1 |  |  | Column value represents whether specialization is sequence enabled or not |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_SPECIALIZATIONS_F_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_SPECIALIZATIONS_F_U1 | Unique | Default | SPECIALIZATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
