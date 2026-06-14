# HRM_POOL_SECURITY_PROFILES

pool security profile table stores the security profiles created for public talent pools.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpoolsecurityprofiles-26279.html#hrmpoolsecurityprofiles-26279](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpoolsecurityprofiles-26279.html#hrmpoolsecurityprofiles-26279)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_POOL_SECURITY_PROFILES_PK | POOL_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| POOL_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Pool security profile id uniquely identifies the talent pool security profile. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. | Active |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the security profile entered by user. | Active |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | Designate if security profile is defined for view all access. | Active |
| VIEW_ALL_PUBLIC_POOLS | VARCHAR2 | 1 |  |  | Designate if security profile is defined for access of all public talent pools. | Active |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Designate if security profile is enabled or not . | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Active |
| SECURE_BY_BUSINESS_UNIT | VARCHAR2 | 1 |  | Yes | Designate whether to secure by business unit. | Active |
| SECURE_BY_DEPARTMENT | VARCHAR2 | 1 |  | Yes | Designate whether to secure by department. | Active |
| SECURE_BY_JOB_FAMILY | VARCHAR2 | 1 |  | Yes | Designate whether to secure by job family. | Active |
| SECURE_BY_OWNER_ONLY | VARCHAR2 | 1 |  | Yes | Designate whether to secure only by defined owners. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRM_POOL_SECURITY_PROFILES_PK | Unique | HRM_POOL_SECURITY_PROFILES_PK | POOL_SECURITY_PROFILE_ID, ORA_SEED_SET1 | Active |
| HRM_POOL_SECURITY_PROFILE_N20 | Non Unique | HRM_POOL_SECURITY_PROFILE_N20 | SGUID |  |
| HRM_POOL_SECURITY_PROFILE_PK1 | Unique | HRM_POOL_SECURITY_PROFILE_PK1 | POOL_SECURITY_PROFILE_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
