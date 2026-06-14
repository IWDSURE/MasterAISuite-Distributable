# IRC_TN_JOB_AGENCY_ACTIONS

This is the table for storing job information requests by an agency on Talent Network.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobagencyactions-24271.html#irctnjobagencyactions-24271](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobagencyactions-24271.html#irctnjobagencyactions-24271)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_AGENCY_ACTIONS_PK | TN_JOB_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_ACTION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| TN_JOB_ID | NUMBER |  | 18 | Yes | To store the TN job id. Foreign Key to IRC_TN_JOBS_VL. |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agent. Foreign key to IRC_AGENCIES table. |
| AGENT_ID | NUMBER |  | 18 | Yes | Stores the AGENT_ID of the Agent. Foreign key to IRC_AGENTS table. |
| ACTION_CODE | VARCHAR2 | 30 |  | Yes | Stores the action performed by the Agency. ORA_COMPLETE/ ORA_PENDING_INFO or ORA_REJECTED |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_AGENCY_ACTIONS_FK1 | Non Unique | Default | TN_JOB_ID |
| IRC_TN_JOB_AGENCY_ACTIONS_FK2 | Non Unique | Default | AGENCY_ID |
| IRC_TN_JOB_AGENCY_ACTIONS_FK3 | Non Unique | Default | AGENT_ID |
| IRC_TN_JOB_AGENCY_ACTIONS_PK | Unique | Default | TN_JOB_ACTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
