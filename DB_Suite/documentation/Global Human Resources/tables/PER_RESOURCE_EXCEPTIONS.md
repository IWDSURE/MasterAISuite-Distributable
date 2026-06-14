# PER_RESOURCE_EXCEPTIONS

This tables holds the resource exception data used during schedule assignment to resources

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perresourceexceptions-28876.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perresourceexceptions-28876.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_RESOURCE_EXCEPTIONS_PK | EXCEPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXCEPTION_ID | NUMBER |  | 18 | Yes | System generated part of the primary key. Surrogate key. |
| EXCEPTION_NAME | VARCHAR2 | 80 |  | Yes | Name of the exception |
| START_DATE_TIME | TIMESTAMP |  |  | Yes | Start Date Time for Exception |
| END_DATE_TIME | TIMESTAMP |  |  | Yes | End Date Time for Exception |
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
|-------|------------|------------|----------|
| PER_RESOURCE_EXCEPTIONS_N1 | Non Unique | Default | EXCEPTION_NAME |
| PER_RESOURCE_EXCEPTIONS_U1 | Unique | Default | EXCEPTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
