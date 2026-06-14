# IRC_TP_PARTNER_ACCOUNTS

Stores partner accounts for third party integration in recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctppartneraccounts-11927.html#irctppartneraccounts-11927](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctppartneraccounts-11927.html#irctppartneraccounts-11927)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TP_PARTNER_ACCOUNTS_PK | ACCOUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCOUNT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| USERNAME | VARCHAR2 | 100 |  | Yes | Stores the username for this partner account |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Stores the description for this partner account |
| USER_SALTED_HASH | VARCHAR2 | 512 |  |  | Stores the salted hash of password for this partner account |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether account is active |
| VALIDATE_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating if partner account is valid |
| LAST_VALIDATE_DATE | TIMESTAMP |  |  |  | Stores the date and time when the account was last validated |
| DEFAULT_FLAG | VARCHAR2 | 1 |  | Yes | Stores the flag indicating whether this is default account for partner |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TP_PARTNER_ACCOUNTS_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_TP_PARTNER_ACCOUNTS_PK | Unique | Default | ACCOUNT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
