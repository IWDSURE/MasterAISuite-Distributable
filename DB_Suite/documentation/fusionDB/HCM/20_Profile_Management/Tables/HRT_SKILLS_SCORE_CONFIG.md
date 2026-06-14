# HRT_SKILLS_SCORE_CONFIG

This table stores skill score configuration information.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsscoreconfig-23461.html#hrtskillsscoreconfig-23461](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillsscoreconfig-23461.html#hrtskillsscoreconfig-23461)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_SCORE_CONFIG_PK | SKILL_SCORE_CONFIG_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_SCORE_CONFIG_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SKILL_EVIDENCE_TYPE | VARCHAR2 | 30 |  | Yes | Stores the skill evidence type. Lookup type - ORA_HRT_SKILL_EVIDENCE_TYPE |
| SKILL_EVIDENCE_SCORE | NUMBER |  | 18 | Yes | Stores the score associated with skill evidence type. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_SKILLS_SCORE_CONFIG_U1 | Unique | Default | SKILL_SCORE_CONFIG_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_SKILLS_SCORE_CONFIG_U11 | Unique | Default | SKILL_SCORE_CONFIG_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |
| HRT_SKILLS_SCORE_CONFIG_U2 | Unique | Default | SKILL_EVIDENCE_TYPE, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_SKILLS_SCORE_CONFIG_U21 | Unique | Default | SKILL_EVIDENCE_TYPE, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
