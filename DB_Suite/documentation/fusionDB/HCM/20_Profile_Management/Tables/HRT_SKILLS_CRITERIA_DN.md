# HRT_SKILLS_CRITERIA_DN

This is a denormalized table.It stores all the information related to core and role skills assigned to a person.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillscriteriadn-22352.html#hrtskillscriteriadn-22352](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillscriteriadn-22352.html#hrtskillscriteriadn-22352)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_CRITERIA_DN_PK | SKILL_CRITERIA_DN_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_CRITERIA_DN_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_CRITERIA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the skill criteria type as lookup code. The corresponding lookup type is ORA_HRT_SKILL_CRITERIA_TYPES |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B table |
| SKILL | VARCHAR2 | 240 |  |  | Name of the assigned role/core skill. |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID of the assigned skill. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID of the skill assignee. |
| PROFILE_ID | NUMBER |  | 18 | Yes | PROFILE_ID of the assigned skill. |
| ASSIGNED_DATE | TIMESTAMP |  |  | Yes | Date on which skill is assigned. |
| ASSIGNED_BY | NUMBER |  | 18 |  | ID of the person who assigned the skill. |
| DEVELOPED_FLAG | VARCHAR2 | 1 |  |  | Identifies whether assigned skill is developed by person or not. |
| ACHIEVED_FLAG | VARCHAR2 | 1 |  |  | To identified  whether assigned skill is achieved by person or not . |
| CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | Identifies whether assigned skill is confirmed or not . |
| JOB_ID | NUMBER |  | 18 |  | Holds JobID that is foreign key to PER_JOBS_F |
| JOB_CODE | VARCHAR2 | 30 |  |  | JOB_CODE for ROLE type assigned skill. |
| JOB_NAME | VARCHAR2 | 240 |  |  | This column denotes name for the Job. |
| REQUIRED_LEVEL | NUMBER |  | 18 |  | The required level set by assignor. |
| ACHIEVED_LEVEL | NUMBER |  | 18 |  | Level that person has achieved for assigned skill. |
| ASSIGNMENT_NAME | VARCHAR2 | 320 |  |  | Assignment Name of the skill assignee person. |
| ENDORSEMENT_COUNT | NUMBER |  | 18 |  | Total count of the endorsement that person has for assigned skil. |
| PERSON_NAME_GLOBAL_LEG_CODE | VARCHAR2 | 4 |  |  | Country context for the Global Name. |
| PERSON_NAME_GLOBAL_CHARSET_CTX | VARCHAR2 | 4 |  |  | Specifies the character set in which the details are stored. |
| PERSON_NAME_GLOBAL_DISP_NAME | VARCHAR2 | 960 |  |  | Skill assignee Person's Display Name |
| PERSON_NAME_GLOBAL_FULL_NAME | VARCHAR2 | 4000 |  |  | Skill assignee Person's Full Name |
| PERSON_NAME_GLOBAL_LIST_NAME | VARCHAR2 | 960 |  |  | Skill assignee Person's List Name |
| PERSON_NAME_LOCAL_LEG_CODE | VARCHAR2 | 4 |  |  | Country context for the Local Name. |
| PERSON_NAME_LOCAL_CHARSET_CTX | VARCHAR2 | 4 |  |  | Specifies the character set in which the details are stored for local name. |
| PERSON_NAME_LOCAL_DISP_NAME | VARCHAR2 | 960 |  |  | Skill assignee Person's Local Display Name |
| PERSON_NAME_LOCAL_FULL_NAME | VARCHAR2 | 4000 |  |  | Skill assignee Person's Local Full Name |
| PERSON_NAME_LOCAL_LIST_NAME | VARCHAR2 | 960 |  |  | Skill assignee Person's Local List Name |
| ASG_BY_GLOBAL_NAME_LEG_CODE | VARCHAR2 | 4 |  |  | Country context for the Assigned By Global Name. |
| ASG_BY_GLOBAL_NAME_CHARSET_CTX | VARCHAR2 | 4 |  |  | Specifies the character set in which the details are stored for Assigned By global name. |
| ASG_BY_GLOBAL_DISP_NAME | VARCHAR2 | 960 |  |  | Assigned By Person's Global Display Name |
| ASG_BY_LOCAL_NAME_LEG_CODE | VARCHAR2 | 4 |  |  | Country context for the Assigned By Local Name. |
| ASG_BY_LOCAL_NAME_CHARSET_CTX | VARCHAR2 | 4 |  |  | Specifies the character set in which the details are stored for Assigned By local name. |
| ASG_BY_LOCAL_DISP_NAME | VARCHAR2 | 960 |  |  | Assigned By Person's Local Display Name |
| POSITION_ID | NUMBER |  | 18 |  | Identifier for the HR_ALL_POSITIONS_F |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_CRITERIA_DN_PK | Unique | Default | SKILL_CRITERIA_DN_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
