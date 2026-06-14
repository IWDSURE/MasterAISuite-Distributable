# ANC_PER_EVENTS

This table holds information of  the absence person event.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperevents-3004.html#ancperevents-3004](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperevents-3004.html#ancperevents-3004)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_EVENTS_PK | PERSON_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | Person Event Identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| PRD_OF_SVC_ID | NUMBER |  | 18 | Yes | Periods of service identifier |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | LEGAL_ENTITY_ID |
| EVENT_ID | NUMBER |  | 18 | Yes | Event Identifier |
| EVENT_DATE | DATE |  |  | Yes | Event date |
| STATUS | VARCHAR2 | 30 |  | Yes | status |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REF_PK_ID | NUMBER |  | 18 | Yes | Reference primary key id of the event |
| OTBI_FLAG_MODIFIED_DT | DATE |  |  |  | Updated the value to Sysdate when the OTBI_REPORT_PROC_FLAG is set to N |
| OTBI_REPORT_PROC_FLAG | VARCHAR2 | 1 |  |  | ‘Y’ represents daily breakdown of absence record is processed and populated in the new table. ‘N’ represents daily breakdown of absence record is not processed/not populated in the new table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_EVENTS_N1 | Non Unique | Default | PERSON_ID, EVENT_ID |
| ANC_PER_EVENTS_N2 | Non Unique | Default | REF_PK_ID |
| ANC_PER_EVENTS_U1 | Unique | FUSION_TS_TX_DATA | PERSON_EVENT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
