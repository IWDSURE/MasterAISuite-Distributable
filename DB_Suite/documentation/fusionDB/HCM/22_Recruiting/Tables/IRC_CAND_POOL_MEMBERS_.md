# IRC_CAND_POOL_MEMBERS_

This table contains information on candidate pool members.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolmembers-8294.html#irccandpoolmembers-8294](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolmembers-8294.html#irccandpoolmembers-8294)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_POOL_MEMBERS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, POOL_MEMBER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_MEMBER_ID | NUMBER |  | 18 | Yes | Primary key of the table and also foreign Key to HRT_POOL_MEMBERS. |
| POOL_ID | NUMBER |  | 18 |  | Foreign key to HRT_POOLS_B table. |
| CURRENT_PHASE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PHASES_B table. |
| CURRENT_STATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_STATES_B table. |
| PROCESS_INSTANCE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PROCESSES_B table. |
| PROCESS_TEMPLATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PROCESSES_B table. |
| LAST_ADD_TO_REQ_DATE | DATE |  |  |  | Stores the date when the Candidate has been added to a requisition for the last time in regards to that Pool. |
| LAST_SYNC_DATE | TIMESTAMP |  |  |  | Column to store the last Sync Date Time |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATED_BY_PERSON_ID | NUMBER |  | 18 |  | Who column: indicates the user personid who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_POOL_MEMBERSN1_ | Non Unique | Default | POOL_MEMBER_ID, LAST_UPDATE_DATE |
| IRC_CAND_POOL_MEMBER_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, POOL_MEMBER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
