# HRT_PERF_RATING_ITEMS_V_

This table contains profile items that make up a Profile. The items can be of any Content Type (Competencies, Objectives, etc.)

It contains all the Developer Descriptive Flex (DDFF) attributes where all the developer defined flex related information is stored and also contains all the Descriptive Flex (DFF) attributes where all the customer defined flex related information is stored.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtperfratingitemsv-25910.html#hrtperfratingitemsv-25910](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtperfratingitemsv-25910.html#hrtperfratingitemsv-25910)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PERF_RATING_ITEMS_V_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERF_RATING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERF_RATING_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to HRT_PROFILES_B |
| PARENT_PROFILE_ITEM_ID | NUMBER |  | 18 |  | Parent Profile Item Id |
| SECTION_ID | NUMBER |  | 18 |  | Foreign Key to HRT_PROFILE_TYP_SECTIONS |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_TYPES_B |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| PERF_RATING_LEVEL_ID | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |
| NUMERIC_RATING | NUMBER |  | 15 |  | A generic decimal field |
| SECTION_CONTENT_TYPE | NUMBER |  | 18 |  | A generic number field |
| COMMENTS | CLOB |  |  |  | A generic CLOB field |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | A generic number field |
| DATE_FROM | DATE |  |  |  | Date From |
| DATE_TO | DATE |  |  |  | Date To |
| QUALIFIER_ID1 | NUMBER |  | 18 |  | The instance qualifier to use for the item |
| PERF_RATING_MODEL_ID | NUMBER |  | 18 |  | The rating model |
| SOURCE_ID | NUMBER |  | 18 |  | Syndication source profile ID. Use this property to display the source profile of a syndicated item |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source Type. For example, IRC, OTA |
| SOURCE_KEY1 | NUMBER |  | 18 |  | Alternative Source Key |
| SOURCE_KEY2 | NUMBER |  | 18 |  | Alternative Source Key |
| SOURCE_KEY3 | NUMBER |  | 18 |  | Alternative Source Key |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
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
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PERF_RATING_ITEMS_VN1_ | Non Unique | Default | PERF_RATING_ID, LAST_UPDATE_DATE |
| HRT_PERF_RATING_ITEMS_V_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERF_RATING_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
