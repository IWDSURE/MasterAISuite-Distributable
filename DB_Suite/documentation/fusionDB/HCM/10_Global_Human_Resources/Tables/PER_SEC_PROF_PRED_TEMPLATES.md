# PER_SEC_PROF_PRED_TEMPLATES

Person Security Profiles Predicate Templates: This table will hold predicate templates for different AOR scope selected for person security profile.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persecprofpredtemplates-19276.html#persecprofpredtemplates-19276](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persecprofpredtemplates-19276.html#persecprofpredtemplates-19276)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SEC_PROF_PRED_TEMPLAT_PK | PRED_TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRED_TEMPLATE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENABLED | VARCHAR2 | 1 |  | Yes | This field represents whether a predicate template is is enabled or disabled. |
| SECURITY_PROFILE_TYPE | VARCHAR2 | 30 |  | Yes | This field represents type of security profile for which this predicate template is defined. |
| CRITERIA_IDENTIFIER | VARCHAR2 | 240 |  | Yes | This field represents criteria identifier. |
| PRED_TEMPLATE | VARCHAR2 | 4000 |  | Yes | This field holds security profile template predicate. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SEC_PROF_PRED_TEMPLAT_N20 | Non Unique | Default | SGUID |
| PER_SEC_PROF_PRED_TEMPL_PK | Unique | FUSION_TS_SEED | PRED_TEMPLATE_ID, ORA_SEED_SET1 |
| PER_SEC_PROF_PRED_TEMPL_PK1 | Unique | FUSION_TS_SEED | PRED_TEMPLATE_ID, ORA_SEED_SET2 |
| PER_SEC_PROF_PRED_TEMPL_U1 | Unique | FUSION_TS_SEED | SECURITY_PROFILE_TYPE, CRITERIA_IDENTIFIER, ORA_SEED_SET1 |
| PER_SEC_PROF_PRED_TEMPL_U11 | Unique | FUSION_TS_SEED | SECURITY_PROFILE_TYPE, CRITERIA_IDENTIFIER, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
