# HRT_PROFILE_TYP_SECTIONS

Profile Type Sections  table that holds the data for the various sections

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypsections-25950.html#hrtprofiletypsections-25950](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypsections-25950.html#hrtprofiletypsections-25950)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TYP_SECTIONS_PK | SECTION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SECTION_ID | NUMBER |  | 18 | Yes | Section ID |
| DEFAULT_FLAG | VARCHAR2 | 1 |  |  | DEFAULT_FLAG |
| DISPLAY_ORDER | NUMBER |  | 5 |  | Display Order |
| SECTION_LAYOUT | VARCHAR2 | 30 |  |  | Stores layout option for FUSE UI. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | Profile Type ID |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Content Type ID |
| PARENT_SECTION_ID | NUMBER |  | 18 |  | Parent Section ID |
| CONTENT_TYPE_RELATION_ID | NUMBER |  | 18 |  | Content Type Relation ID |
| SECTION_ITEM_REQD_FLAG | VARCHAR2 | 30 |  |  | Section Item Required Flag |
| APPROVAL_REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Approval Required Flag |
| QUALIFIER_SET_ID1 | NUMBER |  | 18 |  | Qualifier Set ID1 |
| QUALIFIER_SET_ID2 | NUMBER |  | 18 |  | Qualifier Set ID2 |
| SECTION_CONTEXT | VARCHAR2 | 300 |  |  | Section Context |
| SECURITY_CONTEXT | VARCHAR2 | 300 |  |  | This column will have the same value as Section_Context for newly created sections. For sections that are upgraded from the old architecture, this column will have the value of Context_Name for the Content Type of the section. |
| TEMPLATE_FLAG | VARCHAR2 | 1 |  |  | Template flag to indicate whether it is template or not |
| DFF_CONTEXT_NAME | VARCHAR2 | 80 |  |  | DFF context name for each section |
| ANALYTIC_PRIORITY | VARCHAR2 | 30 |  |  | Analytic priority to indicate the ordering of the data |
| ANALYTIC_PRIORITY_SOURCE_CODE | VARCHAR2 | 30 |  |  | Analytic priority based on consumer |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Active flag to indicate whether the section is active ('Y') or inactive (null/ 'N') |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| TEMPLATE_BASED_SECTION_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate whether section is based on template or not |
| LINKEDIN_ENABLED_FLAG | VARCHAR2 | 30 |  |  | Linkedin enable flag is use to indicate whether the section is supporting linkedin data ('Y') or not (null/ 'N') |
| SKILL_RECOMMEND_ENABLED_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate whether Skills content section supports system-generated recommendations ('Y') or not (null/ 'N') |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_TYP_SECTIONS_N1 | Non Unique | Default | SECTION_CONTEXT |
| HRT_PROFILE_TYP_SECTIONS_N2 | Non Unique | Default | CONTENT_TYPE_ID, PROFILE_TYPE_ID |
| HRT_PROFILE_TYP_SECTIONS_U1 | Unique | Default | SECTION_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_PROFILE_TYP_SECTIONS_U11 | Unique | Default | SECTION_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
