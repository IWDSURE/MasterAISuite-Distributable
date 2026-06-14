# HRT_RATING_LEVELS_B

Rating Level table holds a single point on a rating scale and is used to rate competences.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratinglevelsb-5431.html#hrtratinglevelsb-5431](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratinglevelsb-5431.html#hrtratinglevelsb-5431)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_RATING_LEVELS_B_PK | RATING_LEVEL_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| RATING_LEVEL_ID | NUMBER |  | 18 | Yes | Unique identifier of Rating Level |  |
| STAR_RATING | NUMBER |  | 5 |  | Star Rating Value for the rating level |  |
| MIN_RATING_DISTRIBUTION | NUMBER |  | 5 |  | Minimum distribution as a percentage |  |
| MAX_RATING_DISTRIBUTION | NUMBER |  | 5 |  | Maximum distribution as a percentage |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| RATING_MODEL_ID | NUMBER |  | 18 | Yes | Foreign key to Rating Model table |  |
| RATING_LEVEL_CODE | VARCHAR2 | 30 |  | Yes | Rating Level code |  |
| DATE_FROM | DATE |  |  | Yes | Start date where the Rating Level is valid |  |
| DATE_TO | DATE |  |  |  | End date where the Rating Level is no longer valid |  |
| CAREER_STR_DEV | VARCHAR2 | 30 |  |  | Career Strength and Development |  |
| REVIEW_POINTS | NUMBER |  | 5 |  | Review Points |  |
| NUMERIC_RATING | NUMBER |  | 5 |  | Numeric Rating |  |
| FROM_POINTS | NUMBER |  | 5 |  | From Point rating |  |
| TO_POINTS | NUMBER |  | 5 |  | To Point rating |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rating Levels (HRT_RATING_LEVELS_B) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_RATING_LEVELS_B_N1 | Non Unique | Default | RATING_MODEL_ID, STAR_RATING |
| HRT_RATING_LEVELS_B_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| HRT_RATING_LEVELS_B_PK | Unique | Default | RATING_LEVEL_ID, BUSINESS_GROUP_ID |
| HRT_RATING_LEVELS_B_U1 | Unique | Default | RATING_MODEL_ID, BUSINESS_GROUP_ID, RATING_LEVEL_CODE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
