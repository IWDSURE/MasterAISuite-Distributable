# PAY_DATES

This entity stores Payroll information about when an employee was eligible for Payroll processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydates-6650.html#paydates-6650](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydates-6650.html#paydates-6650)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DATES_PK | PAY_DATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_DATE_ID | NUMBER |  | 18 | Yes | PAY_DATE_ID |
| DATE_VALUE | DATE |  |  | Yes | DATE_VALUE |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 5 |  | Yes | SOURCE_TYPE |
| TIME_DEFINITION_ID | NUMBER |  | 18 | Yes | TIME_DEFINITION_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DATES_N1 | Non Unique | Default | TIME_DEFINITION_ID |
| PAY_DATES_N2 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_DATES_PK | Unique | Default | PAY_DATE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
