# PAY_CHUNK_STATUS

This table contains the status of processing on specific units of work to be processed by a payroll action or process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychunkstatus-19738.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychunkstatus-19738.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CHUNK_STATUS_PK | PAYROLL_ACTION_ID, CHUNK_NUMBER, ACTION_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to PAY_PAYROLL_ACTIONS |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | ACTION_TYPE |
| CHUNK_NUMBER | NUMBER |  | 18 | Yes | Number used to group events into chunks for parallelization. |
| RAND_CHUNK_NUMBER | NUMBER |  | 18 | Yes | Number used to group events into chunks for parallelization. |
| POPULATION_STATUS | VARCHAR2 | 1 |  | Yes | Valid population statuses for a Chunk. |
| PROCESS_STATUS | VARCHAR2 | 1 |  | Yes | Valid process statuses for a Chunk |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_CHUNK_STATUS_N2 | Non Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER, POPULATION_STATUS |
| PAY_CHUNK_STATUS_PK | Unique | Default | PAYROLL_ACTION_ID, CHUNK_NUMBER, ACTION_TYPE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
