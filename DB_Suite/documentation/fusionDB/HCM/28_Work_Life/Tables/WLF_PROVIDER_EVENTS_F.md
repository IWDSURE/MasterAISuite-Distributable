# WLF_PROVIDER_EVENTS_F

Table to maintain provider events information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfprovidereventsf-19705.html#wlfprovidereventsf-19705](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfprovidereventsf-19705.html#wlfprovidereventsf-19705)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROVIDER_EVENTS_F_PK | PROVIDER_EVENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROVIDER_EVENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PROVIDER_ACCOUNT_ID | NUMBER |  | 18 | Yes | Unique identifier of the wlf provider accounts table. |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 600 |  |  | Unique identifier of the event from external provider. |
| SOURCE_ID | NUMBER |  | 18 | Yes | Identifier of the object, the event belongs to |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Type of the object for which the event belongs |
| ORGANIZER_EMAIL | VARCHAR2 | 256 |  |  | Email of the event organizer. |
| EVENT_TYPE | CHAR | 1 |  |  | Identifier to differentiate a calendar event and an alert event. |
| EVENT_PROCESSED_TIME | TIMESTAMP |  |  |  | Indicates processed time of a provider event |
| EVENT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates status of a provider event |
| ACTIVITY_STATE | CLOB |  |  |  | Contains state of learning activity in JSON format. |
| ADDITIONAL_INFO | VARCHAR2 | 4000 |  |  | This column is used to store the additional info like iCalId, retry count of the provider event. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_EVENTS_F_N1 | Non Unique | Default | EVENT_STATUS |
| WLF_PROVIDER_EVENTS_F_N2 | Non Unique | WLF_PROVIDER_EVENTS_F_N2 | SOURCE_ID, SOURCE_TYPE |
| WLF_PROVIDER_EVENTS_F_N3 | Non Unique | WLF_PROVIDER_EVENTS_F_N3 | PROVIDER_ACCOUNT_ID |
| WLF_PROVIDER_EVENTS_F_N4 | Non Unique | WLF_PROVIDER_EVENTS_F_N4 | ORGANIZER_EMAIL |
| WLF_PROVIDER_EVENTS_F_N5 | Non Unique | Default | EVENT_TYPE |
| WLF_PROVIDER_EVENTS_F_U1 | Unique | Default | PROVIDER_EVENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
