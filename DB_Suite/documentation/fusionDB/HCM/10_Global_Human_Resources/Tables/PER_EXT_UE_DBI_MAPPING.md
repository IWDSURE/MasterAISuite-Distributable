# PER_EXT_UE_DBI_MAPPING

DBI and User Entity Mapping Table

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextuedbimapping-16470.html#perextuedbimapping-16470](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextuedbimapping-16470.html#perextuedbimapping-16470)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_UE_DBI_MAPPING_PK | UE_DBI_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UE_DBI_MAPPING_ID | NUMBER |  | 18 | Yes | This column contains the value for UE_DBI_MAPPING_ID |
| USER_ENTITY_ID | NUMBER |  | 18 | Yes | This column contains the value for USER_ENTITY_ID |
| BASE_USER_ENTITY_NAME | VARCHAR2 | 240 |  | Yes | This column contains the value for BASE_USER_ENTITY_NAME |
| PARENT_BASE_USER_ENTITY | VARCHAR2 | 240 |  | Yes | This column contains the value for PARENT_BASE_USER_ENTITY |
| PARENT_USER_ENTITY_ID | NUMBER |  | 18 | Yes | This column contains the value for PARENT_USER_ENTITY_ID |
| BASE_USER_NAME | VARCHAR2 | 240 |  | Yes | This column contains the value for BASE_USER_NAME |
| DBI_ID | NUMBER |  | 18 |  | This column contains the value for DBI_ID |
| PARENT_BASE_USER_NAME | VARCHAR2 | 240 |  |  | This column contains the value for PARENT_BASE_USER_NAME |
| PARENT_DBI_ID | NUMBER |  | 18 |  | This column contains the value for PARENT_DBI_ID |
| ACTIVE_STATUS | VARCHAR2 | 30 |  |  | This column contains the value for ACTIVE_STATUS |
| SCORE | NUMBER |  | 18 |  | This column contains the value for SCORE |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SGUID | VARCHAR2 | 32 |  |  | This column contains the value for SGUID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_EXT_UE_DBI_MAPPING_N1 | Non Unique | Default | BASE_USER_ENTITY_NAME |
| PER_EXT_UE_DBI_MAPPING_N2 | Non Unique | Default | PARENT_BASE_USER_ENTITY |
| PER_EXT_UE_DBI_MAPPING_N20 | Non Unique | Default | SGUID |
| PER_EXT_UE_DBI_MAPPING_N3 | Non Unique | Default | USER_ENTITY_ID |
| PER_EXT_UE_DBI_MAPPING_N4 | Non Unique | Default | PARENT_USER_ENTITY_ID |
| PER_EXT_UE_DBI_MAPPING_PK | Unique | Default | UE_DBI_MAPPING_ID, ORA_SEED_SET1 |
| PER_EXT_UE_DBI_MAPPING_PK1 | Unique | Default | UE_DBI_MAPPING_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
