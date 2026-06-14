# HWR_XP_SKILLS_B

This table will be used to store discovered skills from the experience store.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpskillsb-29263.html#hwrxpskillsb-29263](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpskillsb-29263.html#hwrxpskillsb-29263)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_SKILLS_B_PK | USER_ID, SKILL_ID, VERB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 |  | Yes | This represents the Fusion id of the user for which this skill was found. |
| SKILL_ID | NUMBER |  | 18 | Yes | This is the unique identifier for the corresponding skill. |
| VERB_ID | NUMBER |  | 18 | Yes | This is the unique identifier for the corresponding verb. |
| SCORE | NUMBER |  | 3 |  | SCORE Normalized claculation of the relevance score of skill. |
| RAW_SCORE | NUMBER |  | 3 |  | RAW_SCORE Raw calculation of the relevance score of skill. |
| IS_SEEDED | VARCHAR2 | 20 |  | Yes | This indicates whether the skill was seeded or not seeded. |
| XP_SKILLS_ATTR_1 | VARCHAR2 | 100 |  |  | XP_SKILLS_ATTR_1. This is the extra attribute in case if needed. |
| XP_SKILLS_ATTR_2 | VARCHAR2 | 100 |  |  | XP_SKILLS_ATTR_2. This is the extra attribute in case if needed. |
| XP_SKILLS_ATTR_3 | VARCHAR2 | 100 |  |  | XP_SKILLS_ATTR_3. This is the extra attribute in case if needed. |
| XP_SKILLS_ATTR_4 | VARCHAR2 | 100 |  |  | XP_SKILLS_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_SKILLS_B_N1 | Non Unique | Default | SKILL_ID, SCORE, USER_ID |
| HWR_XP_SKILLS_B_N2 | Non Unique | Default | "RAW_SCORE", SKILL_ID, USER_ID |
| HWR_XP_SKILLS_B_U1 | Unique | Default | USER_ID, SKILL_ID, VERB_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
