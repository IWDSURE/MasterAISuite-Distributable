# IRC_BLOCKED_CONTACTS

This table stores the blocked contacts for all communication channels in HCM Recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircblockedcontacts-14760.html#ircblockedcontacts-14760](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircblockedcontacts-14760.html#ircblockedcontacts-14760)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BLOCKED_CONTACTS_PK | BLOCKED_CONTACT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BLOCKED_CONTACT_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| CONTACT_INFORMATION | VARCHAR2 | 240 |  | Yes | The communication contact information such as email, phone number, etc., as per channel type code. |
| CHANNEL_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The code for the channel such as SMS, email etc., that is used to send the message to the person. Lookup codes of type 'ORA_IRC_INTERACTION_TYPE'. |
| IS_PATTERN_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the contact information is a pattern matching string |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BLOCKED_CONTACTS_N1 | Non Unique | Default | CHANNEL_TYPE_CODE, IS_PATTERN_FLAG, CONTACT_INFORMATION |
| IRC_BLOCKED_CONTACTS_PK | Unique | Default | BLOCKED_CONTACT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
