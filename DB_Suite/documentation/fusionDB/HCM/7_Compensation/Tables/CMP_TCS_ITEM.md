# CMP_TCS_ITEM

Table holds Comp Tcs Item records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsitem-25062.html#cmptcsitem-25062](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsitem-25062.html#cmptcsitem-25062)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_ITEM_PK | ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ITEM_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| NAME | VARCHAR2 | 240 |  |  | NAME |
| SOURCE_CD | VARCHAR2 | 30 |  | Yes | indicates the type of source for the compensation item |
| SOURCE_KEY | NUMBER |  | 18 |  | It is the key for the source table which is identified by the source_cd |
| DATA_TYPE_CD | VARCHAR2 | 30 |  |  | Compensation Type |
| ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | Indicates if the value was an estimated value or an actual value |
| UOM | VARCHAR2 | 30 |  |  | When the source is Formula, it captures the currency |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | If the souce is formula the non-monetary code is captured. If the source is of non-monetary type this attribute will hold a value which overrides the non-monetary code of the element entry. |
| ROUNDING_CD | VARCHAR2 | 30 |  |  | ROUNDING_CD |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SOURCE_KEY_CHAR1 | VARCHAR2 | 100 |  |  | Record type of worker data from an external source |
| SOURCE_KEY_CHAR2 | VARCHAR2 | 100 |  |  | Value column of worker data from an external source |
| SELECTION_CRITERIA | VARCHAR2 | 32 |  |  | Salary Scope for salary item source |
| STAT_CD | VARCHAR2 | 30 |  |  | Status of Compensation Items |
| PRORATION_FLAG | VARCHAR2 | 1 |  |  | Allows Proration of this Element Entry Item |
| CALC_EXPR | VARCHAR2 | 4000 |  |  | Calculation Item Expression |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_ITEM_N1 | Non Unique | Default | SOURCE_CD, SOURCE_KEY, ITEM_ID, BUSINESS_GROUP_ID |
| CMP_TCS_ITEM_N3 | Non Unique | Default | DATA_TYPE_CD |
| CMP_TCS_ITEM_UK1 | Unique | Default | ITEM_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
