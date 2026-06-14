# HRT_SKILLS_CRITERIA

This table stores skill criteria information.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillscriteria-25655.html#hrtskillscriteria-25655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillscriteria-25655.html#hrtskillscriteria-25655)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_CRITERIA_PK | SKILL_CRITERIA_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_CRITERIA_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_CRITERIA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the skill criteria type as lookup code. The corresponding lookup type is ORA_HRT_SKILL_CRITERIA_TYPES |
| OBJECT_ID | NUMBER |  | 18 | Yes | Business Object ID - It can be Person ID / Job ID / Job Profile ID |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B table |
| SKILL | VARCHAR2 | 240 |  |  | Name of the assigned role/core skill. |
| ASSIGNED_DATE | TIMESTAMP |  |  | Yes | Date on which skill is assigned. |
| ASSIGNED_BY | NUMBER |  | 18 |  | ID of the person who assigned the skill. |
| MANAGER_LEVEL | NUMBER |  | 18 |  | Level of the manager who assigned the skill. |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Rating model of the assigned skill set by assignor. |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Rating level of the assigned skill set by assignor. |
| STATUS | VARCHAR2 | 30 |  |  | Indicates the status of the skill criteria. |
| SKILL_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to HRT_SKILLS_ASSIGNMENTS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_CRITERIA_N1 | Non Unique | Default | SKILL_CRITERIA_TYPE_CODE, OBJECT_ID |
| HRT_SKILLS_CRITERIA_PK | Unique | Default | SKILL_CRITERIA_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
