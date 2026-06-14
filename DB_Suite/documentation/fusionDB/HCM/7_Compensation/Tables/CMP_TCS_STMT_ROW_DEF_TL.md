# CMP_TCS_STMT_ROW_DEF_TL

Stroes translatable inforamtion of CMP_TCS_STMT_TBL_ROW_DEF table

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtrowdeftl-15600.html#cmptcsstmtrowdeftl-15600](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtrowdeftl-15600.html#cmptcsstmtrowdeftl-15600)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_RODF_TL_PK | STMT_TBL_ROW_DEF_ID, LANGUAGE, BUSINESS_GROUP_ID, PERD_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_TBL_ROW_DEF_ID | NUMBER |  | 18 | Yes | STMT_TBL_ROW_DEF_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| DISPLAY_NAME | VARCHAR2 | 240 |  |  | DISPLAY_NAME |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| ZERO_ALERT_MSG | CLOB |  |  |  | ZERO_ALERT_MSG |
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
| CMP_TCS_STMT_RODF_TL_UK1 | Unique | FUSION_TS_TX_DATA | STMT_TBL_ROW_DEF_ID, LANGUAGE, BUSINESS_GROUP_ID, PERD_RUN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
