# HRA_FEEDBACK_RESPONSE

Table to store the feedback provided as a response to feedback requests created for a worker.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrafeedbackresponse-25704.html#hrafeedbackresponse-25704](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrafeedbackresponse-25704.html#hrafeedbackresponse-25704)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_FEEDBACK_RESPONSE_PK | FEEDBACK_RESP_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_RESP_ID | NUMBER |  | 18 | Yes | Primary key of the Feedback Response table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| FEEDBACK_REQ_ID | NUMBER |  | 18 | Yes | Foreign key to Feedback Request table |
| STATUS_CODE | VARCHAR2 | 20 |  |  | Status of the Feedback Response |
| FEEDBACK_COMPLETION_DATE | DATE |  |  |  | Feedback Completion Date |
| REVISION_NEEDED | VARCHAR2 | 30 |  |  | Flag to indicate if feedback provided requires a revision |
| REVISION_COMPLETION_DATE | DATE |  |  |  | Date on which revision is completed |
| REVISION_REQ_MESSAGE | VARCHAR2 | 4000 |  |  | Message sent to participant why the revision is needed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_FEEDBACK_RESPONSE_N1 | Non Unique | Default | FEEDBACK_REQ_ID |
| HRA_FEEDBACK_RESPONSE_U1 | Unique | Default | FEEDBACK_RESP_ID |
| HRA_FEEDBACK_RESPONSE_U2 | Unique | Default | FEEDBACK_RESP_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
