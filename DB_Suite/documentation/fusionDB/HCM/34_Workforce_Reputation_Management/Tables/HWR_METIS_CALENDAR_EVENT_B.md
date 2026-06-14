# HWR_METIS_CALENDAR_EVENT_B

The message table stores information about the beehive calendar events.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmetiscalendareventb-28011.html#hwrmetiscalendareventb-28011](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmetiscalendareventb-28011.html#hwrmetiscalendareventb-28011)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_METIS_CALENDAR_EVENT_PK | CAL_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAL_EVENT_ID | NUMBER |  | 18 | Yes | CALENDAThis is the primary key for this table. The number should be generated from the sequence HWR METIS_CALENDAR_EVENT_S |
| UDID | VARCHAR2 | 200 |  | Yes | UDID |
| MEETING_PARTICIPANTS | VARCHAR2 | 4000 |  | Yes | MEETING_PARTICIPANTS |
| MEETING_ORGANIZER | VARCHAR2 | 200 |  | Yes | MEETING_ORGANIZER |
| STATUS | VARCHAR2 | 100 |  |  | CALENDAR EVENT STATUS |
| MEETING_START_TIME | TIMESTAMP |  |  | Yes | MEETING_START_TIME |
| MEETING_END_TIME | TIMESTAMP |  |  |  | MEETING_END_TIME |
| MEETING_CREATION_DATE | TIMESTAMP |  |  | Yes | MEETING_CREATION_DATE |
| MEETING_UPDATE_DATE | TIMESTAMP |  |  | Yes | MEETING_UPDATE_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_METIS_CALENDAR_EVENT_B_U1 | Unique | FUSION_TS_TX_DATA | CAL_EVENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
