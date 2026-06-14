# HRT_SKILLS_REQUIREMENTS

This table stores skill requirements details of the skill assignments.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsrequirements-28079.html#hrtskillsrequirements-28079](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsrequirements-28079.html#hrtskillsrequirements-28079)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_REQUIREMENTS_PK | SKILL_REQUIREMENT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_REQUIREMENT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_SKILLS_ASSIGNMENTS. |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B table |
| SKILL | VARCHAR2 | 240 |  |  | Name of the assigned core skill. |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Rating model id used for the skill assignment. |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Rating level id set during skill assignment. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_REQUIREMENTS_N1 | Non Unique | Default | SKILL_ASSIGNMENT_ID |
| HRT_SKILLS_REQUIREMENTS_PK | Unique | Default | SKILL_REQUIREMENT_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
