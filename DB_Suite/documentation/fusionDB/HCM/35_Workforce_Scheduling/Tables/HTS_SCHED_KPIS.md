# HTS_SCHED_KPIS

This table is dedicated to the KPI that were calculated during a schedule validation execution.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedkpis-22570.html#htsschedkpis-22570](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedkpis-22570.html#htsschedkpis-22570)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_KPIS_PK | SCHED_KPI_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_KPI_ID | NUMBER |  | 18 | Yes | The ID of the schedule KPI. |
| SCHED_FULL_VALIDATION_ID | NUMBER |  | 18 | Yes | The ID of the schedule validation execution having generated this KPI. |
| KPI_NAME_LOOKUP_TYPE | VARCHAR2 | 30 |  | Yes | The reference to the lookup denoting the KPI name enumeration. |
| KPI_NAME_LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | The reference to the lookup denoting the KPI name enumeration value. |
| VALUE | NUMBER |  |  |  | The KPI value. |
| VALUE_UNIT_CODE | VARCHAR2 | 30 |  |  | The unit of the KPI value. |
| KPI_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The type of the KPI. |
| SCOPE_START_DATE | DATE |  |  |  | The scope start date for kpis having a temporal scope. |
| SCOPE_END_DATE | DATE |  |  |  | The scope end date for kpis having a temporal scope. |
| PARENT_KPI_ID | NUMBER |  | 18 |  | The ID of the parent KPI. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | EnterpriseId |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_KPIS_N1 | Non Unique | Default | SCHED_FULL_VALIDATION_ID |
| HTS_SCHED_KPIS_PK | Unique | Default | SCHED_KPI_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
