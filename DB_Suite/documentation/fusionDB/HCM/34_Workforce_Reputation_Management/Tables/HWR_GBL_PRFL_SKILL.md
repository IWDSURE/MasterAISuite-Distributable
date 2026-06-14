# HWR_GBL_PRFL_SKILL

Table storing information on skill assosiated to a global profile. Score, percentile rank, accepted/rejected and relevance.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflskill-20385.html#hwrgblprflskill-20385](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblprflskill-20385.html#hwrgblprflskill-20385)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_GBL_PRFL_SKILL_PK | GBL_PRFL_SKILL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GBL_PRFL_SKILL_ID | NUMBER |  | 18 | Yes | This is the primary key for the global profile topic table |
| GBL_PRFL_ID | NUMBER |  | 18 |  | This is a a foreign key to global profile tables. |
| FUS_PRFL_ID | NUMBER |  | 18 |  | This is the fusion profile ID of the employee. |
| TOPIC_ID | NUMBER |  | 18 | Yes | The topic Id. This is a foreign key from the topic tables. |
| STATUS | NUMBER |  | 2 |  | Indicate if a change was made to a statement related to the global profile skill |
| RAW_SCORE | NUMBER |  |  |  | Raw score of the global profile skill calculated using the related statment |
| PERCENTILE | NUMBER |  | 3 |  | Percentile rank of the user skill compared with other global profile |
| RELEVANCE_VALUE | NUMBER |  |  |  | Relevance score for the skill for the global profile |
| IS_REJECTED | NUMBER |  | 2 | Yes | Specify if the skill exist or is discovered 0 = Discovered, 2 = Existing |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_GBL_PRFL_SKILL_N1 | Non Unique | Default | TOPIC_ID, RAW_SCORE |
| HWR_GBL_PRFL_SKILL_N2 | Non Unique | Default | GBL_PRFL_ID |
| HWR_GBL_PRFL_SKILL_N3 | Non Unique | Default | STATUS, GBL_PRFL_SKILL_ID |
| HWR_GBL_PRFL_SKILL_N4 | Non Unique | FUSION_TS_TX_DATA | FUS_PRFL_ID |
| HWR_GBL_PRFL_SKILL_U1 | Unique | Default | GBL_PRFL_SKILL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
