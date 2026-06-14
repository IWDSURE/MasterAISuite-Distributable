# HRQ_QSTNR_SECTIONS_B

Questions within a questionnaire are grouped into sections.Even if sections are not being used (which is an option on the questionnaire template), one Section will still be created automatically.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrsectionsb-25041.html#hrqqstnrsectionsb-25041](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrsectionsb-25041.html#hrqqstnrsectionsb-25041)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_SECTIONS_B_PK | QSTNR_SECTION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_SECTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a section on a questionnaire.  System generated id.  This attribute combined with business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Identifies the questionnaire id. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | Identifies the questionnaire's version number. |
| SECTION_SEQ_NUM | NUMBER |  | 18 |  | Identifies the sequence number of the questionnaire section. |
| NEW_PAGE | VARCHAR2 | 30 |  |  | Identifies if this section starts in a new page. |
| QUESTION_ORDER | VARCHAR2 | 30 |  |  | Identifies the order of the question (random or fixed). |
| RESPONSE_ORDER | VARCHAR2 | 30 |  |  | Identifies the order of the response list (random or fixed). |
| MANDATORY | VARCHAR2 | 30 |  |  | Identifies if this questionnaire section is mandatory. |
| ALLOW_ADHOC | VARCHAR2 | 30 |  |  | Identifies if this questionnaire section allows adhoc questions. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| RANDOM_SAMPLE_ALL_FLAG | VARCHAR2 | 30 |  |  | Flag Representing whether the random sampling includes all questions in a particular section, or a particular specified in column RANDOM_SAMPLE_SIZE. Possible Values ( "Y"/ "N" ) |
| RANDOM_SAMPLE_SIZE | NUMBER |  | 18 |  | Number representing the random sample size for the number of Questions to be presented in a section |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_SECTIONS_B_PK | Unique | Default | QSTNR_SECTION_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRQ_QSTNR_SECTIONS_B_PK1 | Unique | Default | QSTNR_SECTION_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |
| HRQ_QSTNR_SECTIONS_B_U1 | Unique | Default | BUSINESS_GROUP_ID, QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, QSTNR_SECTION_ID, ORA_SEED_SET1 |
| HRQ_QSTNR_SECTIONS_B_U11 | Unique | Default | BUSINESS_GROUP_ID, QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, QSTNR_SECTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
