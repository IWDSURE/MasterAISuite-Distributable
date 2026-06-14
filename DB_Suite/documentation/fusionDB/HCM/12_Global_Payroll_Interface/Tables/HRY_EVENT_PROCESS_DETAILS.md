# HRY_EVENT_PROCESS_DETAILS

Event Process details data gives the input to extracts runs for which persons to be picked up.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventprocessdetails-28306.html#hryeventprocessdetails-28306](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventprocessdetails-28306.html#hryeventprocessdetails-28306)

## Primary Key

| Name | Columns |
|------|----------|
| hry_event_ext_process_deta_PK | HRY_EVENT_EXT_PROCESS_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_EVENT_EXT_PROCESS_DTL_ID | NUMBER |  | 18 | Yes | Event Extract Process Detail Id |
| HRY_EVENT_CAT_TYPE_MAP_ID | NUMBER |  | 18 |  | Event Category Type Mapping ID. Primary Key Column. |
| HRY_EVENT_CATEGORY_ID | NUMBER |  | 18 |  | Event Category ID. Reference ID Mapping column from hry_event_categories table. |
| HRY_EVENT_EXT_RUN_ID | NUMBER |  | 18 |  | Foreign key mapping to HRY_EVENT_EXT_RUNS. This id gives source id and source run type values. |
| PAYROLL_REL_ID | NUMBER |  | 18 |  | Payroll Relationship ID. Derived ID Value for a person. |
| PAYROLL_REL_NUM | VARCHAR2 | 30 |  |  | Payrol Relationship Number. Derived ID Value for a person. |
| PERSON_ID | NUMBER |  | 18 |  | Person ID Value. Derived ID Value for a person. |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | Person Number Value. Derived ID Value for a person. |
| WORK_REL_ID | NUMBER |  | 18 |  | Work Relationship ID. Derived ID Value for a person. |
| PAYROLL_ID | NUMBER |  | 18 |  | Payroll ID Value. Derived ID Value for a person. |
| EVENT_PUBLISH_TIME | TIMESTAMP |  |  |  | Event Published Time for Payroll Connect. |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_FROM | DATE |  |  |  | Event Effective From Date. Indicates the date at which the row is effective. |
| KEY_VALUE1 | VARCHAR2 | 250 |  |  | Identifier Value to be stroed in Key Value 1 |
| KEY_VALUE2 | VARCHAR2 | 250 |  |  | Identifier Value to be stroed in Key Value 2 |
| KEY_VALUE3 | VARCHAR2 | 250 |  |  | Identifier Value to be stroed in Key Value 3 |
| KEY_VALUE4 | VARCHAR2 | 250 |  |  | Identifier Value to be stroed in Key Value 4 |
| KEY_VALUE5 | VARCHAR2 | 250 |  |  | Identifier Value to be stroed in Key Value 5 |
| PRIORITY | VARCHAR2 | 30 |  |  | Preference to be considered when running Payroll Connect. |
| OBJECT_ID | NUMBER |  | 22 |  | Genereated Object ID when an interface is run. |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Extract Definition ID Value of Payroll Connect. |
| KEY_IDENTIFIER1 | VARCHAR2 | 250 |  |  | Identifier Column to be stroed in Key Identifier 1. |
| KEY_IDENTIFIER2 | VARCHAR2 | 250 |  |  | Identifier Column to be stroed in Key Identifier 2. |
| KEY_IDENTIFIER3 | VARCHAR2 | 250 |  |  | Identifier Column to be stroed in Key Identifier 3. |
| ECID | VARCHAR2 | 250 |  |  | ECID Value from the HRC Events Table. |
| ACTION_OCCURRENCE_ID | VARCHAR2 | 250 |  |  | Action Occurence ID Value from Hrc Events table. |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the Event Processed for Payroll Connect. |
| MESSAGE_TEXT | VARCHAR2 | 4000 |  |  | Message Text to be displayed for Payroll Connect. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Processed Date of an Employee for Payroll Connect. |
| EXCLUDE_FROM_PROCESS | VARCHAR2 | 1 |  |  | Exclude From Process or not for Payroll Connect. |
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
| HRY_EVENT_PROCESS_DETAILS_N1 | Non Unique | Default | OBJECT_ID, STATUS, EXT_DEFINITION_ID, HRY_EVENT_CATEGORY_ID |
| HRY_EVENT_PROCESS_DETAILS_N2 | Non Unique | Default | WORK_REL_ID, PAYROLL_ID, STATUS, EXT_DEFINITION_ID, EVENT_PUBLISH_TIME, EFFECTIVE_FROM, PRIORITY |
| HRY_EVENT_PROCESS_DETAILS_N3 | Non Unique | Default | HRY_EVENT_EXT_RUN_ID |
| HRY_EVENT_PROCESS_DETAILS_N4 | Non Unique | Default | PERSON_ID |
| HRY_EVENT_PROCESS_DETAILS_PK | Unique | Default | HRY_EVENT_EXT_PROCESS_DTL_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
