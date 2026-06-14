# IRC_TC_CAND_ADDL_RESULTS

This table contains additional (other) tax credits break down results for the submissions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctccandaddlresults-5679.html#irctccandaddlresults-5679](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctccandaddlresults-5679.html#irctccandaddlresults-5679)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_CAND_ADDL_RESULTS_PK | TC_ADDL_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TC_ADDL_RESULT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| TC_PKG_RESULT_ID | NUMBER |  | 18 | Yes | Foreign key value to IRC_TC_CAND_PKG_RESULTS table. |
| CREDITS_NAME | VARCHAR2 | 240 |  |  | Specifies the tax credits name. |
| CREDITS_IDENTIFIER | VARCHAR2 | 60 |  |  | Specifies the tax credit Identifier. |
| CREDITS_ELIGIBLE_FLAG | VARCHAR2 | 1 |  |  | Specifies if the candidate eligible for this tax credit. |
| CREDITS_ESTIMATE | NUMBER |  |  |  | Specifies the estimated amount for the candidate. |
| CREDITS_EST_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Specifies the currency for estimated amount. |
| SEQUENCE | NUMBER |  | 2 |  | Specifies the sequence of the tax credit component. |
| COMMENTS | CLOB |  |  |  | Comments provided by the partner. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_CAND_ADDL_RESULTS_FK1 | Non Unique | Default | TC_PKG_RESULT_ID |
| IRC_TC_CAND_ADDL_RESULTS_PK1 | Unique | Default | TC_ADDL_RESULT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
