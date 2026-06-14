# HRT_PROFILE_TYPE_TEXT_B

This table along with the TL table stores the summary text that will be displayed in the profile cards.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypetextb-3699.html#hrtprofiletypetextb-3699](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypetextb-3699.html#hrtprofiletypetextb-3699)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TYPE_TEXT_B_PK | TEXT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEXT_ID | NUMBER |  | 18 | Yes | Primary Key for the table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_TYPE_ID | NUMBER |  | 18 |  | Profile Type for which the summary text is applicable. |
| TEXT_CODE | VARCHAR2 | 30 |  |  | Indicates where the text is applicable: Career Card or Experience Card or other area |
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
| HRT_PROFILE_TYPE_TEXT_B_PK | Unique | Default | TEXT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_PROFILE_TYPE_TEXT_B_PK1 | Unique | Default | TEXT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |
| HRT_PROFILE_TYPE_TEXT_B_U1 | Unique | Default | BUSINESS_GROUP_ID, PROFILE_TYPE_ID, TEXT_CODE, ORA_SEED_SET1 |
| HRT_PROFILE_TYPE_TEXT_B_U11 | Unique | Default | BUSINESS_GROUP_ID, PROFILE_TYPE_ID, TEXT_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
