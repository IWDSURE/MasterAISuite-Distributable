# IRC_REC_EVENT_POOL_MEMBERS

This table contains information on event pool members.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventpoolmembers-24075.html#ircreceventpoolmembers-24075](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventpoolmembers-24075.html#ircreceventpoolmembers-24075)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENT_POOL_MEMBERS_PK | EVENT_POOL_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_POOL_MEMBER_ID | NUMBER |  | 18 | Yes | The primary key of the table and also foreign Key to HRT_POOL_MEMBERS. |
| REGISTRATION_LANGUAGE_CODE | VARCHAR2 | 4 |  |  | This column will store the language of site while registering for the event. |
| EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REC_EVENTS_B |
| DISQUALIFIED_FLAG | VARCHAR2 | 1 |  |  | To track if candidate was disqualified (aggregate snapshot of DQ answers). |
| QSTNR_SCORE | NUMBER |  | 18 |  | The total questionnaire score for this candidate registration. |
| HRT_POOL_ID | NUMBER |  | 18 | Yes | This column stores the event pool id. Foreign key to HRT_POOLS_B table. |
| PERSON_ID | NUMBER |  | 18 |  | This column stores the event person id.Foreign key to PER_PERSONS table. |
| CURRENT_PHASE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PHASES_B table. |
| CURRENT_STATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_STATES_B table. |
| PROCESS_TEMPLATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PROCESSES_B table. |
| PROCESS_INSTANCE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PROCESSES_B table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REGISTERED_DATE | TIMESTAMP |  |  |  | The date in which the pool member registers for this event. |
| CONFIRMED_DATE | TIMESTAMP |  |  |  | Date in which the registration is confirmed |
| CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | Flag to show if event registration is confirmed |
| AF_VERSION_ID | NUMBER |  | 18 |  | Foreign key to IRC_AF_VERSIONS.AF_VERSION_ID. |
| LEGAL_DESC_VERSION_ID | NUMBER |  | 18 |  | To track the legal disclaimer accepted by the applicant. Foreign key to IRC_DESC_VERSIONS_B.DESC_VERSION_ID. |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | unique identifier of the site from which the registration of event was done. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | indicates the status of the record.for soft deleted records value will be ORA_DELETED |
| REGISTRATION_TYPE | VARCHAR2 | 30 |  |  | Indicates the registration_type of the candidate. |
| CHECKIN_MODE | VARCHAR2 | 30 |  |  | Indicates the type of checkin - manual or QR code or self checkin. |
| CHECKIN_PERSON_ID | NUMBER |  | 18 |  | This column stores the checkin person id. Foreign key to PER_PERSONS table |
| REMINDER_NOTIFICATION_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the reminder notification. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENT_POOL_MBRS_FK10 | Non Unique | Default | CHECKIN_PERSON_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK1 | Non Unique | Default | EVENT_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK2 | Non Unique | Default | HRT_POOL_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK3 | Non Unique | Default | CURRENT_PHASE_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK4 | Non Unique | Default | CURRENT_STATE_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK5 | Non Unique | Default | PROCESS_INSTANCE_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK6 | Non Unique | Default | PROCESS_TEMPLATE_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK7 | Non Unique | Default | PERSON_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK8 | Non Unique | Default | AF_VERSION_ID |
| IRC_REC_EVENT_POOL_MEMBERS_FK9 | Non Unique | Default | LEGAL_DESC_VERSION_ID |
| IRC_REC_EVENT_POOL_MEMBERS_N1 | Non Unique | Default | CREATION_DATE |
| IRC_REC_EVENT_POOL_MEMBERS_PK | Unique | Default | EVENT_POOL_MEMBER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
