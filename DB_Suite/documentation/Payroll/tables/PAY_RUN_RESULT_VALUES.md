# PAY_RUN_RESULT_VALUES

This table contains result values from processing a single element entry.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrunresultvalues-14127.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrunresultvalues-14127.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RUN_RESULT_VALUES_PK | INPUT_VALUE_ID, RUN_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES. |
| RUN_RESULT_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_RUN_RESULTS. |
| RESULT_VALUE | VARCHAR2 | 60 |  |  | The value of the result. |
| FORMULA_RESULT_FLAG | VARCHAR2 | 1 |  | Yes | Indicates if the RESULT_VALUE was produced as a result of a Fast Formula calculation |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RUN_RESULT_VALUES_N50 | Non Unique | Default | RUN_RESULT_ID |
| PAY_RUN_RESULT_VALUES_PK | Unique | Default | INPUT_VALUE_ID, RUN_RESULT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
