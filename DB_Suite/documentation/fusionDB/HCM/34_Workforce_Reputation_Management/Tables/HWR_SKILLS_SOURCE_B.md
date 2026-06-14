# HWR_SKILLS_SOURCE_B

This table will be used to store the list of potential sources for the skills.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillssourceb-19652.html#hwrskillssourceb-19652](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillssourceb-19652.html#hwrskillssourceb-19652)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SKILLS_SOURCE_B_PK | SKILL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_ID | NUMBER |  | 18 | Yes | This is the Skill Source Id identifying the Skill Source entry in this table. |
| IS_ENABLED | NUMBER |  | 18 | Yes | This indicates whether the skill source was enabled or not. |
| SKILL_ATTR_1 | VARCHAR2 | 100 |  |  | SKILL_ATTR_1. This is the extra attribute in case if needed. |
| SKILL_ATTR_2 | VARCHAR2 | 100 |  |  | SKILL_ATTR_2. This is the extra attribute in case if needed. |
| SKILL_ATTR_3 | VARCHAR2 | 100 |  |  | SKILL_ATTR_3. This is the extra attribute in case if needed. |
| SKILL_ATTR_4 | VARCHAR2 | 100 |  |  | SKILL_ATTR_4. This is the extra attribute in case if needed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SKILLS_SOURCE_B_U1 | Unique | Default | SKILL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
