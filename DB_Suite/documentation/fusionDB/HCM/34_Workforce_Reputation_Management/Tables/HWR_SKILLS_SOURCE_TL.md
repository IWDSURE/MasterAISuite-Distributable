# HWR_SKILLS_SOURCE_TL

This table will be used to store the list of potential sources for the skills - TL version of HWR_SKILLS_SOURCE_B.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillssourcetl-8328.html#hwrskillssourcetl-8328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillssourcetl-8328.html#hwrskillssourcetl-8328)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SKILLS_SOURCE_TL_PK | SKILL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_ID | NUMBER |  | 18 | Yes | This is the Skill Source Id identifying the Skill Source entry in this table |
| SKILL_NAME | VARCHAR2 | 100 |  | Yes | This is the name of the skill source in the specified language. |
| SKILL_DESCRIPTION | VARCHAR2 | 2000 |  |  | SKILL_DESCRIPTION |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SKILLS_SOURCE_TL_U1 | Unique | Default | SKILL_ID, LANGUAGE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
