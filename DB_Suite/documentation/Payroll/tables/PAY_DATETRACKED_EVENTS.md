# PAY_DATETRACKED_EVENTS

This table contains information about what the event captures and stores, such as a change to a grade, an element entry

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydatetrackedevents-10270.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydatetrackedevents-10270.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DATETRACKED_EVENTS_PK | DATETRACKED_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATETRACKED_EVENT_ID | NUMBER |  | 18 | Yes | DATETRACKED_EVENT_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_GROUP_ID | NUMBER |  | 18 | Yes | EVENT_GROUP_ID |
| DATED_TABLE_ID | NUMBER |  | 18 | Yes | DATED_TABLE_ID |
| COLUMN_NAME | VARCHAR2 | 80 |  |  | COLUMN_NAME |
| UPDATE_TYPE | VARCHAR2 | 80 |  | Yes | UPDATE_TYPE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 30 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PRORATION_STYLE | VARCHAR2 | 30 |  |  | PRORATION_STYLE |
| REF1_EVENT_TYPE_ID | NUMBER |  | 18 |  | REF1_EVENT_TYPE_ID |
| REF2_EVENT_TYPE_ID | NUMBER |  | 18 |  | REF2_EVENT_TYPE_ID |
| REF3_EVENT_TYPE_ID | NUMBER |  | 18 |  | REF3_EVENT_TYPE_ID |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_DATETRACKED_EVENTS_FK2 | Non Unique | Default | DATED_TABLE_ID |
| PAY_DATETRACKED_EVENTS_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DATETRACKED_EVENTS_PK | Unique | Default | DATETRACKED_EVENT_ID, ORA_SEED_SET1 |
| PAY_DATETRACKED_EVENTS_PK1 | Unique | Default | DATETRACKED_EVENT_ID, ORA_SEED_SET2 |
| PAY_DATETRACKED_EVTS_N1 | Non Unique | Default | DATED_TABLE_ID, UPDATE_TYPE, COLUMN_NAME |
| PAY_DATETRACKED_EVTS_UK1 | Unique | Default | EVENT_GROUP_ID, DATED_TABLE_ID, COLUMN_NAME, UPDATE_TYPE, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_DATETRACKED_EVTS_UK11 | Unique | Default | EVENT_GROUP_ID, DATED_TABLE_ID, COLUMN_NAME, UPDATE_TYPE, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
