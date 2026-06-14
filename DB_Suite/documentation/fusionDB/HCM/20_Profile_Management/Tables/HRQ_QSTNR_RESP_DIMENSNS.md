# HRQ_QSTNR_RESP_DIMENSNS

Contains the dimension score calculated for a response.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrrespdimensns-31434.html#hrqqstnrrespdimensns-31434](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrrespdimensns-31434.html#hrqqstnrrespdimensns-31434)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_RESP_DIMENSNS_PK | QSTNR_RESP_DIMENSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_RESP_DIMENSION_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire response dimension.  System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_DIMENSION_ID | NUMBER |  | 18 |  | Identifies the questionnaire dimension id. |
| QSTNR_RESPONSE_ID | NUMBER |  | 18 |  | Identifies the questionnaire response id. |
| SCORE | NUMBER |  | 18 |  | Score calculated for this dimension. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_RESP_DIMENSNS_PK | Unique | Default | QSTNR_RESP_DIMENSION_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
