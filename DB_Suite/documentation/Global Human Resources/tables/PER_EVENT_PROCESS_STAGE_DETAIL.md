# PER_EVENT_PROCESS_STAGE_DETAIL

This table is used to store the event process stage details during Person synchronization process.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pereventprocessstagedetail-27608.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pereventprocessstagedetail-27608.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EVENT_PROCESS_STAGE_D_PK | EVENT_PROCESS_STAGE_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_PROCESS_STAGE_DETAIL_ID | NUMBER |  | 18 | Yes | The enterprise for which this responsibility applies. Allow multi-tenancy customers. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| EVENT_PROCESS_STAGE_ID | NUMBER |  | 18 | Yes | Foreign Key to the PER_EVENT_PROCESS_STAGE table |
| PERSON_ID | NUMBER |  | 18 | Yes | Person ID for which the event has to be raised. |
| EVENT_RAISE_DATE | DATE |  |  |  | Date on which the event should be raised. |
| EVENT_TYPE | VARCHAR2 | 256 |  |  | Type of the event. valid values  "INSERT", "UPDATE" |
| SOURCE_OBJECT_NAME | VARCHAR2 | 1024 |  |  | Source Object Name which fired the event. |
| CHANGED_PERSON_DETAILS_FLAG | VARCHAR2 | 3 |  |  | This flag identifies whether "Changed Person Details Event" should be raised or not. |
| CHANGED_KEYWORDS_FLAG | VARCHAR2 | 3 |  |  | This flag identifies whether "Changed keywords" should be raised or not. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | Number assigned to the person, to identify the person uniquely in any context, not dependent on being an employee, contingent worker, etc. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EVENT_PROCESS_STAGE_DTL_N1 | Non Unique | Default | PERSON_ID, EVENT_PROCESS_STAGE_ID |
| PER_EVENT_PROCESS_STAGE_D_PK | Unique | Default | EVENT_PROCESS_STAGE_DETAIL_ID |
| PER_EVENT_PROCESS_STAGE_DTL_N2 | Non Unique | Default | CREATION_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
