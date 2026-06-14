# PER_ORG_SECURITY_PROFILES_

Organization Security Profiles.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecurityprofiles-15281.html#perorgsecurityprofiles-15281](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecurityprofiles-15281.html#perorgsecurityprofiles-15281)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ORG_SECURITY_PROFILES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORG_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  |  | Indicates whether to display all organizations for the security profile. |
| NAME | VARCHAR2 | 240 |  |  | Denotes the name for Security Profile. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | This field represents whether an organization security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| SECURE_BY_ORG_HIERARCHY | VARCHAR2 | 1 |  |  | This field enables or disables the Organization Hierarchy option for an organization security profile. |
| ORG_HIER_TREE_STRUCT_CODE | VARCHAR2 | 30 |  |  | This field represents if its referencing a department tree or generic organization tree. |
| ORG_HIER_TREE_CODE | VARCHAR2 | 30 |  |  | This field represents the specific  tree code referencing the selected department tree or generic organization tree on the organization security profile. |
| TOP_ORG_SELECTION | VARCHAR2 | 1 |  |  | An organization security profile can be secured by organization trees. This represents an option which when enabled, can restrict the security up to that organization selected as a top organization in the tree. |
| TOP_ORGANIZATION_ID | NUMBER |  | 18 |  | This field represents an option which when enabled, includes the top organization in the selected tree. |
| INCLUDE_TOP_ORGANIZATION | VARCHAR2 | 1 |  |  | An organization security profile can be secured by organization trees. This represents an option which when enabled, can restrict security for selected top organization  in the tree. Otherwise security will be restricted only for those organizations below the top level organization. |
| SECURE_BY_LOCATION | VARCHAR2 | 1 |  |  | Obsolete. Not in use. |
| LOC_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Obsolete. Not in use. |
| SECURE_BY_ORG_CLASS | VARCHAR2 | 1 |  |  | This field enables or disables the Organization classification option for an organization security profile. |
| SECURE_BY_ORG_LIST | VARCHAR2 | 1 |  |  | This field enables or disables the Organization List option for an organization security profile.  When enabled, can allow security based on included or excluded organizations. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INCLUDE_FUTURE_ORGANIZATIONS | VARCHAR2 | 1 |  |  | INCLUDE_FUTURE_ORGANIZATIONS |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ORG_SECURITY_PROFILES_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORG_SECURITY_PROFILE_ID |
| PER_ORG_SEC_PROFN1_ | Non Unique | Default | ORG_SECURITY_PROFILE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
