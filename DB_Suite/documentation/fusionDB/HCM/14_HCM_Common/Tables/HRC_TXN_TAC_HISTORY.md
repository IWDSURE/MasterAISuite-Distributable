# HRC_TXN_TAC_HISTORY

This table is for storing the details of actions happened on transactions

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxntachistory-13496.html#hrctxntachistory-13496](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxntachistory-13496.html#hrctxntachistory-13496)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_txn_tac_history_PK | HISTORYID |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| HISTORYID | VARCHAR2 | 50 | Yes | The primary key to the current table. |
| TRANSACTION_ID | NUMBER |  | Yes | Foreign Key to HRC_TXN_HEADER table |
| ACTION | VARCHAR2 | 200 |  | Action performed by administrator from Transaction Admin Console (e.g. Recover, Terminate etc.) |
| ACTION_BY | VARCHAR2 | 64 |  | Who Column: for storing the username of person responsible for action |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| ACTION_DATE | TIMESTAMP |  |  | Who column: For storing the action date |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_TAC_HISTORY_N1 | Non Unique | Default | TRANSACTION_ID |
| hrc_txn_tac_history_U1 | Unique | Default | HISTORYID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
