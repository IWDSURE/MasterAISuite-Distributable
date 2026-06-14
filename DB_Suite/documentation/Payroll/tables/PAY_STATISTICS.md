# PAY_STATISTICS

Stores the statistics for payroll. based on the types available in statistics types.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatistics-28500.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatistics-28500.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_STATISTICS_PK | STATISTIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATISTIC_ID | NUMBER |  | 18 | Yes | STATISTIC_ID |
| CONTEXT_SEQUENCE | NUMBER |  | 18 |  | CONTEXT_SEQUENCE |
| STATISTIC_TYPE_ID | NUMBER |  | 18 |  | STATISTIC_TYPE_ID |
| PAY_REQUEST_ID | NUMBER |  | 18 |  | PAY_REQUEST_ID |
| STATISTIC_VALUE | VARCHAR2 | 200 |  |  | STATISTIC_VALUE |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| SOURCE_VALUE | VARCHAR2 | 200 |  |  | SOURCE_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CURRENCY | VARCHAR2 | 20 |  |  | Currency |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_STATISTICS_N1 | Non Unique | Default | PAY_REQUEST_ID |
| PAY_STATISTICS_PK | Unique | Default | STATISTIC_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
