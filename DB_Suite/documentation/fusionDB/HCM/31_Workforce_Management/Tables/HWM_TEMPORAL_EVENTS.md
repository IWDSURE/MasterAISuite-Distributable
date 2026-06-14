# HWM_TEMPORAL_EVENTS

Table used for storing temporal events

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtemporalevents-25907.html#hwmtemporalevents-25907](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtemporalevents-25907.html#hwmtemporalevents-25907)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TEMPORAL_EVENTS_PK | TEMPORAL_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPORAL_EVENT_ID | NUMBER |  | 18 | Yes | TEMPORAL_EVENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| TEMPORAL_EVENT_NAME | VARCHAR2 | 64 |  | Yes | TEMPORAL_EVENT_NAME |
| TEMPORAL_EVENT_CATEGORY | VARCHAR2 | 64 |  | Yes | TEMPORAL_EVENT_CATEGORY |
| MINUTE_TRIGGER | NUMBER |  | 9 |  | MINUTE_TRIGGER |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DAY_TRIGGER | NUMBER |  | 9 |  | DAY_TRIGGER |
| MONTH_TRIGGER | NUMBER |  | 9 |  | MONTH_TRIGGER |
| HOUR_TRIGGER | NUMBER |  | 9 |  | HOUR_TRIGGER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| YEAR_TRIGGER | NUMBER |  | 9 |  | YEAR_TRIGGER |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TEMPORAL_EVENTS_U1 | Unique | Default | TEMPORAL_EVENT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
