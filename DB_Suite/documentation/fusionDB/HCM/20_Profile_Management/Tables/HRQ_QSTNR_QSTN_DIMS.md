# HRQ_QSTNR_QSTN_DIMS

The Questions that make up a Dimension and their relative weighting used to calculate the Dimension score.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrqstndims-28067.html#hrqqstnrqstndims-28067](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrqstndims-28067.html#hrqqstnrqstndims-28067)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_QSTN_DIMS_PK | QSTNR_QSTN_DIM_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| QSTNR_QSTN_DIM_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire question dimension.  System generated id.  This attribute combined with business group id forms the primary key. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| QSTNR_QUESTION_ID | NUMBER |  | 18 |  | Identifies the questionnaire question id. |  |
| QSTNR_DIMENSION_ID | NUMBER |  | 18 |  | Identifies the questionnaire dimension id. |  |
| WEIGHT | NUMBER |  | 18 |  | Identifies the weight of the question. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_QSTN_DIMS_PK | Unique | Default | QSTNR_QSTN_DIM_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
