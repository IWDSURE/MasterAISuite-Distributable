# HRT_PROFILE_TYPES_B

Profile Types Base table stores the profile typ header information

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypesb-16225.html#hrtprofiletypesb-16225](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypesb-16225.html#hrtprofiletypesb-16225)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TYPES_B_PK | PROFILE_TYPE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | Profile Type ID |
| SHOW_DESCRIPTION_FLAG | VARCHAR2 | 30 |  |  | Include Description Flag for job profile type. |
| SHOW_RESPONSIBILITY_FLAG | VARCHAR2 | 30 |  |  | Include Responsibility Flag for job profile type. |
| SHOW_QUALIFICATION_FLAG | VARCHAR2 | 30 |  |  | Include Qualification Flag for job profile type. |
| SHOW_CRITICALITY_FLAG | VARCHAR2 | 30 |  |  | Include Criticality Flag for job profile type. |
| AUTO_CREATE_FLAG | VARCHAR2 | 30 |  |  | Auto create person profile flag |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_TYPE_CODE | VARCHAR2 | 30 |  |  | Profile Type Code |
| PROFILE_STATUS_CODE | VARCHAR2 | 30 |  |  | Profile Status Code |
| PROFILE_USAGE_CODE | VARCHAR2 | 30 |  |  | Profile usage Code |
| SYNC_FLEXFIELD_FLAG | VARCHAR2 | 20 |  |  | SYNC_FLEXFIELD_FLAG |
| DATE_FROM | DATE |  |  | Yes | Date From |
| DATE_TO | DATE |  |  |  | Date To |
| PROFILE_SYNC_FLAG | VARCHAR2 | 20 |  |  | PROFILE_SYNC_FLAG |
| SYNC_CRITICALITY_FLAG | VARCHAR2 | 20 |  |  | SYNC_CRITICALITY_FLAG |
| SYNC_DESCRIPTION_FLAG | VARCHAR2 | 20 |  |  | SYNC_DESCRIPTION_FLAG |
| SYNC_QUALIFICATION_FLAG | VARCHAR2 | 20 |  |  | SYNC_QUALIFICATION_FLAG |
| SYNC_RESPONSIBILITY_FLAG | VARCHAR2 | 20 |  |  | SYNC_RESPONSIBILITY_FLAG |
| SYNC_RISK_FLAG | VARCHAR2 | 20 |  |  | SYNC_RISK_FLAG |
| OVERWRITE_SYNC_ITEM_FLAG | VARCHAR2 | 20 |  |  | OVERWRITE_SYNC_ITEM_FLAG |
| SYNC_ATTACHMENT_FLAG | VARCHAR2 | 20 |  |  | SYNC_ATTACHMENT_FLAG |
| PID_APPROVAL_FLAG | VARCHAR2 | 30 |  |  | PID Approval Flag |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_TYPES_B_U1 | Unique | Default | PROFILE_TYPE_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_PROFILE_TYPES_B_U11 | Unique | Default | PROFILE_TYPE_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |
| HRT_PROFILE_TYPES_B_U2 | Unique | Default | PROFILE_TYPE_CODE, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_PROFILE_TYPES_B_U21 | Unique | Default | PROFILE_TYPE_CODE, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
