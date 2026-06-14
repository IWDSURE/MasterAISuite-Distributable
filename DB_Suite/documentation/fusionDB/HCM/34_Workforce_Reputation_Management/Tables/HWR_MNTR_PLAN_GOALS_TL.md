# HWR_MNTR_PLAN_GOALS_TL

The translation table for mentor plan goals table.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplangoalstl-8591.html#hwrmntrplangoalstl-8591](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplangoalstl-8591.html#hwrmntrplangoalstl-8591)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_MNTR_PLAN_GOALS_TL_PK | GOAL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GOAL_ID | NUMBER |  | 18 | Yes | This is the primary key of the table. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| GOAL_NAME | VARCHAR2 | 400 |  | Yes | This is the name of the goal for each Locale. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_MNTR_PLAN_GOALS_TL_U1 | Unique | FUSION_TS_TX_DATA | GOAL_ID, LANGUAGE | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
