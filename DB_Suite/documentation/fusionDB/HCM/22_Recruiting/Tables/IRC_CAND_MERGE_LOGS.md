# IRC_CAND_MERGE_LOGS

To retrieve the original candidate number of a merged candidate at a given point of time.

Also this table can be reuse for the purpose of auditing of merge candidate action.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandmergelogs-9828.html#irccandmergelogs-9828](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandmergelogs-9828.html#irccandmergelogs-9828)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_MERGE_LOGS_PK | CAND_MERGE_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_MERGE_LOG_ID | NUMBER |  | 18 | Yes | It contains the primary key of the table. Its a auto generated number. |
| ENTITY_ID | NUMBER |  | 18 | Yes | It contains the entitly id from where the audit has been orignated |
| ENTITY_TYPE | VARCHAR2 | 64 |  | Yes | It contains entity type from the module where audit is generated |
| ALPHA_PERSON_ID | NUMBER |  | 18 | Yes | It stores the person id of the candidate which will get retained post merge. |
| ALPHA_CANDIDATE_NUMBER | VARCHAR2 | 30 |  | Yes | It stores the candidate number of the candidate which will get retained post merge. |
| BETA_PERSON_ID | NUMBER |  | 18 | Yes | It stores the person id of the candidate which will get discarded  post merge. |
| BETA_CANDIDATE_NUMBER | VARCHAR2 | 30 |  | Yes | It stores the candidate number of the candidate which will get discarded post merge. |
| BETA_START_DATE | TIMESTAMP |  |  | Yes | Captures start of the time or end of previous same entity end time |
| BETA_END_DATE | TIMESTAMP |  |  | Yes | It contains the timestamp when beta candidate entity was discarded. |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | Type of the action like ORA_MERGED or ORA_DELETED |
| ADDITIONAL_INFO | CLOB |  |  |  | Optional field to persist the logs |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_MERGE_LOGS_PK | Unique | Default | CAND_MERGE_LOG_ID |
| IRC_CAND_MERGE_LOGS_U1 | Unique | Default | ALPHA_PERSON_ID, ENTITY_ID, ENTITY_TYPE, BETA_PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
