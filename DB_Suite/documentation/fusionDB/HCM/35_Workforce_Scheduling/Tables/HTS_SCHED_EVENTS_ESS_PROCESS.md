# HTS_SCHED_EVENTS_ESS_PROCESS

Table to track the status of the Schedule events ESS Process per Integrators.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedeventsessprocess-29617.html#htsschedeventsessprocess-29617](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedeventsessprocess-29617.html#htsschedeventsessprocess-29617)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_EVENTS_ESS_PRCS_PK | SCHED_ESS_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_ESS_PROCESS_ID | NUMBER |  | 18 | Yes | SCHED_ESS_PROCESS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | ESS_REQUEST_ID |
| PROCESS_RUN_DATE | TIMESTAMP |  |  | Yes | PROCESS_RUN_DATE |
| STATUS | VARCHAR2 | 20 |  | Yes | STATUS |
| ERROR_TEXT | VARCHAR2 | 4000 |  |  | ERROR_TEXT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_EVENTS_ESS_PRCS_N1 | Non Unique | FUSION_TS_SEED | ESS_REQUEST_ID |
| HTS_SCHED_EVENTS_ESS_PRCS_N2 | Non Unique | FUSION_TS_SEED | STATUS |
| HTS_SCHED_EVENTS_ESS_PRCS_U1 | Unique | FUSION_TS_SEED | SCHED_ESS_PROCESS_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
