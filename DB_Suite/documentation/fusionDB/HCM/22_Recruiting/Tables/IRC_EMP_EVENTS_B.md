# IRC_EMP_EVENTS_B

This is the base table to store the employee event basic details

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventsb-17574.html#ircempeventsb-17574](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircempeventsb-17574.html#ircempeventsb-17574)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_EMP_EVENTS_B_PK | EMP_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EMP_EVENT_ID | NUMBER |  | 18 | Yes | Primary key of the table. Auto generated. |
| EVENT_NUMBER | VARCHAR2 | 64 |  | Yes | The unique number which gets generated to represent an employee event. |
| START_DATE | TIMESTAMP |  |  |  | Stores the start date of the employee event. |
| END_DATE | TIMESTAMP |  |  |  | Stores the end date of the employee event. |
| LAST_REGISTER_DATE | TIMESTAMP |  |  |  | Stores the last date of the registration of the employee event. |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Timezone code of the employee event |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the employee event which is configured in HCM_LOOKUP table. The corresponding lookup type is ORA_IRC_EMP_EVENT_STATUS. |
| STATUS_UPDATED_DATE | TIMESTAMP |  |  |  | Date in which the status is changed for the employee event |
| VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Visibility code of the employee event which is configured in HCM_LOOKUP table. The corresponding lookup type is ORA_IRC_EMP_EVENT_VISIBILITY. |
| CREATION_CODE | VARCHAR2 | 30 |  |  | The creation mode of the employee event which is configured in HCM_LOOKUP table. The corresponding lookup type is ORA_IRC_EMP_EVENT_CREATION. |
| EVENT_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Date in which the event details is last modified |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BANNER_IMAGE_URL | VARCHAR2 | 2048 |  |  | URL of the banner image selected by the user |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_EMP_EVENTS_B_N1 | Non Unique | Default | START_DATE |
| IRC_EMP_EVENTS_B_N2 | Non Unique | Default | STATUS_CODE |
| IRC_EMP_EVENTS_B_PK | Unique | Default | EMP_EVENT_ID |
| IRC_EMP_EVENTS_B_U1 | Unique | Default | EVENT_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
