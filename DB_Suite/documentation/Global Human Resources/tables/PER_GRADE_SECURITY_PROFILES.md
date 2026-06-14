# PER_GRADE_SECURITY_PROFILES

Grade Security Profiles Table for configuring grade related security.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesecurityprofiles-26103.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesecurityprofiles-26103.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GRADE_SEC_PROFILES_PK | GRADE_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRADE_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | Grade security profiles are not in use - leave blank |
| NAME | VARCHAR2 | 240 |  | Yes | Denotes the name for the Grade Security Profile. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Grade security profiles are not in use - leave blank |
| SECURE_BY_GRADE_LADDER_LIST | VARCHAR2 | 1 |  | Yes | Grade security profiles are not in use - leave blank |
| SECURE_BY_GRADE_LIST | VARCHAR2 | 1 |  | Yes | Grade security profiles are not in use - leave blank |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_GRADE_SECURITY_PROFILES_PK | Unique | FUSION_TS_TX_DATA | GRADE_SECURITY_PROFILE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
