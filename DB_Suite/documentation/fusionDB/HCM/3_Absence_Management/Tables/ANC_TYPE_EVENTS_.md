# ANC_TYPE_EVENTS_

Intersection table between absence type and events

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anctypeevents-25401.html#anctypeevents-25401](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anctypeevents-25401.html#anctypeevents-25401)

## Primary Key

| Name | Columns |
|------|----------|
| anc_type_events_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TYPE_EVENTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TYPE_EVENTS_ID | NUMBER |  | 18 | Yes | Type Events Id |
| EVENT_ID | NUMBER |  | 18 |  | Event Id |
| ABSENCE_TYPE_ID | NUMBER |  | 18 |  | Absence Type Id |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise Id |
| PROC_TYPE | VARCHAR2 | 32 |  |  | Processing Type: ORA_ANC_EVAL_ABS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_TYPE_EVENTSN1_ | Non Unique | Default | TYPE_EVENTS_ID |
| ANC_TYPE_EVENTSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TYPE_EVENTS_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
