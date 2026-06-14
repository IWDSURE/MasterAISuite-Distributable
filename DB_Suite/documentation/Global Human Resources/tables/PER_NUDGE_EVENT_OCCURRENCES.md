# PER_NUDGE_EVENT_OCCURRENCES

This table records the nudge event occurrences.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeeventoccurrences-7288.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernudgeeventoccurrences-7288.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NUDGE_EVENT_OCCURRENCES_PK | NUDGE_EVENT_OCCURRENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NUDGE_EVENT_OCCURRENCE_ID | NUMBER |  | 18 | Yes | NUDGE_EVENT_OCCURRENCE_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | OBJECT_TYPE |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_ID |
| PROCESSING_STATUS | VARCHAR2 | 30 |  | Yes | PROCESSING_STATUS |
| PROCESS_ID | NUMBER |  | 18 |  | PROCESS_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_NUDGE_EVENT_OCCURRENCES_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_ID |
| PER_NUDGE_EVENT_OCCURRENCES_N2 | Non Unique | PER_NUDGE_EVENT_OCCURRENCES_N2 | PROCESS_ID |
| PER_NUDGE_EVENT_OCCURRENCES_PK | Unique | Default | NUDGE_EVENT_OCCURRENCE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
