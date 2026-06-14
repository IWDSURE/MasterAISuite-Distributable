# HRQ_SUB_QUESTIONS_B

This contains definitions for multi-part questions (i.e. for Question Types of ???Matching??? and  ???Fill in the blanks???)

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqsubquestionsb-18687.html#hrqsubquestionsb-18687](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqsubquestionsb-18687.html#hrqsubquestionsb-18687)

## Primary Key

| Name | Columns |
|------|----------|
| SUB_QUESTIONS_B_PK | SUB_QUESTION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUB_QUESTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a sub question.  System generated id.  This attribute combined with the business group id forms the primary key. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| QUESTION_ID | NUMBER |  | 18 | Yes | Identifies the question id. |  |
| QSTN_VERSION_NUM | NUMBER |  | 18 |  | Identifies the version number of the question. |  |
| CORRECT_ANSWER_ID | NUMBER |  | 18 |  | Identifies the answer id of the correct answer |  |
| CORRECT_RTG_LVL_ID | NUMBER |  | 18 |  | Identifies the correct rating level id |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
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
| HRQ_SUB_QUESTION_B_PK | Unique | Default | SUB_QUESTION_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
