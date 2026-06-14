# HRT_SKILLS_SETTINGS

This table stores admin skill settings.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillssettings-25480.html#hrtskillssettings-25480](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtskillssettings-25480.html#hrtskillssettings-25480)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_SKILLS_SETTINGS_PK | SKILL_SETTING_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_SETTING_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| AUTO_CONFIRM_FLAG | VARCHAR2 | 30 |  |  | Flag indicating if auto confirmation is enabled or not. |
| FREE_FORM_ENABLED_FLAG | VARCHAR2 | 30 |  |  | Enable free-form entry for a skill |
| CONFIRMED_SKILLS_ONLY_FLAG | VARCHAR2 | 30 |  |  | Column to indicate if a confirmed skill can be marked as developed |
| ALLOW_ADD_OTHER_SKILLS_FLAG | VARCHAR2 | 30 |  |  | Flag indicating if we allow to add other skill |
| SKILLS_DISPLAY_LIMIT | NUMBER |  | 3 |  | Column to store the maximum number of skills to display in the skill river |
| ENABLE_DOMAIN | VARCHAR2 | 30 |  |  | Enable Domain |
| ENABLE_DESCRIPTION | VARCHAR2 | 30 |  |  | Enable Description |
| ENABLE_BUSINESS_CAPABILITY | VARCHAR2 | 30 |  |  | Enable Business Capability |
| ENABLE_BUSINESS_DRIVER | VARCHAR2 | 30 |  |  | Enable Busness Driver |
| HIDE_ENDORSEMENTS | VARCHAR2 | 30 |  |  | Hide Endorsement |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| HRT_SKILLS_SETTINGS_U1 | Unique | Default | SKILL_SETTING_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_SKILLS_SETTINGS_U11 | Unique | Default | SKILL_SETTING_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
