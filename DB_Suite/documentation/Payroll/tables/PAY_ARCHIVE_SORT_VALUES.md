# PAY_ARCHIVE_SORT_VALUES

Table for Archive action sort values

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payarchivesortvalues-29708.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payarchivesortvalues-29708.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_SORT_VALUES_PK | PAY_ARCHIVE_SORT_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_ARCHIVE_SORT_VALUE_ID | NUMBER |  | 18 | Yes | PAY_ARCHIVE_SORT_VALUE_ID |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 10 |  | Yes | SOURCE_TYPE |
| SORT_VALUE1 | VARCHAR2 | 240 |  |  | SORT_VALUE1 |
| PARENT_ACT_INFO_ID | NUMBER |  | 18 |  | PARENT_ACT_INFO_ID |
| SORT_VALUE2 | VARCHAR2 | 240 |  |  | SORT_VALUE2 |
| SORT_VALUE3 | VARCHAR2 | 240 |  |  | SORT_VALUE3 |
| SORT_VALUE4 | VARCHAR2 | 240 |  |  | SORT_VALUE4 |
| SORT_VALUE5 | VARCHAR2 | 240 |  |  | SORT_VALUE5 |
| SORT_VALUE6 | VARCHAR2 | 240 |  |  | SORT_VALUE6 |
| SORT_VALUE7 | VARCHAR2 | 240 |  |  | SORT_VALUE7 |
| SORT_VALUE8 | VARCHAR2 | 240 |  |  | SORT_VALUE8 |
| SORT_VALUE9 | VARCHAR2 | 240 |  |  | SORT_VALUE9 |
| SORT_VALUE10 | VARCHAR2 | 240 |  |  | SORT_VALUE10 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ARCHIVE_SORT_VALUES_N1 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_ARCHIVE_SORT_VALUES_N2 | Non Unique | Default | PAYROLL_ACTION_ID |
| PAY_ARCHIVE_SORT_VALUES_PK | Unique | Default | PAY_ARCHIVE_SORT_VALUE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
