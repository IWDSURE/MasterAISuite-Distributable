# CMP_TCS_ROW_IN_CAT

Setup Table that stores the Category Row Details.Captures the Row display name, description, Zero value flag details. Stores the Top-level category row details for the section and the category row details.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsrowincat-31338.html#cmptcsrowincat-31338](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsrowincat-31338.html#cmptcsrowincat-31338)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ROW_IN_CAT_PK | ROW_IN_CAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROW_IN_CAT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CAT_ID | NUMBER |  | 18 |  | Foreign key to CMP_TCS_CAT |
| SUBCAT_ID | NUMBER |  | 18 |  | Compensation sub-category present in a category Foreign key to CMP_TCS_CAT |
| STMT_ID | NUMBER |  | 18 |  | STMT_ID |
| ORDR_NUM | NUMBER |  | 18 | Yes | Order number |
| URL | VARCHAR2 | 2000 |  |  | Url providing extra information about the compensation items |
| ZERO_VALUE_OPTIONS | VARCHAR2 | 30 |  |  | ZERO_VALUE_OPTIONS |
| HIDE_ZERO_ALERT_FLAG | VARCHAR2 | 1 |  |  | HIDE_ZERO_ALERT_FLAG |
| EXCLUDE_FROM_SMRY_FLAG | VARCHAR2 | 1 |  |  | EXCLUDE_FROM_SMRY_FLAG |
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
| CMP_TCS_ROW_IN_CAT_N1 | Non Unique | Default | CAT_ID, SUBCAT_ID |
| CMP_TCS_ROW_IN_CAT_UK1 | Unique | Default | ROW_IN_CAT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
