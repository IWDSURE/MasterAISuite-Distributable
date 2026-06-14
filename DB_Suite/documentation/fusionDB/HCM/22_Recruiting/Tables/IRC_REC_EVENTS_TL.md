# IRC_REC_EVENTS_TL

Translation table for event details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventstl-12764.html#ircreceventstl-12764](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreceventstl-12764.html#ircreceventstl-12764)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REC_EVENTS_TL_PK | EVENT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ID | NUMBER |  | 18 | Yes | Part of the Primary key for this table. Foreign Key to IRC_REC_EVENTS_B table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| EVENT_NAME | VARCHAR2 | 240 |  |  | This field stores the name of the Event. |
| EVENT_DESCRIPTION | CLOB |  |  |  | Stores the html-free version of the description for this event |
| EVENT_DESC_HTML | CLOB |  |  |  | Stores the html version of the description for this event |
| EVENT_SHORT_DESC | CLOB |  |  |  | Stores the short event description |
| EVENT_PURPOSE | VARCHAR2 | 500 |  |  | Stores the purpose of the event. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| EVENT_NOTES | VARCHAR2 | 1000 |  |  | Can be stored any information related to the events. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REC_EVENTS_TL_PK | Unique | Default | EVENT_ID, LANGUAGE |
| IRC_REC_EVENTS_TL_U1 | Unique | Default | EVENT_ID, LANGUAGE, EVENT_NAME |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
