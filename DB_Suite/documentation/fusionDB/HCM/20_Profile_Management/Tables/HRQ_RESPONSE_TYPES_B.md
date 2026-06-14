# HRQ_RESPONSE_TYPES_B

List of available response types for each question type.  Defines how a question will be rendered in the ui.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqresponsetypesb-16774.html#hrqresponsetypesb-16774](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqresponsetypesb-16774.html#hrqresponsetypesb-16774)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_RESPONSE_TYPES_B_PK | BUSINESS_GROUP_ID, RESPONSE_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESPONSE_TYPE_ID | NUMBER |  | 18 | Yes | Unique identifier for a response type.  System generated id.  This attribute combined with the business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| RESPONSE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | A unique identifier for the response type. |
| QUESTION_TYPE | VARCHAR2 | 30 |  |  | Identifies the question type. |
| USE_AS_DEFAULT | VARCHAR2 | 30 |  |  | One response type can be used as the default for each question type. |
| VIEW_ID | VARCHAR2 | 240 |  | Yes | The jsff page used to display questions in the UI. |
| NUM_ROWS | NUMBER |  | 18 |  | Number of rows displayed for text box type responses. |
| QSTN_WIDTH_PCT | NUMBER |  | 18 |  | Amount of space allocated for displaying question text when question & answer are displayed side by side. |
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
| HRQ_RESPONSE_TYPES_B_PK1 | Unique | Default | BUSINESS_GROUP_ID, RESPONSE_TYPE_ID, ORA_SEED_SET1 |
| HRQ_RESPONSE_TYPES_B_PK11 | Unique | Default | BUSINESS_GROUP_ID, RESPONSE_TYPE_ID, ORA_SEED_SET2 |
| HRQ_RESPONSE_TYPES_B_U1 | Unique | Default | BUSINESS_GROUP_ID, RESPONSE_TYPE_CODE, ORA_SEED_SET1 |
| HRQ_RESPONSE_TYPES_B_U11 | Unique | Default | BUSINESS_GROUP_ID, RESPONSE_TYPE_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
