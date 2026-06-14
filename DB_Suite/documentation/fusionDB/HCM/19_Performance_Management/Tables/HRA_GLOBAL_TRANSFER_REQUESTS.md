# HRA_GLOBAL_TRANSFER_REQUESTS

This table stores the global transfer request related to performance management as a result of GHR global transfer process.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** hra_global_transfer_requests

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraglobaltransferrequests-11068.html#hraglobaltransferrequests-11068](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraglobaltransferrequests-11068.html#hraglobaltransferrequests-11068)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_GBL_TRANSFER_REQUESTS_PK | GLOBAL_TRANSFER_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GLOBAL_TRANSFER_REQUEST_ID | NUMBER |  | 18 | Yes | Stores the primary key of the global transfer request. |
| REQUEST_HEADER_ID | NUMBER |  | 18 |  | Stores the primary key of the GHR global transfer request. |
| PERSON_ID | NUMBER |  | 18 |  | Stores the worker person identifier of the global transfer request. |
| OLD_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the old worker assignment identifier of the global transfer request. |
| NEW_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the new worker assignment identifier of the global transfer request. |
| NEW_MANAGER_ID | NUMBER |  | 18 |  | Stores the new manager person identifier of the global transfer request. |
| NEW_MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the new manager assignment identifier of the global transfer request. |
| REQUEST_EFFECTIVE_DATE | DATE |  |  |  | Stores the effective date of the global transfer request. |
| ALL_REVIEW_PERIODS | VARCHAR2 | 20 |  |  | Indicate the review period option of the global transfer request. |
| REVIEW_PERIOD_IDS | VARCHAR2 | 4000 |  |  | Stores the list of review period identifiers of the global transfer request. |
| MGR_OF_NEW_LINE_MGR | VARCHAR2 | 20 |  |  | Indicate whether the submitter is the manager of new line manager of the global transfer request. |
| MODULE_IDENTIFIER | VARCHAR2 | 80 |  |  | Stores the module identifier of the global transfer request. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_GBL_TRANSFER_REQUESTS_PK | Unique | HRA_GBL_TRANSFER_REQUESTS_PK | GLOBAL_TRANSFER_REQUEST_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
