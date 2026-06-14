# HWR_RECOGNITION_B

The recognition table stores global profile recognition data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecognitionb-28786.html#hwrrecognitionb-28786](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecognitionb-28786.html#hwrrecognitionb-28786)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RECOGNITION_B_PK | RECOGNITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOGNITION_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the recognition table. |
| RECOGNITION_TEXT | CLOB |  |  |  | This is the full text of the recognition. |
| RECOGNITION_DATE | TIMESTAMP |  |  |  | This is the date of the recognition. |
| RECOMMENDER_ID | VARCHAR2 | 500 |  |  | This is the unique Id of the recommender. |
| RECOMMENDER_GBL_PRFL_ID | NUMBER |  | 18 |  | This is the global profile ID of the recommender. |
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
| HWR_RECOGNITION_B_U1 | Unique | FUSION_TS_TX_DATA | RECOGNITION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
