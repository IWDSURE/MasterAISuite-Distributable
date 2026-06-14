# CMP_TCS_ROW_IN_CAT_TL

Setup Translatable Table that stores the Category Row Details.Captures the Row display name, description, Zero value flag details. Stores the Top-level category row details for the section and the category row details.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsrowincattl-25060.html#cmptcsrowincattl-25060](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsrowincattl-25060.html#cmptcsrowincattl-25060)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ROW_IN_CAT_TL_PK | ROW_IN_CAT_ID, LANGUAGE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROW_IN_CAT_ID | NUMBER |  | 18 | Yes | ROW_IN_CAT_ID |
| DISPLAY_NAME | VARCHAR2 | 240 |  | Yes | DISPLAY_NAME |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| ZERO_ALERT_MSG | CLOB |  |  |  | ZERO_ALERT_MSG |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_ROW_IN_CAT_TL_UK1 | Unique | FUSION_TS_TX_DATA | ROW_IN_CAT_ID, LANGUAGE, BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
