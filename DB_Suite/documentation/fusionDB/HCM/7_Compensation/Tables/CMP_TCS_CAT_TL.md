# CMP_TCS_CAT_TL

Setup Translatable Table that stores the Category Details.Captures Category Name, Category Type Code, Contribution Type, Unit of measure, Drill down Options, number of columns, additional information, description text, graph details, display order of components.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscattl-30648.html#cmptcscattl-30648](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscattl-30648.html#cmptcscattl-30648)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_CAT_TL_PK | CAT_ID, LANGUAGE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAT_ID | NUMBER |  | 18 | Yes | CAT_ID |
| NAME | VARCHAR2 | 240 |  | Yes | NAME |
| CHART1_TITLE | VARCHAR2 | 240 |  |  | CHART1_TITLE |
| CHART2_TITLE | VARCHAR2 | 240 |  |  | CHART2_TITLE |
| CHART_RN_TITLE | VARCHAR2 | 240 |  |  | CHART_RN_TITLE |
| ADDL_INFO | CLOB |  |  |  | ADDL_INFO |
| ADDL_INFO_TITLE | VARCHAR2 | 240 |  |  | ADDL_INFO_TITLE |
| DESC_TXT | CLOB |  |  |  | DESC_TXT |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_CAT_TL_N1 | Non Unique | Default | UPPER("NAME") |
| CMP_TCS_CAT_TL_UK1 | Unique | FUSION_TS_TX_DATA | CAT_ID, LANGUAGE, BUSINESS_GROUP_ID |
| CMP_TCS_CAT_TL_UK2 | Unique | FUSION_TS_TX_DATA | NAME, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
