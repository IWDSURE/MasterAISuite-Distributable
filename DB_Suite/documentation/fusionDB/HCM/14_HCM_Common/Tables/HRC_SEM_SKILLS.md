# HRC_SEM_SKILLS

This table contains the seeded skills to be used in the application.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemskills-4434.html#hrcsemskills-4434](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemskills-4434.html#hrcsemskills-4434)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_SKILLS_PK | SKILL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_ID | NUMBER |  | 18 | Yes | This is the primary key of the skill table. |
| PERSON_ID | NUMBER |  | 18 |  | This column contains the person id referenced to the person table. |
| NAME | VARCHAR2 | 512 |  |  | This is the name of a particular skill. |
| CATEGORY | VARCHAR2 | 512 |  |  | This is the category of a particular skill. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_SKILLS_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID |
| HRC_SEM_SKILLS_N2 | Non Unique | FUSION_TS_TX_DATA | NAME |
| HRC_SEM_SKILLS_N3 | Non Unique | FUSION_TS_TX_DATA | CATEGORY |
| HRC_SEM_SKILLS_U1 | Unique | FUSION_TS_TX_DATA | SKILL_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
