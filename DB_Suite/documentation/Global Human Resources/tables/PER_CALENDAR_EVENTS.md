# PER_CALENDAR_EVENTS

This table is used to hold calendar events like public holidays

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percalendarevents-29140.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percalendarevents-29140.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CALENDAR_EVENTS_PK | CALENDAR_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CALENDAR_EVENT_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| SHORT_CODE | VARCHAR2 | 48 |  | Yes | Unique Event Short Code | Active |
| CATEGORY | VARCHAR2 | 30 |  | Yes | Event Category like Public Holidays | Active |
| START_DATE_TIME | TIMESTAMP |  |  | Yes | Start Date Time of Event | Active |
| END_DATE_TIME | TIMESTAMP |  |  | Yes | End Date Time of Event | Active |
| COVERAGE_TYPE | VARCHAR2 | 30 |  |  | Coverage Type (ORG or GEO) | Active |
| TREE_STRUCTURE_CODE | VARCHAR2 | 30 |  |  | Foreign key to TREE_STRUCTURE_CODE on FND_TREE | Active |
| TREE_CODE | VARCHAR2 | 30 |  |  | Foreign key to TREE_CODE on FND_TREE. | Active |
| TREE_VERSION_ID | VARCHAR2 | 32 |  |  | Foreign key to VERSION_ID on FND_TREE_VERSION | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| HALF_DAY_FOR_ELAPSED | VARCHAR2 | 1 |  |  | Property that allows differentiating full calendar event from half day calendar event. |  |
| EVENT_TYPE | VARCHAR2 | 64 |  |  | EVENT_TYPE |  |
| ALL_DAY_FLAG | VARCHAR2 | 1 |  |  | ALL_DAY_FLAG |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CALENDAR_EVENTS_N1 | Non Unique | Default | BUSINESS_GROUP_ID, START_DATE_TIME, END_DATE_TIME, COVERAGE_TYPE |
| PER_CALENDAR_EVENTS_PK | Unique | FUSION_TS_TX_IDX | CALENDAR_EVENT_ID |
| PER_CALENDAR_EVENTS_U2 | Unique | Default | SHORT_CODE, BUSINESS_GROUP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
