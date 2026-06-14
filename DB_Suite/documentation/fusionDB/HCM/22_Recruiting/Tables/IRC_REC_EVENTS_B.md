# IRC_REC_EVENTS_B

This is the base table to store the event related details

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventsb-20014.html#ircreceventsb-20014](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventsb-20014.html#ircreceventsb-20014)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENTS_B_PK | EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ID | NUMBER |  | 18 | Yes | Primary key of the table. Auto generated. |
| APPLIED_METRICS_DAYS | NUMBER |  | 18 |  | Specifies the Applied metrics timeframe In days. |
| HIRED_METRICS_DAYS | NUMBER |  | 18 |  | Specifies the Hired metrics timeframe In days. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS_F table. |
| EVENT_NUMBER | VARCHAR2 | 64 |  | Yes | The unique number which gets generated to represent an event. |
| EVENT_START_DATE | TIMESTAMP |  |  |  | Stores the start date of the event. |
| EVENT_END_DATE | TIMESTAMP |  |  |  | Stores the end date of the event. |
| EVENT_CATEGORY_CODE | VARCHAR2 | 30 |  |  | Category code of the event which is configured in HCM_LOOKUP table. The corresponding lookup type is ORA_IRC_REC_EVT_CATEGORY. |
| EVENT_OWNER_ID | NUMBER |  | 18 |  | Person id of the event owner. Foreign key to PER_PERSONS. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| APPLY_FLOW_ID | NUMBER |  | 18 |  | To store the registration form id of an event. Foreign key to IRC_APPLY_FLOWS_B table. |
| EVENT_LAST_REG_DATE | TIMESTAMP |  |  |  | Stores the last date for registration. |
| EVENT_VISIBILITY_CODE | VARCHAR2 | 30 |  |  | To store the visibility code of the event. The corresponding lookup type is ORA_IRC_REC_EVT_VISIBILITY. |
| PUBLISH_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the status of the published event as a lookup code. The lookup type is ORA_IRC_REC_EVT_PUBLISH_STATUS. |
| PUBLISH_START_DATE | TIMESTAMP |  |  |  | Stores the start date and time of the published event. |
| PUBLISH_END_DATE | TIMESTAMP |  |  |  | Stores the end date and time of the published event. |
| PUBLISH_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Stores the time zone used of the published event. |
| HRT_POOL_ID | NUMBER |  | 18 |  | Stores the hrt pool id. Foreign Key to hrt_pools_b table |
| EVENT_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Stores the timezone of the event. |
| EVENT_CREATION_MODE | VARCHAR2 | 30 |  |  | Stores the event creation mode. It uses the lookup type ORA_IRC_REC_EVT_CRE_MODE |
| PHASE_CODE | VARCHAR2 | 64 |  |  | Stores the phase code of the event, the corresponding look up type is ORA_IRC_REC_EVT_PHASE_CODE |
| MAX_REG_COUNT | NUMBER |  | 9 |  | Stores the maximum registration allowed for an event |
| ENABLE_INTERVIEW_FLAG | VARCHAR2 | 1 |  |  | Stores whether interview is enabled or not for this event. |
| MANUAL_REGN_CONFIRM_FLAG | VARCHAR2 | 1 |  |  | Stores Manual registration status for this event. |
| POOL_MEM_PROC_TEMPLATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PROCESSES_B table. Stores the ID of the process template that registrations on this event will follow. |
| EVENT_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Stores the timestamp at which corresponding
 row has last updated. |
| WALKIN_REGISTRATION_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if on-spot registration is enabled for this event or not. |
| QR_CODE_CHECKIN_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if qr code checkin is enabled for this event or not |
| REMINDER_NOTIFICATION_FLAG | VARCHAR2 | 1 |  |  | Indicates if reminder notification is sent to the candidate. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENTS_B_FK1 | Non Unique | Default | EVENT_OWNER_ID |
| IRC_REC_EVENTS_B_FK2 | Non Unique | Default | HRT_POOL_ID |
| IRC_REC_EVENTS_B_FK3 | Non Unique | Default | APPLY_FLOW_ID |
| IRC_REC_EVENTS_B_FK4 | Non Unique | Default | BUSINESS_UNIT_ID |
| IRC_REC_EVENTS_B_FK5 | Non Unique | Default | POOL_MEM_PROC_TEMPLATE_ID |
| IRC_REC_EVENTS_B_N1 | Non Unique | Default | EVENT_NUMBER |
| IRC_REC_EVENTS_B_N2 | Non Unique | Default | UPPER("EVENT_NUMBER") |
| IRC_REC_EVENTS_B_N3 | Non Unique | Default | EVENT_CATEGORY_CODE |
| IRC_REC_EVENTS_B_N4 | Non Unique | Default | PHASE_CODE |
| IRC_REC_EVENTS_B_N5 | Non Unique | Default | EVENT_START_DATE |
| IRC_REC_EVENTS_B_N6 | Non Unique | Default | PUBLISH_STATUS_CODE, PUBLISH_START_DATE, PUBLISH_END_DATE |
| IRC_REC_EVENTS_B_PK | Unique | Default | EVENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
