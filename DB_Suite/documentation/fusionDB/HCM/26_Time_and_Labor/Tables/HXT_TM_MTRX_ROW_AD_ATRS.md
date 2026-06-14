# HXT_TM_MTRX_ROW_AD_ATRS

This table would have the additional row level attributes for each timecard MTRX row. We will have 1..1 association between HXT_TM_MTRX and HXT_TM_MTRX_ROW_AD_ATRS.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxrowadatrs-9122.html#hxttmmtrxrowadatrs-9122](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmmtrxrowadatrs-9122.html#hxttmmtrxrowadatrs-9122)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_MTRX_ROW_AD_ATRS_PK | TM_MTRX_ROW_AD_ATR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TM_MTRX_ROW_AD_ATR_ID | NUMBER |  | 18 | Yes | Primary Key | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| TM_MTRX_ROW_ID | NUMBER |  | 18 | Yes | Foriegn key to HXT_TM_MTRX table | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR1_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR1_VALUE |  |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR2_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR2_VALUE |  |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR3_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR3_VALUE |  |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR4_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR4_VALUE |  |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR5_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR5_VALUE |  |
| ATTRIBUTE_CHAR6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR6_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR6_VALUE |  |
| ATTRIBUTE_CHAR7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR7_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR7_VALUE |  |
| ATTRIBUTE_CHAR8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR8_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR8_VALUE |  |
| ATTRIBUTE_CHAR9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR9_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR9_VALUE |  |
| ATTRIBUTE_CHAR10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR10_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR10_VALUE |  |
| ATTRIBUTE_CHAR11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR11_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR11_VALUE |  |
| ATTRIBUTE_CHAR12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR12_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR12_VALUE |  |
| ATTRIBUTE_CHAR13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR13_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR13_VALUE |  |
| ATTRIBUTE_CHAR14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR14_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR14_VALUE |  |
| ATTRIBUTE_CHAR15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR15_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR15_VALUE |  |
| ATTRIBUTE_CHAR16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR16_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR16_VALUE |  |
| ATTRIBUTE_CHAR17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR17_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR17_VALUE |  |
| ATTRIBUTE_CHAR18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR18_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR18_VALUE |  |
| ATTRIBUTE_CHAR19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR19_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR19_VALUE |  |
| ATTRIBUTE_CHAR20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR20_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR20_VALUE |  |
| ATTRIBUTE_CHAR21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR21_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR21_VALUE |  |
| ATTRIBUTE_CHAR22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR22_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR22_VALUE |  |
| ATTRIBUTE_CHAR23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR23_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR23_VALUE |  |
| ATTRIBUTE_CHAR24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR24_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR24_VALUE |  |
| ATTRIBUTE_CHAR25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR25_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR25_VALUE |  |
| ATTRIBUTE_CHAR26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR26_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR26_VALUE |  |
| ATTRIBUTE_CHAR27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR27_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR27_VALUE |  |
| ATTRIBUTE_CHAR28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR28_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR28_VALUE |  |
| ATTRIBUTE_CHAR29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR29_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR29_VALUE |  |
| ATTRIBUTE_CHAR30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_CHAR30_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_CHAR30_VALUE |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER1_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER1_VALUE |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER2_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER2_VALUE |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER3_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER3_VALUE |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER4_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER4_VALUE |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER5_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER5_VALUE |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER6_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER6_VALUE |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER7_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER7_VALUE |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER8_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER8_VALUE |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER9_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER9_VALUE |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER10_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER10_VALUE |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER11_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER11_VALUE |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER12_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER12_VALUE |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER13_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER13_VALUE |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER14_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER14_VALUE |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER15_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER15_VALUE |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER16_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER16_VALUE |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER17_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER17_VALUE |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER18_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER18_VALUE |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER19_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER19_VALUE |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER20_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_NUMBER20_VALUE |  |
| ATTRIBUTE_ALT_NAME1 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME1 |  |
| ATTRIBUTE_ALT_NAME1_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME1_VALUE |  |
| ATTRIBUTE_ALT_NAME2 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME2 |  |
| ATTRIBUTE_ALT_NAME2_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME2_VALUE |  |
| ATTRIBUTE_ALT_NAME3 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME3 |  |
| ATTRIBUTE_ALT_NAME3_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME3_VALUE |  |
| ATTRIBUTE_ALT_NAME4 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME4 |  |
| ATTRIBUTE_ALT_NAME4_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME4_VALUE |  |
| ATTRIBUTE_ALT_NAME5 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME5 |  |
| ATTRIBUTE_ALT_NAME5_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME5_VALUE |  |
| ATTRIBUTE_ALT_NAME6 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME6 |  |
| ATTRIBUTE_ALT_NAME6_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME6_VALUE |  |
| ATTRIBUTE_ALT_NAME7 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME7 |  |
| ATTRIBUTE_ALT_NAME7_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME7_VALUE |  |
| ATTRIBUTE_ALT_NAME8 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME8 |  |
| ATTRIBUTE_ALT_NAME8_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME8_VALUE |  |
| ATTRIBUTE_ALT_NAME9 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME9 |  |
| ATTRIBUTE_ALT_NAME9_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME9_VALUE |  |
| ATTRIBUTE_ALT_NAME10 | NUMBER |  | 18 |  | ATTRIBUTE_ALT_NAME10 |  |
| ATTRIBUTE_ALT_NAME10_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_ALT_NAME10_VALUE |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE1_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE1_VALUE |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE2_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE2_VALUE |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE3_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE3_VALUE |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE4_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE4_VALUE |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE5_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE5_VALUE |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE6_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE6_VALUE |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE7_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE7_VALUE |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE8_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE8_VALUE |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE9_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE9_VALUE |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE10_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE10_VALUE |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE11_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE11_VALUE |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE12_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE12_VALUE |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE13_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE13_VALUE |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE14_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE14_VALUE |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_DATE15_VALUE | VARCHAR2 | 150 |  |  | ATTRIBUTE_DATE15_VALUE |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_MTRX_ROW_AD_ATRS_N1 | Non Unique | Default | TM_MTRX_ROW_ID |
| HXT_TM_MTRX_ROW_AD_ATRS_PK | Unique | Default | TM_MTRX_ROW_AD_ATR_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
