# PER_SCHEDULE_EXCEPTIONS

This table holds the exception details for every schedule and schedule assignment. The exception can be a Resource exception, calendar event or a calendar event category.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perscheduleexceptions-22526.html#perscheduleexceptions-22526](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perscheduleexceptions-22526.html#perscheduleexceptions-22526)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SCHEDULE_EXCEPTIONS_PK | SCHEDULE_EXCEPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_EXCEPTION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| SCHEDULE_ID | NUMBER |  | 18 |  | Schedule Id to which Exception is attached |
| SCHEDULE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Schedule Assignment Id to which Exception is attached |
| EXCEPTION_TYPE | VARCHAR2 | 30 |  |  | Exception Type like Calendar Event, CAlendar Event Type, Resource exception |
| EXCEPTION_ID | NUMBER |  | 18 |  | Depending upon the exception type, this column holds the corresponding identifier for the exception. |
| EXCEPTION_CODE | VARCHAR2 | 30 |  |  | Exception Code for Calendar Event Types |
| AVAILABILITY_CODE | VARCHAR2 | 30 |  |  | Availability Code (AVAILABLE or NOT AVAILABLE) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SCHEDULE_EXCEPTIONS_N1 | Non Unique | Default | SCHEDULE_ID |
| PER_SCHEDULE_EXCEPTIONS_N2 | Non Unique | Default | SCHEDULE_ASSIGNMENT_ID |
| PER_SCHEDULE_EXCEPTIONS_N3 | Non Unique | Default | EXCEPTION_ID |
| PER_SCHEDULE_EXCEPTIONS_N4 | Non Unique | Default | EXCEPTION_CODE, EXCEPTION_ID |
| PER_SCHEDULE_EXCEPTIONS_N5 | Non Unique | Default | EXCEPTION_CODE, EXCEPTION_TYPE |
| PER_SCHEDULE_EXCEPTIONS_U1 | Unique | Default | SCHEDULE_EXCEPTION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
