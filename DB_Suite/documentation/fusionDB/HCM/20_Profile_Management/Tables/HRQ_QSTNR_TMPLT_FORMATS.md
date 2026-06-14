# HRQ_QSTNR_TMPLT_FORMATS

Defines a list of Response Types that are permitted for Questionnaires using this template.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrtmpltformats-8725.html#hrqqstnrtmpltformats-8725](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrtmpltformats-8725.html#hrqqstnrtmpltformats-8725)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_QSTNR_TMPLT_FORMATS_PK | QSTNR_TMPLT_FORMAT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_TMPLT_FORMAT_ID | NUMBER |  | 18 | Yes | Unique identifier for a questionnaire template format.  System generated id.  This attribute combined with business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| QSTNR_TEMPLATE_ID | NUMBER |  | 18 |  | Identifies the questionnaire template id. |
| RESPONSE_TYPE_ID | NUMBER |  | 18 |  | Identifies the response type id. |
| ADHOC_ALLOWED | VARCHAR2 | 230 |  |  | Determine if the Response Type may be used for adhoc questions. |
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
| HRQ_QSTNR_TMPLT_FORMATS_N1 | Non Unique | Default | BUSINESS_GROUP_ID, QSTNR_TEMPLATE_ID |
| HRQ_QSTNR_TMPLT_FORMATS_PK | Unique | Default | QSTNR_TMPLT_FORMAT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRQ_QSTNR_TMPLT_FORMATS_PK1 | Unique | Default | QSTNR_TMPLT_FORMAT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
