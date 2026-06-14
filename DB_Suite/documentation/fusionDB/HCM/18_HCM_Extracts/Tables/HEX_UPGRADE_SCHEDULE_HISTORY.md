# HEX_UPGRADE_SCHEDULE_HISTORY

The table stores the history of runs for all schedules.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexupgradeschedulehistory-17639.html#hexupgradeschedulehistory-17639](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexupgradeschedulehistory-17639.html#hexupgradeschedulehistory-17639)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_UPGRADE_SCHEDULE_HISTO_PK | SCHEDULE_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_RUN_ID | NUMBER |  | 18 | Yes | The column indicates the unique sequence generated value. |
| PROCESS_ID | NUMBER |  | 18 |  | The column indicates the reference from the table HEX_PROCESS_METADATA. |
| SCHEDULE_ID | NUMBER |  | 18 |  | The column indicates the reference from the table HEX_SCHEDULE_METADATA. |
| START_DATE | TIMESTAMP |  |  |  | The column indicates the start time for the request. |
| END_DATE | TIMESTAMP |  |  |  | The column indicates the end time for the request. |
| NEXT_SCHEDULE_DATE | DATE |  |  |  | The column indicates the next upcoming schedule date. |
| PROCESS_STATUS | VARCHAR2 | 30 |  |  | The column indicates the status of the process. |
| PARENT_REQ_ID | NUMBER |  | 18 |  | The column indicates the initial request id which has triggered the schedule. |
| SPECIAL_STATUS_FLAG | VARCHAR2 | 30 |  |  | The column indicates if the current run is initial/latest run. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_RUN_RELEASE | VARCHAR2 | 30 |  |  | The column indicates the last run release for the schedule. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_UPGRADE_SCHEDULE_HISTO_N1 | Non Unique | Default | PROCESS_ID |
| HEX_UPGRADE_SCHEDULE_HISTO_N2 | Non Unique | Default | SCHEDULE_ID |
| HEX_UPGRADE_SCHEDULE_HISTO_N3 | Non Unique | Default | PROCESS_STATUS |
| HEX_UPGRADE_SCHEDULE_HISTO_N4 | Non Unique | Default | SPECIAL_STATUS_FLAG |
| HEX_UPGRADE_SCHEDULE_HISTO_PK | Unique | Default | SCHEDULE_RUN_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
