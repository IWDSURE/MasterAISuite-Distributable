# IRC_BC_REQ_ACCOUNTS

Stores Partner information at Requisition level .

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbcreqaccounts-22562.html#ircbcreqaccounts-22562](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbcreqaccounts-22562.html#ircbcreqaccounts-22562)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BC_REQ_ACCOUNTS_PK | REQ_ACCOUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_ACCOUNT_ID | NUMBER |  | 18 | Yes | Stores the Primary Key |
| REQUISITION_ID | NUMBER |  | 18 |  | Foreign Key to "irc_requisitions_b" |
| PROVISIONING_ID | NUMBER |  | 18 |  | Foreign Key to "irc_tp_partner_provisngs" |
| ACCOUNT_ID | NUMBER |  | 18 |  | Foreign key to "irc_tp_partner_accounts" |
| MULTIPLE_REQUEST_FLAG | VARCHAR2 | 1 |  |  | Stores the Flag whether recruiter allowed to associate packages at multiple phases. |
| ALLOW_UPDATE_ON_JA_FLAG | VARCHAR2 | 1 |  |  | Stores the Flag to define whether the partner account is editable or not. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BC_REQ_ACCOUNTS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_BC_REQ_ACCOUNTS_FK2 | Non Unique | Default | PROVISIONING_ID |
| IRC_BC_REQ_ACCOUNTS_FK3 | Non Unique | Default | ACCOUNT_ID |
| IRC_BC_REQ_ACCOUNTS_PK | Unique | Default | REQ_ACCOUNT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
