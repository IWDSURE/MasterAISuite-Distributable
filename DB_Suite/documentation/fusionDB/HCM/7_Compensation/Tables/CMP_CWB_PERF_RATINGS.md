# CMP_CWB_PERF_RATINGS

Stores rating given by managers to employees to recognize their performance.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbperfratings-22700.html#cmpcwbperfratings-22700](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbperfratings-22700.html#cmpcwbperfratings-22700)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PERF_RATINGS_PK | PERF_RATING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERF_RATING_ID | NUMBER |  | 18 | Yes | PERF_RATING_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| PERF_DATE | DATE |  |  | Yes | PERF_DATE |
| PERF_RATING | NUMBER |  | 18 |  | PERF_RATING |
| PERF_COMMENTS | CLOB |  |  |  | PERF_COMMENTS |
| PERF_ORIG_UPDATED_BY | NUMBER |  | 18 |  | PERF_ORIG_UPDATED_BY |
| PERF_UPDATE_DATE | DATE |  |  |  | PERF_UPDATE_DATE |
| PERF_UPDATED_BY | NUMBER |  | 18 |  | PERF_UPDATED_BY |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PERF_RATINGS_N1 | Non Unique | Default | PERSON_ID |
| CMP_CWB_PERF_RATINGS_PK | Unique | Default | PERF_RATING_ID |
| CMP_CWB_PERF_RATINGS_U1 | Unique | Default | ASSIGNMENT_ID, PERF_DATE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
