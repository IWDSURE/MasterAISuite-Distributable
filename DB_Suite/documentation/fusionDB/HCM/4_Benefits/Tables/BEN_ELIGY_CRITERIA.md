# BEN_ELIGY_CRITERIA

To hold the information about the new criteria defined by user (with a criteria_type = 'USER'), what is the valid list of values for the criteria and the table.column, which should be retrieved for a person to be validated against the criteria values

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligycriteria-11097.html#beneligycriteria-11097](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligycriteria-11097.html#beneligycriteria-11097)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIGY_CRITERIA_PK | ELIGY_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIGY_CRITERIA_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the New Criteria. |
| SHORT_CODE | VARCHAR2 | 30 |  | Yes | Short Code. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Description. |
| CRITERIA_TYPE | VARCHAR2 | 30 |  | Yes | Criteria Type. |
| CRIT_COL1_VAL_TYPE_CD | VARCHAR2 | 30 |  | Yes | Criteria Column Value Type. |
| CRIT_COL1_DATATYPE | VARCHAR2 | 10 |  | Yes | Criteria Column Datatype. |
| COL1_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | Lookup Type for Criteria Values. |
| COL1_VALUE_SET_ID | NUMBER |  | 18 |  | Value Set to get Criteria Values. |
| ACCESS_TABLE_NAME1 | VARCHAR2 | 30 |  |  | Table containing person?s information for this criterion. |
| ACCESS_COLUMN_NAME1 | VARCHAR2 | 30 |  |  | Column containing person?s information for this criterion. |
| TIME_ENT_ACC_TABLE_NAME1 | VARCHAR2 | 30 |  |  | Time Entry Access Table Name 1 |
| TIME_ENT_ACC_COL_NAME1 | VARCHAR2 | 30 |  |  | Column where person?s time entry for this criteria can be obtained. |
| CRIT_COL2_VAL_TYPE_CD | VARCHAR2 | 30 |  |  | Criteria Column Value Type. |
| CRIT_COL2_DATATYPE | VARCHAR2 | 10 |  |  | Criteria Column Datatype. |
| COL2_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | Lookup Type for Criteria Values. |
| COL2_VALUE_SET_ID | NUMBER |  | 18 |  | Value Set to get Criteria Values. |
| ACCESS_TABLE_NAME2 | VARCHAR2 | 30 |  |  | Table containing person information for this criterion. |
| ACCESS_COLUMN_NAME2 | VARCHAR2 | 30 |  |  | Column containing person?s information for this criterion. |
| TIME_ENT_ACC_TABLE_NAME2 | VARCHAR2 | 30 |  |  | Time Entry Access Table Name 2 |
| TIME_ENTRY_ACCESS_COL_NAME2 | VARCHAR2 | 30 |  |  | Column where person?s time entry for this criteria can be obtained. |
| ACCESS_CALC_RULE | NUMBER |  | 18 |  | Fast formula |
| ALW_RANGE_VALIDATION_FLAG | VARCHAR2 | 10 |  |  | Flag to determine if Range Validation is allowed or not |
| USER_DEFINED_FLAG | VARCHAR2 | 30 |  |  | User defined Y or N |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ALW_RANGE_VALIDATION_FLAG2 | VARCHAR2 | 30 |  |  | Flag to determine if Range Validation is allowed or not |
| ACCESS_CALC_RULE2 | NUMBER |  | 18 |  | Access Calculation Rule (Set 2) |
| TIME_ACCESS_CALC_RULE1 | NUMBER |  | 18 |  | Time Access Calculation Rule (Set 1) |
| TIME_ACCESS_CALC_RULE2 | NUMBER |  | 18 |  | Time Access Calculation Rule (Set 2) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIGY_CRITERIA_N1 | Non Unique | Default | NAME |
| BEN_ELIGY_CRITERIA_PK | Unique | Default | ELIGY_CRITERIA_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
