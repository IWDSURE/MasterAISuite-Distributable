# HWR_POST_CON_STATUS

Table to save the skill scoring check points.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** HWR_POST_CON_STATUS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpostconstatus-30574.html#hwrpostconstatus-30574](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpostconstatus-30574.html#hwrpostconstatus-30574)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_POST_CON_STATUS_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| STATUS | VARCHAR2 | 256 |  |  | The status of last skill scoring, completed or in progress. |
| LOAD_TYPE | VARCHAR2 | 256 |  | Yes | Indicates if it is incremental or topic ID. |
| LAST_RUN_TIME | TIMESTAMP |  |  |  | The last time skill scoring has ran. |
| LAST_STATEMENT_TIME | TIMESTAMP |  |  |  | The time stamp of the last loaded statement. |
| LAST_TOPIC_ID | NUMBER |  | 18 |  | The ID of the last loaded skill topic. |
| JOB_ID | NUMBER |  | 18 |  | The ESS job ID. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_POST_CON_STATUS_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
