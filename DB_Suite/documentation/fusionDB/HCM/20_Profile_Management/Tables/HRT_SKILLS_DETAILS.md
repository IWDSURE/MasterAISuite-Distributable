# HRT_SKILLS_DETAILS

This table stores skill details information.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsdetails-19525.html#hrtskillsdetails-19525](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsdetails-19525.html#hrtskillsdetails-19525)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_DETAILS_PK | SKILL_DETAIL_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_DETAIL_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_CRITERIA_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_SKILLS_CRITERIA table. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID of the skill assignee. |
| SKILL_CRITERIA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the skill criteria type as lookup code. The corresponding lookup type is ORA_HRT_SKILL_CRITERIA_TYPES |
| SKILL_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_SKILL_ITEMS_V table. |
| ASSIGNED_DATE | TIMESTAMP |  |  | Yes | Date on which skill is assigned. |
| ASSIGNED_BY | NUMBER |  | 18 |  | ID of the person who assigned the skill. |
| MANAGER_LEVEL | NUMBER |  | 18 |  | Level of the manager who assigned the skill. |
| SKILL_STATUS | VARCHAR2 | 30 |  |  | Indicates the status of assigned skill. |
| REQUIRED_RATING_MODEL_ID | NUMBER |  | 18 |  | Required Rating model set by assignor. |
| REQUIRED_RATING_LEVEL_ID | NUMBER |  | 18 |  | Required rating level set by assignor. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_DETAILS_N1 | Non Unique | Default | SKILL_CRITERIA_ID, SKILL_ID |
| HRT_SKILLS_DETAILS_N2 | Non Unique | Default | SKILL_CRITERIA_ID, SKILL_CRITERIA_TYPE_CODE |
| HRT_SKILLS_DETAILS_PK | Unique | Default | SKILL_DETAIL_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
