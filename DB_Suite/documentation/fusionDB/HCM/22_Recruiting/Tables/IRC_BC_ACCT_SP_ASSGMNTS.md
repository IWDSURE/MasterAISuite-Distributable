# IRC_BC_ACCT_SP_ASSGMNTS

Stores screening packages associated with BC partner accounts in recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbcacctspassgmnts-8283.html#ircbcacctspassgmnts-8283](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbcacctspassgmnts-8283.html#ircbcacctspassgmnts-8283)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BC_ACCT_SP_ASSGMNTS_PK | ACCT_SP_ASSGMNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCT_SP_ASSGMNT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the object. |
| ACCOUNT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_ACCOUNTS |
| SCR_PKG_CODE | VARCHAR2 | 30 |  |  | Stores the code identifying the screening package assigned to account |
| SCR_PKG_NAME | VARCHAR2 | 500 |  | Yes | Stores the name of the screening package |
| SCR_PKG_DESC | VARCHAR2 | 2000 |  |  | Stores the description of screening package |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BC_ACCT_SP_ASSIGMNTS_FK1 | Non Unique | Default | ACCOUNT_ID |
| IRC_BC_ACCT_SP_ASSIGMNTS_PK | Unique | Default | ACCT_SP_ASSGMNT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
