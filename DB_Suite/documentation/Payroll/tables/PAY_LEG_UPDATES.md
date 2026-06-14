# PAY_LEG_UPDATES

PAY_LEG_UPDATES - contains seed row for planned updates by Country and Update Type

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdates-26238.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdates-26238.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_LEG_UPDATES_PK | PAY_STAT_UPDATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_STAT_UPDATE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | Legislation Code |
| UPDATE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The update type code of the legislative update. |
| UPDATE_FOR_YEAR | NUMBER |  | 4 | Yes | Year of the legislative update. |
| UPDATE_FOR_MONTH | VARCHAR2 | 30 |  | Yes | Month of the legislative update. |
| SEQ_FOR_YEAR_MON | NUMBER |  | 4 | Yes | Sequence of the legislative update for the applicable year and month. |
| MANDATORY_FLAG | VARCHAR2 | 5 |  |  | Indicates whether legislative update is a mandatory update. Valid value are Y,N |
| APPLY_FLAG | VARCHAR2 | 5 |  |  | Indicates if the legislative update can be skipped. Valid value are Y,N |
| PROCESS_STATUS | VARCHAR2 | 1 |  |  | Indicates the process status of legislative update. Valid values are I - In process, E - Error, C - Complete |
| PAY_REQUEST_ID | NUMBER |  | 18 |  | Request ID of the Flow Request |
| PROCESS_START_DATE_TIME | TIMESTAMP |  |  |  | ESS job upload start date/time |
| PROCESS_END_DATE_TIME | TIMESTAMP |  |  |  | ESS job upload end date/time |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_LEG_UPDATES_PK | Unique | Default | PAY_STAT_UPDATE_ID, ORA_SEED_SET1 |
| PAY_LEG_UPDATES_PK1 | Unique | Default | PAY_STAT_UPDATE_ID, ORA_SEED_SET2 |
| PAY_LEG_UPDATES_UK1 | Unique | Default | LEGISLATION_CODE, UPDATE_TYPE_CODE, UPDATE_FOR_YEAR, UPDATE_FOR_MONTH, SEQ_FOR_YEAR_MON, ORA_SEED_SET1 |
| PAY_LEG_UPDATES_UK11 | Unique | Default | LEGISLATION_CODE, UPDATE_TYPE_CODE, UPDATE_FOR_YEAR, UPDATE_FOR_MONTH, SEQ_FOR_YEAR_MON, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
