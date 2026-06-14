# PER_GEN_DATA_ROLE_PROFILES_

This table stores the information related to assignment of Security Profiles to a Data Role.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergendataroleprofiles-11458.html#pergendataroleprofiles-11458](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergendataroleprofiles-11458.html#pergendataroleprofiles-11458)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GEN_DATA_ROLE_PROF_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GEN_DATA_ROLE_PROFILES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEN_DATA_ROLE_PROFILES_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| GENERATED_DATA_ROLE_ID | NUMBER |  | 18 |  | Foreign Key to PER_GENERATED_DATA_ROLES table. |
| HR_SECURING_OBJECT | VARCHAR2 | 20 |  |  | Type of security profile assigned to the role via the data roles UI. |
| SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Internal ID for a security profile assigned to role via the data roles UI. |
| VIEW_ALL | VARCHAR2 | 30 |  |  | Obsolete. |
| START_DATE | DATE |  |  |  | Date from which the Generated Data Role Profile is Active. |
| END_DATE | DATE |  |  |  | Date till when the Generated Data Role Profile is Active. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_GEN_DATA_ROLE_PROFILN1_ | Non Unique | Default | GEN_DATA_ROLE_PROFILES_ID |
| PER_GEN_DATA_ROLE_PROF_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, GEN_DATA_ROLE_PROFILES_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
