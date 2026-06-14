# HRT_SKILLS_ASSIGNMENTS

This table stores skill assignments information.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsassignments-11763.html#hrtskillsassignments-11763](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsassignments-11763.html#hrtskillsassignments-11763)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_ASSIGNMENTS_PK | SKILL_ASSIGNMENT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the skill assignment. |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  | Yes | Indicates assignment type like ORA_ASSIGN or ORA_UNASSIGN. |
| ASSIGNED_BY | NUMBER |  | 18 | Yes | PERSON_ID of the manager who makes the skill assignment. |
| LOGIN_PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID of the user who creates skill assignment. |
| ASSIGNED_DATE | TIMESTAMP |  |  | Yes | Date on which skill assignment is created. |
| PROCESS_ID | NUMBER |  | 18 |  | Stores the ESS process Id in which the skill assignment is processed. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Date on which skill assignment is processed. |
| STATUS | VARCHAR2 | 30 |  |  | Indicates the skill assignment status. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_ASSIGNMENTS_PK | Unique | Default | SKILL_ASSIGNMENT_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
