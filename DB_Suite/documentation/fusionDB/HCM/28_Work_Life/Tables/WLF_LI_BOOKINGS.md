# WLF_LI_BOOKINGS

Table to store details of activity bookings

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflibookings-31613.html#wlflibookings-31613](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflibookings-31613.html#wlflibookings-31613)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_BOOKINGS_PK | BOOKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BOOKING_ID | NUMBER |  | 18 | Yes | Booking Id pk |
| BOOKING_NUMBER | VARCHAR2 | 30 |  |  | UserKey for uniquely identifying Learning Booking. |
| ADHOC_ITEM_DESC | VARCHAR2 | 4000 |  |  | ADHOC Resource Description |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | Activity learning item id |
| BOOKED_ITEM_TYPE | VARCHAR2 | 30 |  |  | Indicates what type of booked item this is (resource, person, etc) |
| BOOKED_ITEM_ID | NUMBER |  | 18 |  | Can be a resource_id or person_id |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | Primary Flag |
| ADHOC_ITEM_NAME | VARCHAR2 | 100 |  |  | Adhoc resource name |
| ADHOC_ITEM_QUANTITY | NUMBER |  |  |  | ADHOC_ITEM_QUANTITY |
| HOST_URL | VARCHAR2 | 1000 |  |  | Vilt host url value |
| VILT_PRODUCT | VARCHAR2 | 30 |  |  | Webex product type |
| VILT_CALL_TIME | TIMESTAMP |  |  |  | Vilt call timestamp |
| VILT_CALL_STATUS | VARCHAR2 | 30 |  |  | Vilt call status |
| VILT_CALL_LOG | VARCHAR2 | 1000 |  |  | Vilt call log |
| SESSION_KEY | VARCHAR2 | 30 |  |  | Session key |
| RECORDING_LOCATION | VARCHAR2 | 1000 |  |  | URL for the recording of the meeting |
| OPEN_TIME | NUMBER |  |  |  | The amount of time before the meeting starts in which the VILT learner can join the meeting |
| RECORDING_FLAG | VARCHAR2 | 1 |  |  | Indicates if the VILT ACCOUNT associated to the ILT activity has recordings or not. Y/N value |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Indicates if record is processed to security index or not |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_BOOKINGS_FK1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_BOOKINGS_N1 | Non Unique | Default | BOOKED_ITEM_ID, BOOKED_ITEM_TYPE |
| WLF_LI_BOOKINGS_N2 | Non Unique | Default | BOOKING_NUMBER |
| WLF_LI_BOOKINGS_U1 | Unique | Default | BOOKING_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
