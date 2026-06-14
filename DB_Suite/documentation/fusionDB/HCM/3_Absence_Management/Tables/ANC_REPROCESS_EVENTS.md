# ANC_REPROCESS_EVENTS

Table for storing reprocessing event data like personId, startDate, endDate, Status ActionId, Processid

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancreprocessevents-24164.html#ancreprocessevents-24164](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancreprocessevents-24164.html#ancreprocessevents-24164)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_REPROCESS_EVENTS_PK | REPROCESS_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPROCESS_EVENT_ID | NUMBER |  | 18 | Yes | REPROCESS_EVENT_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| PROCESS_ID | NUMBER |  | 18 |  | PROCESS_ID |
| STATUS | NUMBER |  | 9 | Yes | STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_REPROCESS_EVENTS_U1 | Unique | Default | REPROCESS_EVENT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
