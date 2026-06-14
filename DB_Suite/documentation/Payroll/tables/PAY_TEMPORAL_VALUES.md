# PAY_TEMPORAL_VALUES

This table contains values that can change over time.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemporalvalues-30093.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemporalvalues-30093.html)

## Primary Key

| Name | Columns |
|------|----------|
| pay_temporal_values_PK | TEMPORAL_VALUE_ID, START_DATE, END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPORAL_VALUE_ID | NUMBER |  | 18 | Yes | Primary Key Id |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| TIME_DEPEND_VALUE_ID | NUMBER |  | 18 | Yes | TIME_DEPEND_VALUE_ID |
| LEVEL_ID | NUMBER |  | 18 | Yes | LEVEL_ID |
| VALUE | VARCHAR2 | 180 |  |  | VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TEMPORAL_VALUES_N1 | Non Unique | Default | LEVEL_ID, TIME_DEPEND_VALUE_ID |
| PAY_TEMPORAL_VALUES_PK | Unique | Default | TEMPORAL_VALUE_ID, START_DATE, END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
