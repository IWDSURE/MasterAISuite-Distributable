# HWR_ENDORSEMENT_B

The endorsement table stores global profile endorsement data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrendorsementb-5707.html#hwrendorsementb-5707](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrendorsementb-5707.html#hwrendorsementb-5707)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ENDORSEMENT_B_PK | ENDORSEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENDORSEMENT_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the endorsement table. |
| ENDORSEMENT_TEXT | CLOB |  |  |  | This is the full text of the endorsement. |
| ENDORSEMENT_DATE | TIMESTAMP |  |  |  | This is the date of the endorsement. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This column contains endorsement description |
| TOPIC_ID | NUMBER |  | 18 |  | This is the topic id of the endorsement. |
| RECOMMENDER_ID | VARCHAR2 | 500 |  |  | This is the unique Id of the recommender. |
| RECOMMENDER_GBL_PRFL_ID | NUMBER |  | 18 |  | This is the global profile ID of the recommender. |
| RECOMMENDER_FUS_PRFL_ID | NUMBER |  | 18 |  | This is the fusion profile ID of the recommender. |
| ENDORSEE_FUS_PRFL_ID | NUMBER |  | 18 |  | This is the fusion profile ID of the endorsee. |
| RECOMMENDER_NAME | VARCHAR2 | 255 |  |  | This is the name of the recommender. |
| RECOMMENDER_TITLE | VARCHAR2 | 255 |  |  | This is the title of the recommender. |
| RECOMMENDER_EMAIL | VARCHAR2 | 1000 |  |  | This is the list of email addresses of the recommender. |
| RECOMMENDER_RELATION | VARCHAR2 | 255 |  |  | This is the relation type of the recommender. |
| RECOMMENDER_IMAGE_URL | VARCHAR2 | 1000 |  |  | This is the image URL of the recommender. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ENDORSEMENT_B_N1 | Non Unique | FUSION_TS_TX_DATA | RECOMMENDER_FUS_PRFL_ID |
| HWR_ENDORSEMENT_B_N2 | Non Unique | FUSION_TS_TX_DATA | ENDORSEE_FUS_PRFL_ID |
| HWR_ENDORSEMENT_B_U1 | Unique | FUSION_TS_TX_DATA | ENDORSEMENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
