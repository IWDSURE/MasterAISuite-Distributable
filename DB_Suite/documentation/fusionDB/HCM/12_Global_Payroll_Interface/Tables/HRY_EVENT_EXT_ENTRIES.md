# HRY_EVENT_EXT_ENTRIES

Event Entry details data for whom the archive job is submitted.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventextentries-12594.html#hryeventextentries-12594](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventextentries-12594.html#hryeventextentries-12594)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EVENT_EXT_ENTRIES_PK | HRY_EVENT_EXT_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_EVENT_EXT_ENTRY_ID | NUMBER |  | 18 | Yes | Event Extract Entry Id. Primary Key of the table. |
| EVENT_FETCH_RUN_ID | NUMBER |  | 18 |  | Event Fetch Run ID reference from hry_event_fetch_runs table. |
| EVENT_EXT_PROCESS_DTL_ID | NUMBER |  | 18 |  | Event Extract Process Detail Id reference from hry_event_process_details table. |
| EXT_RUN_ID | NUMBER |  | 18 |  | Payroll action id of the run submitted. |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Extract Definition ID Value of Payroll Connect. |
| PAYROLL_ID | NUMBER |  | 18 |  | Payroll ID Value. Derived ID Value for a person. |
| EVENT_CATEGORY_ID | NUMBER |  | 18 |  | Event Category ID. Reference ID Mapping column from hry_event_categories table. |
| EVENT_CAT_TYPE_MAP_ID | NUMBER |  | 18 |  | Event Category Type Mapping ID. Primary Key Column. |
| OBJECT_ID | NUMBER |  | 22 |  | Genereated Object ID when an interface is run. |
| PROCESS_DATE | DATE |  |  |  | Indicates the date at which the row is effective. |
| KEY_VALUES | VARCHAR2 | 250 |  |  | Identifier ValueS to be stroed in Key Fields. |
| PERSON_ID | NUMBER |  | 18 |  | Person ID Value. Derived ID Value for a person. |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the Event Processed for Payroll Connect. |
| RETRY_COUNT | NUMBER |  | 4 |  | Retry Counts maintained for Payroll Connect. |
| PURGE_DATE | DATE |  |  |  | Date to be Purged for Payroll Connect. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EVENT_EXT_ENTRIES_N1 | Non Unique | Default | PAYROLL_ID, EVENT_CATEGORY_ID, EXT_DEFINITION_ID |
| HRY_EVENT_EXT_ENTRIES_N2 | Non Unique | Default | EVENT_FETCH_RUN_ID |
| HRY_EVENT_EXT_ENTRIES_PK | Unique | Default | HRY_EVENT_EXT_ENTRY_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
