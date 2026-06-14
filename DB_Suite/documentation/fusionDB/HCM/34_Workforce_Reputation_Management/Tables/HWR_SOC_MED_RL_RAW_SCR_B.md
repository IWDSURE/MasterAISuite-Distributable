# HWR_SOC_MED_RL_RAW_SCR_B

This table stores the raw score for the roles of the profiles in socila media

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedrlrawscrb-31503.html#hwrsocmedrlrawscrb-31503](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedrlrawscrb-31503.html#hwrsocmedrlrawscrb-31503)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SOC_MED_RL_RAW_SCR_B_PK | GBL_PRFL_ID, ROLE_ID_URI, SCORE_TIMESTAMP |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | This stores the Global Profile Id of the consumer. |
| ROLE_ID_URI | VARCHAR2 | 1000 |  | Yes | This stores the Role Id of the consumer |
| ACCURACY | NUMBER |  |  |  | This stores the information about the Accuracy of the Score |
| IMPORTANCE | NUMBER |  |  |  | This stores the information on the importance of the Raw Score |
| PRECISION | NUMBER |  |  |  | This stores the information on the precision of the score |
| RELEVANCE | NUMBER |  |  |  | This stores the relevance of the score. |
| SCORE_TIMESTAMP | TIMESTAMP |  |  | Yes | This stores information about the timestamp when the score is created |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SOC_MED_RL_RAW_SCR_B_U1 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID, ROLE_ID_URI, SCORE_TIMESTAMP |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
