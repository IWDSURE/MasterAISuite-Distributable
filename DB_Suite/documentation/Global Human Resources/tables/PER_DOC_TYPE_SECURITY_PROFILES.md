# PER_DOC_TYPE_SECURITY_PROFILES

This table is contains the Document Type Security profiles created in the application.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecurityprofiles-27297.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecurityprofiles-27297.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DOC_TYPE_SECURITY_PRO_PK | DOC_TYPE_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOC_TYPE_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | When this is set to True, all document types become available when the document type security profile is applied. |
| NAME | VARCHAR2 | 240 |  | Yes | Defines the name for Security Profile |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether to enable or disable the?document type security profile |
| INCLUDE_EXCLUDE_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether to include or exclude the associated document types in the document type security profile. |
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
| PER_DOC_TYPE_SECURITY_PRO_N20 | Non Unique | Default | SGUID |
| PER_DOC_TYPE_SECURITY_PRO_PK | Unique | Default | DOC_TYPE_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| PER_DOC_TYPE_SECURITY_PRO_PK1 | Unique | Default | DOC_TYPE_SECURITY_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
