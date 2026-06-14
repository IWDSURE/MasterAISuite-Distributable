# HRC_TXN_TAC_ESS

Transaction Model table: Table for storing the details of the ess job ran.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxntacess-26289.html#hrctxntacess-26289](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxntacess-26289.html#hrctxntacess-26289)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_txn_tac_ess_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | Unique ID which is used as a primary key |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Indicates Unique identifier of the ess request identifier |
| JOBNAME | VARCHAR2 | 200 |  |  | To distinguish the records based on jobname |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| STARTTIME | TIMESTAMP |  |  |  | Indicates the date and time the transaction ESS job began executing. |
| ENDTIME | TIMESTAMP |  |  |  | Indicates the date and time the transaction ESS job finished executing. |
| TRANSACTIONSPICKED | CLOB |  |  |  | Indicates the transactions handled by the the transaction ESS job. |
| TRANSACTIONSUPDATED | CLOB |  |  |  | Indicates the transactions updated by the the transaction ESS job. |
| LOGS | CLOB |  |  |  | Log files associated with the transaction ESS job run. |
| SUBMITTEDFROM | VARCHAR2 | 20 |  |  | Indicates whether ESS job was run from the ESS Scheduler or manually from the Transaction Console application. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| STATUS | VARCHAR2 | 20 |  |  | Status of the transaction ESS job. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hrc_txn_tac_ess_U1 | Unique | Default | ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
