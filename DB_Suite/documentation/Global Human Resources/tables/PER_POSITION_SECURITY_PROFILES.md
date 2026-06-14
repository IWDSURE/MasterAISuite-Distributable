# PER_POSITION_SECURITY_PROFILES

Position Security Profiles Table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionsecurityprofiles-24723.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpositionsecurityprofiles-24723.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POS_SEC_PROFILES_PK | POSITION_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | This option provides unrestricted security access to the specific position security profile. |
| NAME | VARCHAR2 | 240 |  | Yes | Denotes name for the Position Security Profile. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This field represents whether a position security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| SECURE_BY_AOR | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profiles based on areas of responsibility. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description for the position security profile. |
| SECURE_BY_POSITION_HIERARCHY | VARCHAR2 | 1 |  | Yes | This option allows users to restrict positions based on position hierarchy in a position security profile. |
| POS_HIERARCHY_TREE_STRUCT_CODE | VARCHAR2 | 30 |  |  | Code representing the selected position tree structure used in a position hierarchy. |
| POS_HIERARCHY_TREE_CODE | VARCHAR2 | 30 |  |  | When securing by position hierarchy, this is the name of the position tree. |
| TOP_POS_SELECTION | VARCHAR2 | 100 |  |  | When securing position security profile by position tree, this option indicates the top position. |
| POS_HIERARCHY_CONTENT | VARCHAR2 | 30 |  |  | This option indicates position hierarchy content to be used for top position identification. |
| TOP_POSITION_ID | NUMBER |  | 18 |  | A position security profile can be secured by position trees. This option which when enabled, restricts the security up to that position selected as a top position in the tree. |
| INCLUDE_TOP_POSITION | VARCHAR2 | 1 |  |  | This option on the position security profile restricts the security access up to that position selected as a top position in the tree. |
| SECURE_BY_BUSINESS_UNIT | VARCHAR2 | 1 |  | Yes | This option allows users to restrict positions based on a list of business units from a selected organization security profile. |
| BU_ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | The unique organization security profile used to identify the list of business units secured by the position security profile. |
| SECURE_BY_DEPARTMENT | VARCHAR2 | 1 |  | Yes | This option allows users to restrict the position security profile based on a set of departments defined by an organization security profile. |
| DEPT_ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | The unique organization security profile used to identify the list of departments secured by the position security profile. |
| SECURE_BY_JOB | VARCHAR2 | 1 |  | Yes | Attribute not in use - leave blank |
| JOB_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOB_SECURITY_PROFILES table. |
| SECURE_BY_LOCATION | VARCHAR2 | 1 |  | Yes | Attribute not in use - leave blank |
| LOC_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Location security profiles are not in use - leave blank |
| SECURE_BY_POSITION_LIST | VARCHAR2 | 1 |  | Yes | Secure data based on a list of positions |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INCLUDE_FUTURE_POSITIONS | VARCHAR2 | 1 |  | Yes | INCLUDE_FUTURE_POSITIONS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_POSITION_SECURITY_PRO_N20 | Non Unique | Default | SGUID |
| PER_POS_SEC_PROFILES_PK | Unique | FUSION_TS_TX_DATA | POSITION_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| PER_POS_SEC_PROFILES_PK1 | Unique | FUSION_TS_TX_DATA | POSITION_SECURITY_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
