# HRT_CHANNEL_MESSAGE_ACCESS

Stores the details of access provided on channel messages.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtchannelmessageaccess-3896.html#hrtchannelmessageaccess-3896](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtchannelmessageaccess-3896.html#hrtchannelmessageaccess-3896)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CHANNEL_MESSAGE_ACCES_PK | MESSAGE_ACCESS_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ACCESS_ID | NUMBER |  | 18 | Yes | The system generated surrogate key for this entry. |
| MESSAGE_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_CHANNEL_MESSAGES |
| SHARED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign key to  PER_ALL_PEOPLE_F, which represents the person who shared the message. |
| SHARED_WITH_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F, which represents the person who received access on the message. |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | Object for which messages are stored |
| OBJECT_ID | NUMBER |  | 18 |  | Object id for which results are stored |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CHANNEL_MESSAGE_ACCESS_N1 | Non Unique | Default | MESSAGE_ID, SHARED_WITH_PERSON_ID |
| HRT_CHANNEL_MESSAGE_ACCESS_N2 | Non Unique | Default | MESSAGE_ID, OBJECT_TYPE, OBJECT_ID |
| HRT_CHANNEL_MESSAGE_ACCESS_U1 | Unique | Default | MESSAGE_ACCESS_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
