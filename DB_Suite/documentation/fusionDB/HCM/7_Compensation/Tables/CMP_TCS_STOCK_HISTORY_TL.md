# CMP_TCS_STOCK_HISTORY_TL

Stores translatable information of  CMP_TCS_STOCK_HISTORY

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstockhistorytl-6500.html#cmptcsstockhistorytl-6500](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstockhistorytl-6500.html#cmptcsstockhistorytl-6500)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STKHIST_TL_PK | STOCK_HISTORY_ID, LANGUAGE, BUSINESS_GROUP_ID, PERD_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STOCK_HISTORY_ID | NUMBER |  | 18 | Yes | STOCK_HISTORY_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| GRANT_DATE_LABEL | VARCHAR2 | 240 |  |  | GRANT_DATE_LABEL |
| STOCK_SYMBOL_LABEL | VARCHAR2 | 240 |  |  | STOCK_SYMBOL_LABEL |
| GRANT_NUMBER_LABEL | VARCHAR2 | 240 |  |  | GRANT_NUMBER_LABEL |
| GRANT_NAME_LABEL | VARCHAR2 | 240 |  |  | GRANT_NAME_LABEL |
| GRANT_TYPE_LABEL | VARCHAR2 | 240 |  |  | GRANT_TYPE_LABEL |
| TOTAL_SHRS_LABEL | VARCHAR2 | 240 |  |  | TOTAL_SHRS_LABEL |
| SHRS_GRANTED_LABEL | VARCHAR2 | 240 |  |  | SHRS_GRANTED_LABEL |
| XRCISE_PRICE_LABEL | VARCHAR2 | 240 |  |  | XRCISE_PRICE_LABEL |
| GRANT_PRICE_LABEL | VARCHAR2 | 240 |  |  | GRANT_PRICE_LABEL |
| GRANT_VALUE_LABEL | VARCHAR2 | 240 |  |  | GRANT_VALUE_LABEL |
| CANCELLED_SHRS_LABEL | VARCHAR2 | 240 |  |  | CANCELLED_SHRS_LABEL |
| REASON_CODE_LABEL | VARCHAR2 | 240 |  |  | REASON_CODE_LABEL |
| CLASS_TYPE_LABEL | VARCHAR2 | 240 |  |  | CLASS_TYPE_LABEL |
| EST_MKT_VAL_LABEL | VARCHAR2 | 240 |  |  | EST_MKT_VAL_LABEL |
| MISC_LABEL | VARCHAR2 | 240 |  |  | MISC_LABEL |
| EST_VALUE_LABEL | VARCHAR2 | 240 |  |  | EST_VALUE_LABEL |
| VST_EST_UNEX_MKT_VAL_LABEL | VARCHAR2 | 240 |  |  | VST_EST_UNEX_MKT_VAL_LABEL |
| VST_SHRS_LABEL | VARCHAR2 | 240 |  |  | VST_SHRS_LABEL |
| VST_EX_LABEL | VARCHAR2 | 240 |  |  | VST_EX_LABEL |
| VST_UNEX_LABEL | VARCHAR2 | 240 |  |  | VST_UNEX_LABEL |
| VST_EST_VAL_LABEL | VARCHAR2 | 240 |  |  | VST_EST_VAL_LABEL |
| VST_EST_MKT_VAL_LABEL | VARCHAR2 | 240 |  |  | VST_EST_MKT_VAL_LABEL |
| VST_EST_UNEX_VAL_LABEL | VARCHAR2 | 240 |  |  | VST_EST_UNEX_VAL_LABEL |
| UNVST_SHRS_LABEL | VARCHAR2 | 240 |  |  | UNVST_SHRS_LABEL |
| UNVST_EST_VAL_LABEL | VARCHAR2 | 240 |  |  | UNVST_EST_VAL_LABEL |
| UNVST_EST_MKT_VAL_LABEL | VARCHAR2 | 240 |  |  | UNVST_EST_MKT_VAL_LABEL |
| EXPIRE_DATE_LABEL | VARCHAR2 | 240 |  |  | EXPIRE_DATE_LABEL |
| VEST_DATE_LABEL | VARCHAR2 | 240 |  |  | Label for Vest Date column |
| EXERCISE_DATE_LABEL | VARCHAR2 | 240 |  |  | Label for Exercise Date column |
| CANCEL_DATE_LABEL | VARCHAR2 | 240 |  |  | Label for Calcellation Date column |
| MISC1_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Text 1 column |
| MISC2_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Text 2 column |
| MISC3_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Text 3 column |
| MISC4_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Text 4 column |
| MISC5_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Text 5 column |
| MISC_NUM1_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Number 1 column |
| MISC_NUM2_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Number 2 column |
| MISC_NUM3_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Number 3 column |
| MISC_NUM4_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Number 4 column |
| MISC_NUM5_LABEL | VARCHAR2 | 240 |  |  | Label for Miscellaneous Number 5 column |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STKHIST_TL_UK1 | Unique | FUSION_TS_TX_DATA | STOCK_HISTORY_ID, LANGUAGE, BUSINESS_GROUP_ID, PERD_RUN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
