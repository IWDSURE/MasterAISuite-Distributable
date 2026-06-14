# IRC_JD_REQ_POSTINGS

Stores postings to JD partners for a requisition

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjdreqpostings-13690.html#ircjdreqpostings-13690](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjdreqpostings-13690.html#ircjdreqpostings-13690)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JD_REQ_POSTINGS_PK | POSTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSTING_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISIONINGS |
| JD_ERROR_DESC | VARCHAR2 | 1000 |  |  | Stores the overall error detail from JD partner |
| POSTED_BY | VARCHAR2 | 64 |  | Yes | Stores the user who initiated request for posting. |
| POSTED_DATE | DATE |  |  | Yes | Stores the posting date for the requisition from JD partner |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JD_REQ_POSTINGS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_JD_REQ_POSTINGS_FK2 | Non Unique | Default | PROVISIONING_ID |
| IRC_JD_REQ_POSTINGS_PK | Unique | Default | POSTING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
