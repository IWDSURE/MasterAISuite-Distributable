# HWR_RCMNDTN_B

The recommendation table stores recommendations for profiles.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrcmndtnb-30202.html#hwrrcmndtnb-30202](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrcmndtnb-30202.html#hwrrcmndtnb-30202)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RCMNDTN_B_PK | SOURCE_ID, RECOMMENDATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMENDATION_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the recommendation table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the profile which has the recommendation. |
| RECOMMENDATION_TEXT | CLOB |  |  |  | This is the full text of the recommendation. |
| RECOMMENDATION_TYPE | VARCHAR2 | 255 |  |  | This is the type of the recommendation. |
| RECOMMENDER_ID | VARCHAR2 | 500 |  |  | This is the unique Id of the recommender. |
| RECOMMENDER_URI | VARCHAR2 | 500 |  |  | This is the URI identifying the recommender. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_RCMNDTN_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, RECOMMENDATION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
