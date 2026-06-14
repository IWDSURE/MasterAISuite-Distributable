# BEN_ELIGY_CRIT_VALUES

BEN_ELIGY_CRIT_VALUES stores eligibility criteria values for user defined criteria.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligycritvalues-8945.html#beneligycritvalues-8945](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligycritvalues-8945.html#beneligycritvalues-8945)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIGY_CRIT_VALUES_PK | ELIGY_CRIT_VALUES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIGY_CRIT_VALUES_ID | NUMBER |  | 18 | Yes | Primary Key |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Eligibility Profile Identifier |
| ELIGY_CRITERIA_ID | NUMBER |  | 18 | Yes | Criteria Identifier |
| START_DATE | DATE |  |  |  | Start Date |
| END_DATE | DATE |  |  |  | End Date |
| ORDR_NUM | NUMBER |  | 18 |  | Sequence Number |
| NUMBER_VALUE1 | NUMBER |  |  |  | Number Value 1 |
| NUMBER_VALUE2 | NUMBER |  |  |  | Number Value 2 |
| CHAR_VALUE1 | VARCHAR2 | 240 |  |  | Character Value 1 |
| CHAR_VALUE2 | VARCHAR2 | 240 |  |  | Character Value 2 |
| DATE_VALUE1 | DATE |  |  |  | Date Value 1 |
| DATE_VALUE2 | DATE |  |  |  | Date Value 2 |
| EXCLD_FLAG | VARCHAR2 | 30 |  | Yes | Exclude Flag |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Enterprise Identifier |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code |
| CRITERIA_SCORE | NUMBER |  |  |  | Criteria Score |
| CRITERIA_WEIGHT | NUMBER |  |  |  | Criteria Weight |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| NUMBER_VALUE3 | NUMBER |  |  |  | Number Value 3 |
| NUMBER_VALUE4 | NUMBER |  |  |  | Number Value 4 |
| CHAR_VALUE3 | VARCHAR2 | 240 |  |  | Character Value 3 |
| CHAR_VALUE4 | VARCHAR2 | 240 |  |  | Character Value 4 |
| DATE_VALUE3 | DATE |  |  |  | Date Value 3 |
| DATE_VALUE4 | DATE |  |  |  | Date Value 4 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIGY_CRIT_VALUES_FK2 | Non Unique | Default | ELIGY_CRITERIA_ID |
| BEN_ELIGY_CRIT_VALUES_FK3 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_ELIGY_CRIT_VALUES_PK | Unique | Default | ELIGY_CRIT_VALUES_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
