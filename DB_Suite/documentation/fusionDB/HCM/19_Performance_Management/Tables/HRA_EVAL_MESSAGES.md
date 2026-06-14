# HRA_EVAL_MESSAGES

This table stores the validation messages of performance documents as a result of Mass Evaluation Submit Process.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** hra_eval_messages

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalmessages-19239.html#hraevalmessages-19239](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalmessages-19239.html#hraevalmessages-19239)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_MESSAGES_PK | EVAL_MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVAL_MESSAGE_ID | NUMBER |  | 18 | Yes | Stores the primary key of the performance document validation messages. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| EVALUATION_ID | NUMBER |  | 18 |  | Stores the document identifier of the performance document validation messages. |
| MANAGER_ID | NUMBER |  | 18 |  | Stores the manager identifier of the performance document validation messages. |
| TMPL_PERIOD_ID | NUMBER |  | 18 |  | Stores the template period identifier of the performance document validation messages. |
| EVAL_PARTICIPANT_ID | NUMBER |  | 18 |  | Stores the participant identifier in the document. |
| TMPL_SECTION_ID | NUMBER |  | 18 |  | Stores the template section identifier of the performance document validation messages. |
| EVAL_SECTION_ID | NUMBER |  | 18 |  | Stores the document section identifier of the performance document validation messages. |
| SECTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the document section type code identifier of the performance document validation messages. |
| MESSAGE_LEVEL | VARCHAR2 | 30 |  |  | Stores the validation message level of the performance document validation messages. |
| MESSAGE_TYPE | VARCHAR2 | 30 |  |  | Stores the validation message type of the performance document validation messages. |
| MESSAGE_CODE | VARCHAR2 | 30 |  |  | Stores the validation message code of the performance document validation messages. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_MESSAGES_N1 | Non Unique | HRA_EVAL_MESSAGES_N1 | EVALUATION_ID, TMPL_SECTION_ID |
| HRA_EVAL_MESSAGES_N2 | Non Unique | HRA_EVAL_MESSAGES_N2 | MANAGER_ID, TMPL_PERIOD_ID |
| HRA_EVAL_MESSAGES_PK | Unique | Default | EVAL_MESSAGE_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
