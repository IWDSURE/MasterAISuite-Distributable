# HRT_SKILLS_ASSIGNEE

This table stores assignee details of the skill assignments.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsassignee-25383.html#hrtskillsassignee-25383](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsassignee-25383.html#hrtskillsassignee-25383)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_ASSIGNEE_PK | SKILL_ASSIGNEE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_ASSIGNEE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_SKILLS_ASSIGNMENTS. |
| SKILL_CRITERIA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the skill criteria type as lookup code. The corresponding lookup type is ORA_HRT_SKILL_CRITERIA_TYPES |
| JOB_ID | NUMBER |  | 18 |  | It stores JobId of ROLECORE skills assignment. |
| PERSON_ID | NUMBER |  | 18 |  | It stores personId of skill asignee for CORE skills assignment. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Id of the assignee in case of assignee type such as person, direct report or entire org. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_ASSIGNEE_N1 | Non Unique | Default | SKILL_ASSIGNMENT_ID |
| HRT_SKILLS_ASSIGNEE_PK | Unique | Default | SKILL_ASSIGNEE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
