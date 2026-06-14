# IRC_TC_SCREENING_ORDERS

This table contains the screening requests sent to the partner.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcscreeningorders-14328.html#irctcscreeningorders-14328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcscreeningorders-14328.html#irctcscreeningorders-14328)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_SCREENING_ORDERS_PK | TC_ORDER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TC_ORDER_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| APP_DRAFT_ID | NUMBER |  | 18 |  | Foreign key value to IRC_CX_APP_DRAFTS table. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Foreign key value to IRC_SUBMISSIONS table. |
| TC_REQ_PACKAGE_ID | NUMBER |  | 18 | Yes | Foreign key value to IRC_TC_REQ_PACKAGES table. |
| ORDER_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the order type code of the tax credits package. |
| ORDER_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the order status code of the tax credits package. |
| REQUESTED_BY | VARCHAR2 | 60 |  |  | Stores the user who triggered the tax credit package for the submission. |
| REQUESTED_DATE | TIMESTAMP |  |  |  | Stores the date on which the tax credit package was triggered for the submission. |
| RETRY_COUNT | NUMBER |  | 4 |  | This column stores the number of failed tries made to invoke the partner service. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_SCREENING_ORDERS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_TC_SCREENING_ORDERS_FK2 | Non Unique | Default | TC_REQ_PACKAGE_ID |
| IRC_TC_SCREENING_ORDERS_FK3 | Non Unique | Default | APP_DRAFT_ID |
| IRC_TC_SCREENING_ORDERS_N1 | Non Unique | Default | ORDER_TYPE_CODE, ORDER_STATUS_CODE, SUBMISSION_ID |
| IRC_TC_SCREENING_ORDERS_N2 | Non Unique | Default | ORDER_STATUS_CODE, RETRY_COUNT |
| IRC_TC_SCREENING_ORDERS_PK | Unique | Default | TC_ORDER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
