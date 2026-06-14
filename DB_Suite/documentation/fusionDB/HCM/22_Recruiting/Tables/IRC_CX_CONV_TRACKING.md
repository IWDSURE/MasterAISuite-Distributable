# IRC_CX_CONV_TRACKING

Stores user conversation request and response tracking information in the career coach orchestration layers

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxconvtracking-17334.html#irccxconvtracking-17334](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxconvtracking-17334.html#irccxconvtracking-17334)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_CONV_TRACKING_PK | CONVERSATION_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONVERSATION_LOG_ID | NUMBER |  | 18 | Yes | Unique Identifier for the conversation tracking. System generated value |
| USER_REQUEST_ID | VARCHAR2 | 240 |  | Yes | Unique user request identifier for the user conversation on career site. |
| CONVERSATION_ID | VARCHAR2 | 240 |  |  | Conversation identifier sent in the initial request |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Indicates the site where the request is received. |
| CANDIDATE_NUMBER | VARCHAR2 | 30 |  |  | Readable number generated for Candidate used in the site. |
| SESSION_ID | VARCHAR2 | 240 |  |  | Unique identifier for the user session |
| TRACE_ID | VARCHAR2 | 240 |  |  | Trace identifier received in the response |
| JOB_ID | VARCHAR2 | 240 |  |  | Job identifier received in the response |
| WORKFLOW_CODE | VARCHAR2 | 30 |  | Yes | Identifier for the conversation workflow code |
| WORKFLOW_VERSION | NUMBER |  | 9 |  | Workflow version used in the request |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_CONV_TRACKING_N1 | Non Unique | Default | USER_REQUEST_ID, CONVERSATION_ID |
| IRC_CX_CONV_TRACKING_N2 | Non Unique | Default | USER_REQUEST_ID, JOB_ID |
| IRC_CX_CONV_TRACKING_PK | Unique | Default | CONVERSATION_LOG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
