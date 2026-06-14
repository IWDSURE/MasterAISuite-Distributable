# WLF_ROLE_ALIGNMENT_DN

This is a denormalized table. It stores all the information related to capability guide skills assigned to a person.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrolealignmentdn-20723.html#wlfrolealignmentdn-20723](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrolealignmentdn-20723.html#wlfrolealignmentdn-20723)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ROLE_ALIGNMENT_DN_PK | ROLE_ALIGNMENT_DN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_ALIGNMENT_DN_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SKILL | VARCHAR2 | 240 |  |  | Name of the assigned capability guide skill. |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ALL_PEOPLE_F. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID of the skill assignee and Foreign Key to PER_MANAGER_HRCHY_CF. |
| PROFILE_ID | NUMBER |  | 18 | Yes | PROFILE_ID of the assigned skill. |
| ACHIEVED_FLAG | VARCHAR2 | 1 |  |  | To identified  whether assigned skill is achieved by person or not. |
| REQUIRED_LEVEL | NUMBER |  | 18 |  | The required level set by assigner. |
| ACHIEVED_LEVEL | NUMBER |  | 18 |  | Level that person has achieved for assigned skill. |
| ASSIGNED_BY | NUMBER |  | 18 |  | ID of the person who assigned the skill. |
| ASSIGNED_DATE | TIMESTAMP |  |  | Yes | Date on which skill is assigned. |
| ROLE_GUIDE_ID | NUMBER |  | 18 | Yes | Identifier of Role Guide and Foreign Key to WLF_GRW_GUIDES_F. |
| CAPABILITY_GUIDE_ID | NUMBER |  | 18 | Yes | Identifier of Capability Guide and Foreign Key to WLF_GRW_GUIDES_F. |
| PERSON_NAME_GLOBAL_DISP_NAME | VARCHAR2 | 240 |  |  | Global - Derived denormalized name formatted for on-screen display. Formatting depends on the Legislation Code, expect First Name as first component in this format. |
| PERSON_NAME_GLOBAL_LIST_NAME | VARCHAR2 | 240 |  |  | Global - Constructed version of a person's name, intended for use in an alphabetically-ordered list. The value may naturally differ depending on the  Legislation Code.Expect the Last Name as the first component in this format in most cases. |
| PERSON_NAME_LOCAL_DISP_NAME | VARCHAR2 | 240 |  |  | Local - Derived denormalized name formatted for on-screen display. Formatting depends on the Legislation Code, expect First Name as first component in this format. |
| PERSON_NAME_LOCAL_LIST_NAME | VARCHAR2 | 240 |  |  | Local - Constructed version of a person's name, intended for use in an alphabetically-ordered list. The value may naturally differ depending on the  Legislation Code.Expect the Last Name as the first component in this format in most cases. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ROLE_ALIGNMENT_DN_U1 | Unique | WLF_ROLE_ALIGNMENT_DN_U1 | ROLE_ALIGNMENT_DN_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
