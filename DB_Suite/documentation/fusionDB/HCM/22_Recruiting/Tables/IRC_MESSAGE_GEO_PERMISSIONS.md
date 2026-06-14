# IRC_MESSAGE_GEO_PERMISSIONS

This table stores message allowed countries with throttling limits

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagegeopermissions-8539.html#ircmessagegeopermissions-8539](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmessagegeopermissions-8539.html#ircmessagegeopermissions-8539)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MESSAGE_GEO_PERMISSIONS_PK | IRC_MESSAGE_GEO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IRC_MESSAGE_GEO_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| PHONE_COUNTRY_CODE | VARCHAR2 | 30 |  | Yes | Country prefix for international phone numbers including area code, such as 33 for France |
| THROTTLE_LIMIT | NUMBER |  |  |  | Maximum number of outbound SMS or WhatsApp messages in a day for this country |
| CHANNEL_TYPE_CODE | VARCHAR2 | 30 |  |  | The code for the channel such as SMS, email, whatsapp etc., that is used to send the message to the person. Lookup codes of type 'ORA_IRC_INTERACTION_TYPE'. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MESSAGE_GEO_PERMISSIONS_N1 | Non Unique | Default | PHONE_COUNTRY_CODE, CHANNEL_TYPE_CODE |
| IRC_MESSAGE_GEO_PERMISSIONS_PK | Unique | Default | IRC_MESSAGE_GEO_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
