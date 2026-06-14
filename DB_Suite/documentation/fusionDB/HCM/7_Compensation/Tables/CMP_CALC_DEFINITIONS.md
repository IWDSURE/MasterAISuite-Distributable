# CMP_CALC_DEFINITIONS

Stores dynamic calculation definitions

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcalcdefinitions-28294.html#cmpcalcdefinitions-28294](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcalcdefinitions-28294.html#cmpcalcdefinitions-28294)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CALC_DEFINITIONS_PK | DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEFINITION_ID | NUMBER |  | 18 | Yes | DEFINITION_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| DEF_KEY | NUMBER |  | 18 | Yes | DEF_KEY |
| KEY_TYPE | VARCHAR2 | 30 |  | Yes | KEY_TYPE |
| VIEW_ATTRIBUTE | VARCHAR2 | 60 |  | Yes | VIEW_ATTRIBUTE |
| EXE_ORDER | NUMBER |  | 18 | Yes | EXE_ORDER |
| PARTI_PROCESS_ENA | VARCHAR2 | 1 |  |  | PARTI_PROCESS_ENA |
| REFRESH_PROCESS_ENA | VARCHAR2 | 1 |  |  | REFRESH_PROCESS_ENA |
| WRKSHT_TAB_OUT_ENA | VARCHAR2 | 1 |  |  | WRKSHT_TAB_OUT_ENA |
| WRKSHT_SAVE_ENA | VARCHAR2 | 1 |  |  | WRKSHT_SAVE_ENA |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CALC_DEFINITIONS_N1 | Non Unique | Default | DEF_KEY, KEY_TYPE, VIEW_ATTRIBUTE |
| CMP_CALC_DEFINITIONS_UK1 | Unique | Default | DEFINITION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
