# HRQ_QUESTIONNAIRES_B

Defines a set of questions that participants are to respond to.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionnairesb-31519.html#hrqquestionnairesb-31519](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqquestionnairesb-31519.html#hrqquestionnairesb-31519)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QUESTIONNAIRE_VL_PK | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire.  System generated id.  This attribute combined with the version number and business group id forms the primary key. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | The version number of the questionnaire. This attribute combined with the questionnaire id and business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| STATUS | VARCHAR2 | 30 |  |  | Identifies the status of the questionnaire. |
| QUESTIONNAIRE_CODE | VARCHAR2 | 240 |  |  | Unique identifier for the questionnaire. |
| TEMPLATE_FLAG | VARCHAR2 | 30 |  |  | Indicates if the questionnaire is used as a template. |
| CATEGORY_ID | NUMBER |  | 18 |  | Identifies the category id. |
| SUBSCRIBER_ID | NUMBER |  | 18 |  | Identifies the subscriber id. |
| QSTNR_TEMPLATE_ID | NUMBER |  | 18 |  | Identifies the questionnaire template id. |
| PRIVACY_FLAG | VARCHAR2 | 30 |  |  | Indicates if the questionnaire is Private or Public.  Private questionnaires can only be updated by the owner. |
| UPDATE_ALLOWED | VARCHAR2 | 30 |  |  | Not used |
| OWNER | VARCHAR2 | 64 |  |  | Person Id of the owner of the questionnaire. |
| SECTION_ORDER | VARCHAR2 | 30 |  |  | Order in which sections are displayed (fixed or random). |
| SECTION_PRESENTATION | VARCHAR2 | 30 |  |  | Options for how sections are presented in the UI. |
| PAGE_LAYOUT | VARCHAR2 | 30 |  |  | Options for how questions are presented in the UI. |
| QSTNS_PER_PAGE | NUMBER |  | 18 |  | Number of questions to show per page in the UI. |
| IN_USE | VARCHAR2 | 30 |  |  | Indicates if there have been any responses submitted for this questionnaire. |
| LATEST_VERSION | VARCHAR2 | 30 |  |  | Indicates if this is the latest version for this questionnaire id. |
| VERSION_DESCRIPTION | VARCHAR2 | 2000 |  |  | Description of changes made when a new version is created. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SCORED_FLAG | VARCHAR2 | 30 |  |  | Indicates questionnaire is a scored questionnaire. |
| CALC_RULE_CODE | VARCHAR2 | 30 |  |  | Calculation rule for calculating overall questionnaire score. |
| MAX_POSSIBLE_SCORE | NUMBER |  | 18 |  | Maximum possible score for a questionnaire, used to determine passing score. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| LAYOUT_OPTION | VARCHAR2 | 30 |  |  | Layout option for the questionnaire |
| SURVEY_TYPE | VARCHAR2 | 80 |  |  | Indicates the survey type of the questionnaire. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_QUESTIONNAIRES_B_N1 | Non Unique | Default | BUSINESS_GROUP_ID, TEMPLATE_FLAG, SUBSCRIBER_ID, QUESTIONNAIRE_CODE, QSTNR_VERSION_NUM |
| HRQ_QUESTIONNAIRES_B_N2 | Non Unique | Default | BUSINESS_GROUP_ID, QSTNR_TEMPLATE_ID |
| HRQ_QUESTIONNAIRES_B_PK | Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRQ_QUESTIONNAIRES_B_PK1 | Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
