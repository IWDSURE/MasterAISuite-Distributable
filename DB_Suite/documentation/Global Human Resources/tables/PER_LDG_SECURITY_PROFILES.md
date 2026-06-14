# PER_LDG_SECURITY_PROFILES

Legislative Data Groups Security Profile.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldgsecurityprofiles-11644.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldgsecurityprofiles-11644.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDG_SECURITY_PROFILE_PK | LDG_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDG_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | This option provides unrestricted security access to the specific legislative data group (LDG) security profile. |
| NAME | VARCHAR2 | 240 |  |  | Denotes name for LDG Security Profiles. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This field represents whether a legislative data group (LDG) security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
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
|-------|------------|------------|----------|
| PER_LDG_SECURITY_PROFILES_N20 | Non Unique | Default | SGUID |
| PER_LDG_SECURITY_PROFILES_PK | Unique | FUSION_TS_TX_DATA | LDG_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| PER_LDG_SECURITY_PROFILES_PK1 | Unique | FUSION_TS_TX_DATA | LDG_SECURITY_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
