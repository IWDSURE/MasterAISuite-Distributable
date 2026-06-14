# HRQ_QSTN_ANSWERS_B

This contains a list of possible answers to a question.These answers are for a specific question only.  For generic responses, a Rating Model may be associated with the question instead.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnanswersb-27323.html#hrqqstnanswersb-27323](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnanswersb-27323.html#hrqqstnanswersb-27323)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTN_ANSWERS_B_PK | QSTN_ANSWER_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTN_ANSWER_ID | NUMBER |  | 18 | Yes | Unique identifier for an answer to a question.  System generated id.  This attribute combined with business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QUESTION_ID | NUMBER |  | 18 | Yes | Identifies the question. |
| QSTN_VERSION_NUM | NUMBER |  | 18 |  | The version number of the question. |
| SEQ_NUM | NUMBER |  | 18 |  | Used to determine the Sequence in which the Answers are displayed. |
| CORRECT_FLAG | VARCHAR2 | 30 |  |  | Indicates if this is the Correct Answer to the question. |
| SCORE_WEIGHT | NUMBER |  | 18 |  | Used in calculating the overall assessment score when this answer is selected. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| RATING_LEVEL_ID | NUMBER |  | 18 |  | Identifies the rating level id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SCORE | NUMBER |  | 18 |  | Score for the answer. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ADDL_QSTNR_ID | NUMBER |  | 18 |  | ADDL_QSTNR_ID |
| ADDL_QSTNR_VERSION_NUM | NUMBER |  | 18 |  | ADDL_QSTNR_VERSION_NUM |
| ANSWER_CODE | VARCHAR2 | 240 |  |  | ANSWER_CODE |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTN_ANSWERS_B_N1 | Non Unique | Default | BUSINESS_GROUP_ID, QUESTION_ID, QSTN_VERSION_NUM |
| HRQ_QSTN_ANSWERS_B_N2 | Non Unique | Default | ADDL_QSTNR_ID, ADDL_QSTNR_VERSION_NUM |
| HRQ_QSTN_ANSWERS_B_PK | Unique | Default | QSTN_ANSWER_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRQ_QSTN_ANSWERS_B_PK1 | Unique | Default | QSTN_ANSWER_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
