# PAY_STATISTIC_CONTEXT_VALUES

Stores context values, against contexts available in pay_statistic_contexts.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontextvalues-24834.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontextvalues-24834.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_STATISTIC_CONTEXT_VAL_PK | STATISTIC_CONTEXT_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATISTIC_CONTEXT_VALUE_ID | NUMBER |  | 18 | Yes | STATISTIC_CONTEXT_VALUE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| SOURCE_VALUE | VARCHAR2 | 200 |  |  | SOURCE_VALUE |
| STATISTIC_CONTEXT_ID | NUMBER |  | 18 | Yes | STATISTIC_CONTEXT_ID |
| STATISTIC_CONTEXT_VALUE | VARCHAR2 | 200 |  | Yes | STATISTIC_CONTEXT_VALUE |
| PAY_REQUEST_ID | NUMBER |  | 18 | Yes | PAY_REQUEST_ID |
| CONTEXT_SEQUENCE | NUMBER |  | 18 | Yes | CONTEXT_SEQUENCE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_STATISTIC_CONTEXT_VAL_N1 | Non Unique | Default | PAY_REQUEST_ID |
| PAY_STATISTIC_CONTEXT_VAL_PK | Unique | Default | STATISTIC_CONTEXT_VALUE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
