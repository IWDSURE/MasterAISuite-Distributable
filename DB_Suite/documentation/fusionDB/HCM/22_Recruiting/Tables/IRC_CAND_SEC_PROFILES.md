# IRC_CAND_SEC_PROFILES

This table will store any candidate search profiles that have been created from the FSM UI. It will also have a seeded row with 'View All Candidates' , allowing unfiltered search results.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandsecprofiles-25727.html#irccandsecprofiles-25727](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandsecprofiles-25727.html#irccandsecprofiles-25727)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_SEC_PROFILES_PK | CAND_SEC_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAND_SEC_PROFILE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of Candidate Search Security Profile |
| DESCRIPTION | CLOB |  |  |  | Brief description of Profile |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify if the profile is enabled or not |
| SECURE_BY_RECRUITING_TYPE_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Recruiting Type dimension |
| SECURE_BY_PERSON_TYPE_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Person Type dimension |
| SECURE_BY_CAND_COUNTRY_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Candidate Country dimension |
| SECURE_BY_GRADE_LEVEL_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Grade level dimension |
| SECURE_BY_BUSINESS_UNIT_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify business unit dimension |
| SECURE_BY_JOB_FAMILY_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Job Family dimension |
| SECURE_BY_JOB_FUNC_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Job Function dimension |
| SECURE_BY_LEGAL_EMPLOYER_FLAG | VARCHAR2 | 1 |  | Yes | Flag to specify Legal Employer dimension |
| VIEW_ALL_FLAG | VARCHAR2 | 1 |  |  | Flag to specify all dimensions |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_SEC_PROFILES_PK | Unique | Default | CAND_SEC_PROFILE_ID, ORA_SEED_SET1 |
| IRC_CAND_SEC_PROFILES_PK1 | Unique | Default | CAND_SEC_PROFILE_ID, ORA_SEED_SET2 |
| IRC_CAND_SEC_PROFILES_U1 | Unique | Default | NAME, ORA_SEED_SET1 |
| IRC_CAND_SEC_PROFILES_U11 | Unique | Default | NAME, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
