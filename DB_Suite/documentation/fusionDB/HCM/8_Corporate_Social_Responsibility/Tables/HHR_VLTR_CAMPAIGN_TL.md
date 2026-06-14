# HHR_VLTR_CAMPAIGN_TL

This table stores translation campaigns information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrcampaigntl-22104.html#hhrvltrcampaigntl-22104](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrcampaigntl-22104.html#hhrvltrcampaigntl-22104)

## Primary Key

| Name | Columns |
|------|----------|
| hhr_vltr_campaign_tl_PK | CAMPAIGN_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMPAIGN_ID | NUMBER |  | 18 | Yes | CAMPAIGN_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CAMPAIGN_NAME | VARCHAR2 | 100 |  |  | PROJECT_NAME |
| CAMPAIGN_DESCRIPTION | VARCHAR2 | 4000 |  |  | PROJECT_DESCRIPTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hhr_vltr_campaign_tl_U1 | Unique | FUSION_TS_TX_IDX | CAMPAIGN_ID, LANGUAGE |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
