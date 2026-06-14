# WLF_PROVIDER_BOOKINGS_F

Table to store provider bookings information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderbookingsf-16025.html#wlfproviderbookingsf-16025](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderbookingsf-16025.html#wlfproviderbookingsf-16025)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROVIDER_BOOKINGS_F_PK | PROVIDER_BOOKING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROVIDER_BOOKING_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_BOOKING_NUMBER | VARCHAR2 | 30 |  |  | PROVIDER_BOOKING_NUMBER |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PROVIDER_INSTR_ACCOUNT_ID | NUMBER |  | 18 | Yes | Indicates relation id |
| PROVIDER_ACCOUNT_ID | NUMBER |  | 18 | Yes | Indicates provider id |
| BOOKING_ID | NUMBER |  | 18 | Yes | Indicates booking id |
| PROVIDER_TEMPLATE_ID | NUMBER |  | 18 | Yes | Indicates provider template id |
| MEETING_ID | VARCHAR2 | 250 |  |  | Indicates meeting id of a provider account |
| MEETING_URL | VARCHAR2 | 1000 |  |  | Indicates meeting URL |
| RECORDING_URLS | CLOB |  |  |  | Indicates recording URL |
| RECORDING_DOWNLOAD_FLAG | VARCHAR2 | 1 |  |  | Indicates wheather download recording option enabled or not |
| RECORDING_DOWNLOAD_TIME | TIMESTAMP |  |  |  | Indicates timestamp of download recording |
| ATTENDANCE_DOWNLOAD_FLAG | VARCHAR2 | 1 |  |  | Indicates wheather download attendance option enabled or not |
| ATTENDANCE_DOWNLOAD_TIME | TIMESTAMP |  |  |  | Indicates timestamp of download attendance |
| AUTO_COMPLETION_FLAG | VARCHAR2 | 1 |  |  | Indicates whether auto completion processing done or not. |
| AUTO_COMPLETION_TIME | TIMESTAMP |  |  |  | Indicates timestamp of when auto completion processing done |
| VILT_STATUS | VARCHAR2 | 30 |  |  | Indicates vilt call status |
| VILT_TIME | TIMESTAMP |  |  |  | Indicates vilt call timestamp |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_BOOKINGS_F_N1 | Non Unique | Default | PROVIDER_INSTR_ACCOUNT_ID |
| WLF_PROVIDER_BOOKINGS_F_N2 | Non Unique | Default | PROVIDER_ACCOUNT_ID |
| WLF_PROVIDER_BOOKINGS_F_N3 | Non Unique | Default | BOOKING_ID |
| WLF_PROVIDER_BOOKINGS_F_N4 | Non Unique | Default | PROVIDER_TEMPLATE_ID |
| WLF_PROVIDER_BOOKINGS_F_N5 | Non Unique | Default | MEETING_ID |
| WLF_PROVIDER_BOOKINGS_F_N6 | Non Unique | Default | VILT_STATUS |
| WLF_PROVIDER_BOOKINGS_F_N7 | Non Unique | Default | VILT_TIME |
| WLF_PROVIDER_BOOKINGS_F_N8 | Non Unique | Default | PROVIDER_BOOKING_NUMBER |
| WLF_PROVIDER_BOOKINGS_F_U1 | Unique | Default | PROVIDER_BOOKING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
