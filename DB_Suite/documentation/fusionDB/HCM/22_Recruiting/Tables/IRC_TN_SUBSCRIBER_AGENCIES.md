# IRC_TN_SUBSCRIBER_AGENCIES

This is the table for storing subscriber agencies information on Talent Network.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnsubscriberagencies-21970.html#irctnsubscriberagencies-21970](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnsubscriberagencies-21970.html#irctnsubscriberagencies-21970)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_SUBSCRIBER_AGENCIES_PK | SUBSCRIBER_AGENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBSCRIBER_AGENCY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | To store the subscriber id. Foreign Key to IRC_TN_SUBSCRIBERS. |
| AGENCY_ID | NUMBER |  | 18 | Yes | To store the agency_id.Foreign key to IRC_AGENCIES. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_SUBSCRIBER_AGENCIES_FK1 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_SUBSCRIBER_AGENCIES_FK2 | Non Unique | Default | AGENCY_ID |
| IRC_TN_SUBSCRIBER_AGENCIES_PK | Unique | Default | SUBSCRIBER_AGENCY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
