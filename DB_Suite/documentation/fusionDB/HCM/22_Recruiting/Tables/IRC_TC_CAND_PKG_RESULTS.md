# IRC_TC_CAND_PKG_RESULTS

This table contains the package level tax credits results for the submissions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctccandpkgresults-21454.html#irctccandpkgresults-21454](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctccandpkgresults-21454.html#irctccandpkgresults-21454)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_CAND_PKG_RESULTS_PK | TC_PKG_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TC_PKG_RESULT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| APP_DRAFT_ID | NUMBER |  | 18 |  | Foreign key value to IRC_CX_APP_DRAFTS table. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Foreign key value to IRC_SUBMISSIONS table. |
| TC_REQ_PACKAGE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TC_REQ_PACKAGES table. |
| PACKAGE_CODE | VARCHAR2 | 30 |  |  | Specifies the package code used by the partner |
| PACKAGE_NAME | VARCHAR2 | 500 |  |  | Specifies the package name used by the partner |
| RESULT_STATUS_CODE | VARCHAR2 | 30 |  |  | Status code of the tax credit request. |
| CREDITS_ELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | Specifies if the candidate is eligible for any tax credits. |
| TOTAL_CREDITS_ESTIMATE | NUMBER |  |  |  | Specifies the total tax credits estimate for the candidate. |
| CREDITS_EST_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Specifies the currency for  tax credits estimate. |
| FEDERAL_CREDITS_ELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | Specifies if the candidate is eligible for federal tax credits. |
| FEDERAL_CREDITS_IDENTIFIER | VARCHAR2 | 60 |  |  | Specifies federal tax credits identifier. |
| FEDERAL_CREDITS_ESTIMATE | NUMBER |  |  |  | Specifies federal credits estimate for the candidate. |
| STATE_CREDITS_ELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | Specifies if the candidate is eligible for state tax credits. |
| STATE_CREDITS_IDENTIFIER | VARCHAR2 | 60 |  |  | Specifies state tax credits identifier. |
| STATE_CREDITS_ESTIMATE | NUMBER |  |  |  | Specifies state credits estimate for the candidate. |
| COMMENTS | CLOB |  |  |  | Comments provided by the partner. |
| DRAFT_ADDITIONAL_RESULTS | CLOB |  |  |  | Stores additional results payload for the draft application Tax Credits packages |
| REQUESTED_BY | VARCHAR2 | 60 |  |  | Stores the user who triggered the tax credit package for the submission. |
| REQUESTED_DATE | TIMESTAMP |  |  |  | Stores the date on which the tax credit package was triggered for the submission. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_CAND_PKG_RESULTS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_TC_CAND_PKG_RESULTS_FK2 | Non Unique | Default | TC_REQ_PACKAGE_ID |
| IRC_TC_CAND_PKG_RESULTS_FK3 | Non Unique | Default | APP_DRAFT_ID |
| IRC_TC_CAND_PKG_RESULTS_PK | Unique | Default | TC_PKG_RESULT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
