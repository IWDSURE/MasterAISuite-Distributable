# HNS_NOTES_

HNS NOTES. This table stores all the notes. Notes are primarily CLOB column and stored separately.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsnotes-12664.html#hnsnotes-12664](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsnotes-12664.html#hnsnotes-12664)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_NOTES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, NOTES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTES_ID | NUMBER |  | 18 | Yes | NOTES_ID unique identifer. Primary key for table HNS_NOTES. |
| AUTHOR_ID | NUMBER |  | 18 |  | Author identifier for a NOTES. Author  is an employee who add comments to the note. |
| NOTES_CREATION_DATE | TIMESTAMP |  |  |  | Notes Create Date column. Date autopopulated once a note is created. |
| NOTES | CLOB |  |  |  | Notes clob column. This column is an append only column. |
| TASK_ID | NUMBER |  | 18 |  | Task Identifier. Task is defined as either incident_id, investigation_id or action_id. |
| UPDATED_BY | VARCHAR2 | 250 |  |  | The person / owner who updated the note. Note is an append only column. It can only be updated. |
| UPDATED_DATE | TIMESTAMP |  |  |  | UPDATE_DATE column: The date the note got updated. |
| TASK_TYPE_CODE | VARCHAR2 | 30 |  |  | Type of task i.e. Incident, Investigation or Action. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_NOTESN1_ | Non Unique | Default | NOTES_ID, LAST_UPDATE_DATE |
| HNS_NOTES_UK1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, NOTES_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
