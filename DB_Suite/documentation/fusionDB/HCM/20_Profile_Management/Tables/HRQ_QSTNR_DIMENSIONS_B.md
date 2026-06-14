# HRQ_QSTNR_DIMENSIONS_B

A list of Dimensions in a Questionnaire with a relative weighting for each used to calculate the overall score.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrdimensionsb-26799.html#hrqqstnrdimensionsb-26799](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrdimensionsb-26799.html#hrqqstnrdimensionsb-26799)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_DIMENSIONS_B_PK | QSTNR_DIMENSION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| QSTNR_DIMENSION_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire dimension.  System generated id.  This attribute combined with business group id forms the primary key. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Identifies the questionnaire id. |  |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | Identifies the version number of the questionnaire. |  |
| VERSION_NUMBER | NUMBER |  | 18 |  | Identifies the version number of the questionnaire dimension. |  |
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
| HRQ_QSTNR_DIMENSIONS_B_PK | Unique | Default | QSTNR_DIMENSION_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
