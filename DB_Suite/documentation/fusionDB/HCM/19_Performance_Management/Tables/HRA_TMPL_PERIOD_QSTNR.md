# HRA_TMPL_PERIOD_QSTNR

This table stores the questionnaire to be used for each role and for each template period.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplperiodqstnr-10217.html#hratmplperiodqstnr-10217](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplperiodqstnr-10217.html#hratmplperiodqstnr-10217)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_TMPL_PERIOD_QSTNR_PK | TMPL_PERIOD_QSTNR_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TMPL_PERIOD_QSTNR_ID | NUMBER |  | 18 | Yes | Primary Key |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Stores the Business Group |  |
| TMPL_PERIOD_ID | NUMBER |  | 18 | Yes | Foreign Key reference to HRA_TMPL_PERIODS_VL |  |
| SECTION_ID | NUMBER |  | 18 | Yes | Foreign key reference to HRA_TMPL_SECTIONS |  |
| TMPL_ROLE_ID | NUMBER |  | 18 | Yes | Foreign key reference to HRA_TMPL_ROLES |  |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Stores the questionnaire to be used by the role |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_TMPL_PERIOD_QSTNR_PK | Unique | Default | TMPL_PERIOD_QSTNR_ID, BUSINESS_GROUP_ID |
| HRA_TMPL_PERIOD_QSTNR_UK1 | Unique | Default | TMPL_PERIOD_ID, SECTION_ID, TMPL_ROLE_ID, QUESTIONNAIRE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
