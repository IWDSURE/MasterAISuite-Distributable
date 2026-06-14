# HRT_PROFILE_TYPE_ROLES

Profile Type Roles is the table that stores the data for the allowed roles for the users.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletyperoles-22194.html#hrtprofiletyperoles-22194](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletyperoles-22194.html#hrtprofiletyperoles-22194)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TYPE_ROLES_PK | PROFILE_TYPE_ROLE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PROFILE_TYPE_ROLE_ID | NUMBER |  | 18 | Yes | Profile Type Role Id |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| SECTION_ID | NUMBER |  | 18 | Yes | Section ID |  |
| ROLE_CODE | VARCHAR2 | 30 |  |  | Rold Code |  |
| SECURITY_MODIFY_FLAG | VARCHAR2 | 30 |  |  | Security Modify Flag |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_TYPE_ROLES_U1 | Unique | Default | PROFILE_TYPE_ROLE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
