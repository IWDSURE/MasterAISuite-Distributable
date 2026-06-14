# PER_ORG_SECURITY_PROFILES

Organization Security Profiles.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecurityprofiles-8422.html#perorgsecurityprofiles-8422](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecurityprofiles-8422.html#perorgsecurityprofiles-8422)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ORG_SECURITY_PROFILES_PK | ORG_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | Indicates whether to display all organizations for the security profile. |
| NAME | VARCHAR2 | 240 |  | Yes | Denotes the name for Security Profile. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This field represents whether an organization security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| SECURE_BY_ORG_HIERARCHY | VARCHAR2 | 1 |  | Yes | This field enables or disables the Organization Hierarchy option for an organization security profile. |
| ORG_HIER_TREE_STRUCT_CODE | VARCHAR2 | 30 |  |  | This field represents if its referencing a department tree or generic organization tree. |
| ORG_HIER_TREE_CODE | VARCHAR2 | 30 |  |  | This field represents the specific  tree code referencing the selected department tree or generic organization tree on the organization security profile. |
| TOP_ORG_SELECTION | VARCHAR2 | 1 |  |  | An organization security profile can be secured by organization trees. This represents an option which when enabled, can restrict the security up to that organization selected as a top organization in the tree. |
| TOP_ORGANIZATION_ID | NUMBER |  | 18 |  | This field represents an option which when enabled, includes the top organization in the selected tree. |
| INCLUDE_TOP_ORGANIZATION | VARCHAR2 | 1 |  |  | An organization security profile can be secured by organization trees. This represents an option which when enabled, can restrict security for selected top organization  in the tree. Otherwise security will be restricted only for those organizations below the top level organization. |
| SECURE_BY_LOCATION | VARCHAR2 | 1 |  | Yes | Obsolete. Not in use. |
| LOC_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Obsolete. Not in use. |
| SECURE_BY_ORG_CLASS | VARCHAR2 | 1 |  | Yes | This field enables or disables the Organization classification option for an organization security profile. |
| SECURE_BY_ORG_LIST | VARCHAR2 | 1 |  | Yes | This field enables or disables the Organization List option for an organization security profile.  When enabled, can allow security based on included or excluded organizations. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INCLUDE_FUTURE_ORGANIZATIONS | VARCHAR2 | 1 |  | Yes | INCLUDE_FUTURE_ORGANIZATIONS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ORG_SECURITY_PROFILES_FK1 | Non Unique | FUSION_TS_TX_DATA | LOC_SECURITY_PROFILE_ID |
| PER_ORG_SECURITY_PROFILES_N20 | Non Unique | Default | SGUID |
| PER_ORG_SECURITY_PROFILES_PK | Unique | FUSION_TS_TX_DATA | ORG_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| PER_ORG_SECURITY_PROFILES_PK1 | Unique | FUSION_TS_TX_DATA | ORG_SECURITY_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
