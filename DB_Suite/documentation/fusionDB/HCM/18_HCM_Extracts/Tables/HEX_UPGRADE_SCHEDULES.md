# HEX_UPGRADE_SCHEDULES

The table stores the list of schedules for processes.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexupgradeschedules-11775.html#hexupgradeschedules-11775](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexupgradeschedules-11775.html#hexupgradeschedules-11775)

## Primary Key

| Name | Columns |
|------|----------|
| hex_upgrade_schedules_PK | SCHEDULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_ID | NUMBER |  | 18 | Yes | The column indicates the unique sequence generated value. |
| ACTIVE_STATUS | VARCHAR2 | 30 |  |  | The column indicates the status of the schedule. |
| BASE_SCHEDULE_NAME | VARCHAR2 | 30 |  |  | The column indicates the name for the schedule. |
| PROCESS_CODE | VARCHAR2 | 400 |  |  | The column indicates the Scheduled Process Name. |
| START_RELEASE | VARCHAR2 | 30 |  |  | The column indicates the start release for the specified process. Format to be used is 11132501. |
| END_RELEASE | VARCHAR2 | 30 |  |  | The column indicates the end release for the specified process.Format to be used is 11132501. |
| FREQUENCY | VARCHAR2 | 30 |  |  | The column indicates the frequency for the specified process. |
| START_DATE | DATE |  |  |  | The column indicates the start date of the schedule. |
| END_DATE | DATE |  |  |  | The column indicates the end date of the schedule. |
| PROCESS_PARAMETERS | VARCHAR2 | 4000 |  |  | The column indicates the parameters specified for the schedule. |
| RETRIES | NUMBER |  | 18 |  | The column indicates the number of retries allowed for the schedule. |
| PROCESS_CONFIG_GROUP | VARCHAR2 | 100 |  |  | The column indicates the default configuration group to be used for the process. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_UPGRADE_SCHEDULES_PK | Unique | Default | SCHEDULE_ID, ORA_SEED_SET1 |
| HEX_UPGRADE_SCHEDULES_PK1 | Unique | Default | SCHEDULE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
