# HRQ_QSTNR_TEMPLATES_B

Questionnaire Templates provide options to configure different types of questionnaires to fit to particular circumstances.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrtemplatesb-27413.html#hrqqstnrtemplatesb-27413](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrtemplatesb-27413.html#hrqqstnrtemplatesb-27413)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_TEMPLATES_VL_PK | QSTNR_TEMPLATE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_TEMPLATE_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire template.  System generated id.  This attribute combined with business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Identifies the questionnaire id. |
| ALLOW_FORMAT_CHG | VARCHAR2 | 30 |  |  | Identifies if the format of the questionnaire can be changed. |
| ALLOW_INTRO_CHG | VARCHAR2 | 30 |  |  | Identifies if the introduction of the questionnaire can be changed. |
| ALLOW_SECTION_CHG | VARCHAR2 | 30 |  |  | Identifies if a section of the questionnaire can be changed. |
| ALLOW_QSTN_ORDER_CHG | VARCHAR2 | 30 |  |  | Identifies if the question order of the questionnaire can be changed. |
| ALLOW_RESP_ORDER_CHG | VARCHAR2 | 30 |  |  | Identifies if the response order of the questionnaire can be changed. |
| BASIC_SETUP_FLAG | VARCHAR2 | 30 |  |  | Display the basic elements in the UI |
| RANDOM_QSTNS | VARCHAR2 | 30 |  |  | Identifies if the questions will be presented in random order. |
| RANDOM_ANSWERS | VARCHAR2 | 30 |  |  | Identifies if the answers will be presented in random order. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QSTNR_TEMPLATES_B_PK | Unique | Default | QSTNR_TEMPLATE_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRQ_QSTNR_TEMPLATES_B_PK1 | Unique | Default | QSTNR_TEMPLATE_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
