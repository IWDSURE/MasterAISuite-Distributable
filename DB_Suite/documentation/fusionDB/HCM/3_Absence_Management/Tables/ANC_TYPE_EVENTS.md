# ANC_TYPE_EVENTS

Intersection table between absence type and events

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anctypeevents-11681.html#anctypeevents-11681](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anctypeevents-11681.html#anctypeevents-11681)

## Primary Key

| Name | Columns |
|------|----------|
| anc_type_events_PK | TYPE_EVENTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TYPE_EVENTS_ID | NUMBER |  | 18 | Yes | Type Events Id |
| EVENT_ID | NUMBER |  | 18 | Yes | Event Id |
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | Absence Type Id |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| PROC_TYPE | VARCHAR2 | 32 |  | Yes | Processing Type: ORA_ANC_EVAL_ABS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_TYPE_EVENTS_N1 | Non Unique | Default | EVENT_ID |
| ANC_TYPE_EVENTS_U1 | Unique | Default | TYPE_EVENTS_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
