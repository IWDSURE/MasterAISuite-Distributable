# PER_GEN_DATA_ROLE_PROFILES

This table stores the information related to assignment of Security Profiles to a Data Role.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergendataroleprofiles-18469.html#pergendataroleprofiles-18469](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergendataroleprofiles-18469.html#pergendataroleprofiles-18469)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GEN_DATA_ROLE_PROF_PK | GEN_DATA_ROLE_PROFILES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEN_DATA_ROLE_PROFILES_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| GENERATED_DATA_ROLE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_GENERATED_DATA_ROLES table. |
| HR_SECURING_OBJECT | VARCHAR2 | 20 |  | Yes | Type of security profile assigned to the role via the data roles UI. |
| SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Internal ID for a security profile assigned to role via the data roles UI. |
| VIEW_ALL | VARCHAR2 | 30 |  |  | Obsolete. |
| START_DATE | DATE |  |  | Yes | Date from which the Generated Data Role Profile is Active. |
| END_DATE | DATE |  |  |  | Date till when the Generated Data Role Profile is Active. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_GEN_DATA_ROLE_PROFILES_N1 | Non Unique | Default | SECURITY_PROFILE_ID, HR_SECURING_OBJECT, GENERATED_DATA_ROLE_ID, BUSINESS_GROUP_ID |
| PER_GEN_DATA_ROLE_PROF_PK | Unique | FUSION_TS_TX_DATA | GEN_DATA_ROLE_PROFILES_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
