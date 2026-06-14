# PAY_PROCESS_TIMINGS

This table contains the timings for processing areas.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocesstimings-26721.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocesstimings-26721.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_TIMING_ID | NUMBER |  | 18 | Yes | Primary Key |
| CALL_NAME | VARCHAR2 | 240 |  | Yes | Name of the function call |
| TIME_TAKEN | NUMBER |  | 18 | Yes | Time Taken in call |
| CALL_COUNT | NUMBER |  | 18 | Yes | Count of Calls |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Enterprise of the Call |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to Payroll Actions |
| ESS_REQUEST_ID | VARCHAR2 | 18 |  |  | ESS Request Id |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PROCESS_TIMINGS_N1 | Non Unique | Default | PAYROLL_ACTION_ID |
| PAY_PROCESS_TIMINGS_PK | Unique | Default | PROCESS_TIMING_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
