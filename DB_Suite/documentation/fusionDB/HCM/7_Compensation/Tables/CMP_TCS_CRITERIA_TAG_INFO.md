# CMP_TCS_CRITERIA_TAG_INFO

Table holds Comp Tcs Criteria Tag records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscriteriataginfo-23880.html#cmptcscriteriataginfo-23880](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscriteriataginfo-23880.html#cmptcscriteriataginfo-23880)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_CRITERIA_TAG_INFO_PK | CRITERIA_TAG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRITERIA_TAG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| CRITERIA_DEF_ID | NUMBER |  | 18 |  | Foreign key to CMP_TCS_CRITERIA_DEF table |
| CRITERIA_ID | NUMBER |  | 18 |  | Earlier used as Foreign key to CMP_TCS_CRITERIA table |
| ITEM_ID | NUMBER |  | 18 | Yes | Item Id of the item in Compensation Item lov |
| ITEM_VALUE | VARCHAR2 | 30 |  | Yes | Column to decide which value of the item should be used to evaluate the Criteria. |
| TRANSFORM_OPERATOR | VARCHAR2 | 30 |  |  | Transform Operator |
| TRANSFORM_NUM_VALUE | NUMBER |  |  |  | Number value in Transform input field for Monetary/Non-monetary items |
| COMPARISON_OPERATOR | VARCHAR2 | 30 |  | Yes | Value Operator |
| NUMERIC_COMPARISON_VALUE | NUMBER |  |  |  | Number value in Value input field for Monetary/Non-monetary items |
| TEXT_COMPARISON_VALUE | VARCHAR2 | 30 |  |  | Text value in Value input field for Text items |
| DATE_COMPARISON_VALUE | DATE |  |  |  | Date value in Value input field for Date items |
| OPEN_PARENTHESES | VARCHAR2 | 20 |  |  | Left Parenthesis value |
| CLOSE_PARENTHESES | VARCHAR2 | 20 |  |  | Right Parenthesis value |
| CONJUNCTION_OPERATOR | VARCHAR2 | 20 |  |  | Next Component value |
| CRITERIA | VARCHAR2 | 3000 |  |  | Conditional Displat Sub-criterion |
| ORDR_NUM | NUMBER |  | 9 | Yes | Order number of sub-criterion |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_CRITERIA_TAG_INFO_U1 | Unique | Default | CRITERIA_TAG_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
