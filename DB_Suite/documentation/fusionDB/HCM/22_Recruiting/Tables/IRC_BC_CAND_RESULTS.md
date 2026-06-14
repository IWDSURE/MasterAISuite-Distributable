# IRC_BC_CAND_RESULTS

Stores candidate background check results for submissions in recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbccandresults-27084.html#ircbccandresults-27084](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbccandresults-27084.html#ircbccandresults-27084)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BC_CAND_RESULTS_PK | RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESULT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_SUBMISSIONS |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| ACCOUNT_ID | NUMBER |  | 18 |  | Foreign key to IRC_TP_PARTNER_ACCOUNTS |
| REQUESTED_BY | VARCHAR2 | 64 |  |  | Stores the user who intiated the background check screening for submission |
| REQUEST_DATE | DATE |  |  |  | Stores the date the background check screening was initiated for submission |
| BC_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores background check status from partner. The corresponding lookup type is ORA_IRC_BC_RESULT_STATUS |
| BC_ERROR_DESC | CLOB |  |  |  | Stores the error description sent by BC partner |
| BC_COMMENT | CLOB |  |  |  | Stores  comments send by BC partner |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BC_CAND_RESULTS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_BC_CAND_RESULTS_FK2 | Non Unique | Default | PROVISIONING_ID |
| IRC_BC_CAND_RESULTS_FK3 | Non Unique | Default | ACCOUNT_ID |
| IRC_BC_CAND_RESULTS_PK | Unique | Default | RESULT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
