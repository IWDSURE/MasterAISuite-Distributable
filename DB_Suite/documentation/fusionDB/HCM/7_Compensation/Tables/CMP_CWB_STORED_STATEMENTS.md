# CMP_CWB_STORED_STATEMENTS

Stores all relevant data of workers statements processed

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbstoredstatements-22110.html#cmpcwbstoredstatements-22110](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbstoredstatements-22110.html#cmpcwbstoredstatements-22110)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_STORED_STATEMENTS_PK | STORED_STMT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STORED_STMT_ID | NUMBER |  | 18 | Yes | STORED_STMT_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| PLAN_ID | NUMBER |  | 18 |  | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 |  | PERIOD_ID |
| STMT_TEMPLATE_ID | NUMBER |  | 18 | Yes | STMT_TEMPLATE_ID |
| STMT_GROUP_ID | NUMBER |  | 18 |  | STMT_GROUP_ID |
| STMT_GROUP_TEMPLATE_ID | NUMBER |  | 18 |  | STMT_GROUP_TEMPLATE_ID |
| PERSON_STMT_ID | NUMBER |  | 18 | Yes | PERSON_STMT_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| STMT_RUN_REQUEST_ID | NUMBER |  | 18 |  | STMT_RUN_REQUEST_ID |
| STMT_EXPIRATION_DATE | DATE |  |  |  | STMT_EXPIRATION_DATE |
| STMT_TEMPLATE_NAME | VARCHAR2 | 80 |  |  | STMT_TEMPLATE_NAME |
| STMT_OUTPUT_FORMAT | VARCHAR2 | 30 |  |  | STMT_OUTPUT_FORMAT |
| STMT_VISIBILITY | VARCHAR2 | 30 |  |  | STMT_VISIBILITY |
| ALLOW_STAGGERED_STMT_RELEASE | VARCHAR2 | 1 |  |  | ALLOW_STAGGERED_STMT_RELEASE |
| STMT_RELEASED_BY_MANAGER | VARCHAR2 | 1 |  |  | STMT_RELEASED_BY_MANAGER |
| STMT_ACK_ACTION | VARCHAR2 | 30 |  |  | STMT_ACK_ACTION |
| STMT_ACK_RESULT | VARCHAR2 | 30 |  |  | STMT_ACK_RESULT |
| STMT_ACK_DATE | DATE |  |  |  | STMT_ACK_DATE |
| STMT_STORED_BY | VARCHAR2 | 64 |  |  | STMT_STORED_BY |
| STMT_STORED_DATE | TIMESTAMP |  |  |  | STMT_STORED_DATE |
| WORKER_NOTIFIED_FLAG | VARCHAR2 | 1 |  |  | WORKER_NOTIFIED_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| STMT_ACK_TIMING | VARCHAR2 | 1 |  |  | STMT_ACK_TIMING |
| STMT_VIEWED_DATE | TIMESTAMP |  |  |  | STMT_VIEWED_DATE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_STORED_STATEMENTS_PK | Unique | Default | STORED_STMT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
