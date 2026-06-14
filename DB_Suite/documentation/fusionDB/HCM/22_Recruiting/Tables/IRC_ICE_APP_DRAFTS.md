# IRC_ICE_APP_DRAFTS

This table contains the data about the draft application information and it is for internal candidates only.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irciceappdrafts-30655.html#irciceappdrafts-30655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irciceappdrafts-30655.html#irciceappdrafts-30655)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ICE_APP_DRAFTS_PK | ICE_APP_DRAFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ICE_APP_DRAFT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CANDIDATES table. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the object. |
| CONTENT | CLOB |  |  |  | Stores JSON payload for the application draft. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ICE_APP_DRAFTS_FK1 | Non Unique | Default | PERSON_ID |
| IRC_ICE_APP_DRAFTS_FK2 | Non Unique | Default | REQUISITION_ID |
| IRC_ICE_APP_DRAFTS_PK | Unique | Default | ICE_APP_DRAFT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
