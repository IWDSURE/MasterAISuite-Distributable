# PER_CALENDAR_EVENTS_TL

Language dependent table . Stores the translated data for PER_CALENDAR_EVENTS

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percalendareventstl-18345.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percalendareventstl-18345.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CALENDAR_EVENTS_TL_PK | CALENDAR_EVENT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CALENDAR_EVENT_ID | NUMBER |  | 18 | Yes | Foreign Key for PER_CALENDAR_EVENTS |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 80 |  | Yes | User defined Calendar event name |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of calendar event |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CALENDAR_EVENTS_TL_PK | Unique | Default | CALENDAR_EVENT_ID, LANGUAGE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
