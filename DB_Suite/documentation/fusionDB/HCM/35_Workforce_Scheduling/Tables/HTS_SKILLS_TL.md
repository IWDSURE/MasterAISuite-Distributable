# HTS_SKILLS_TL

Skills translatable name and description.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsskillstl-19517.html#htsskillstl-19517](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsskillstl-19517.html#htsskillstl-19517)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SKILLS_TL_PK | SCHED_SKILL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_SKILL_ID | NUMBER |  | 18 | Yes | System generated identifier to uniquely identify a skill. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SKILL_NAME | VARCHAR2 | 240 |  |  | Name used to help identify the skill. |
| SKILL_DESCRIPTION | VARCHAR2 | 2000 |  |  | Description used to help identify a Skill. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SKILLS_TL_U1 | Unique | Default | SCHED_SKILL_ID, LANGUAGE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
