# HTS_CONSOL_EVT_SCH_UNIT_USAGES

The table is used to track the usage of consolidated event changes for schedule units.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsconsolevtschunitusages-15930.html#htsconsolevtschunitusages-15930](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsconsolevtschunitusages-15930.html#htsconsolevtschunitusages-15930)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_CONSOL_EVT_SCH_UNIT_US_PK | CONS_EVENT_PRCS_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONS_EVENT_PRCS_USAGE_ID | NUMBER |  | 18 | Yes | Unique identifier for each consolidated event processing usage record |
| CONSOLIDATE_CHANGE_EVENT_ID | NUMBER |  | 18 | Yes | References the consolidated change event record in the HTS_CONSOL_EVT_CHANGES table. |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SCHEDULE_UNIT_PROCESS_ID | NUMBER |  | 18 | Yes | Foreign key of hts_schedule_unit_processes |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | enterprise id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_CONSOL_EVT_SCH_UNIT_US_N1 | Non Unique | Default | SCHEDULE_UNIT_PROCESS_ID |
| HTS_CONSOL_EVT_SCH_UNIT_US_PK | Unique | Default | CONS_EVENT_PRCS_USAGE_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
