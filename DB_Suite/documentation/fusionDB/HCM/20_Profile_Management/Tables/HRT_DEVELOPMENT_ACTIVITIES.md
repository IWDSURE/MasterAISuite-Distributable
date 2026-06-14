# HRT_DEVELOPMENT_ACTIVITIES

This table stores skill development activities information.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtdevelopmentactivities-19826.html#hrtdevelopmentactivities-19826](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtdevelopmentactivities-19826.html#hrtdevelopmentactivities-19826)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_DEVELOPMENT_ACTIVITIES_PK | DEVELOPMENT_ACTIVITY_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEVELOPMENT_ACTIVITY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_PROFILES_B table. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Stores the primary key of the object involved in the development activity. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Stores the object type involved in the development activity. Lookup type - ORA_HRT_DEV_ACTIVITY_OBJECT_TYPE |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B table |
| SKILL | VARCHAR2 | 240 |  |  | This column stores the name of the skill |
| SKILL_ID | NUMBER |  | 18 |  | Foreign key to HRT_PROFILE_ITEMS table. |
| STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of development activity. Lookup type - ORA_HRT_DEVELOPMENT_ACTIVITY |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Stores the rating level associated to development activity |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Stores the rating model used in the development activity rating. |
| COMPLETION_DATE | TIMESTAMP |  |  | Yes | Stores the date on which development activity is completed |
| SKILL_SCORE_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_SKILLS_SCORE_CONFIG table. |
| CUSTOM_SCORE | NUMBER |  | 18 |  | Stores custom score value if any development activity overrides the default score from score configuration. |
| EXPIRY_DATE | DATE |  |  |  | Stores expiry date |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_DEVELOPMENT_ACTIVITIES_N1 | Non Unique | Default | PROFILE_ID, OBJECT_TYPE, UPPER("SKILL") |
| HRT_DEVELOPMENT_ACTIVITIES_U1 | Unique | Default | DEVELOPMENT_ACTIVITY_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
