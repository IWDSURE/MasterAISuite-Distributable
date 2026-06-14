# HWR_SOC_MED_ROLE_SCORE_B

This table stores the information related Social Media Role Score.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedrolescoreb-5725.html#hwrsocmedrolescoreb-5725](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedrolescoreb-5725.html#hwrsocmedrolescoreb-5725)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SOC_MED_ROLE_SCORE_B_PK | FUS_PRFL_ID#01, ROLE_ID_URI, SCORE_TIMESTAMP |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GBL_PRFL_ID | NUMBER |  | 18 |  | This stores the Golbal Profile Id. |  |
| FUS_PRFL_ID | NUMBER |  | 18 |  | This stores the Fusion Profile Id. | Obsolete |
| FUS_PRFL_ID#01 | NUMBER |  | 18 | Yes | This stores the Fusion Profile Id. |  |
| ROLE_ID_URI | VARCHAR2 | 1000 |  | Yes | This stores the URI of the Role |  |
| ACCURACY | NUMBER |  |  |  | This stores information about accuracy |  |
| IMPORTANCE | NUMBER |  |  |  | This stores the information about the Importance of the score |  |
| PRECISION | NUMBER |  |  |  | This stores the information about the precision of the score |  |
| RELEVANCE | NUMBER |  |  |  | This stores the relevance information |  |
| SCORE_TIMESTAMP | TIMESTAMP |  |  | Yes | This stores the time of creation of the score |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_SOC_MED_ROLE_SCORE_B_N1 | Non Unique | FUSION_TS_TX_DATA | FUS_PRFL_ID#01, ROLE_ID_URI, SCORE_TIMESTAMP | Obsolete |
| HWR_SOC_MED_ROLE_SCORE_B_U1 | Unique | FUSION_TS_TX_DATA | FUS_PRFL_ID#01, ROLE_ID_URI, SCORE_TIMESTAMP |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
