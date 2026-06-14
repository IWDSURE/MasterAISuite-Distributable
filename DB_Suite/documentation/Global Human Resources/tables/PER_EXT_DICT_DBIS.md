# PER_EXT_DICT_DBIS

This Table will be used in Extract for Dictionary DBI.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdictdbis-28996.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdictdbis-28996.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_DICT_DBIS_PK | DICTIONARY_DBI_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DICTIONARY_DBI_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| DATABASE_ITEM_ID | NUMBER |  | 18 | Yes | DATABASE_ITEM_ID |
| BASE_USER_NAME | VARCHAR2 | 255 |  | Yes | BASE_USER_NAME |
| LRG_OBJ_DATA_TYPE | VARCHAR2 | 32 |  |  | LRG_OBJ_DATA_TYPE |
| XML_TAG_NAME | VARCHAR2 | 80 |  | Yes | XML_TAG_NAME |
| ATTRIBUTE_TYPE | VARCHAR2 | 5 |  |  | ATTRIBUTE_TYPE |
| AUTO_CREATE_TYPE | VARCHAR2 | 1 |  |  | AUTO_CREATE_TYPE |
| THREADING_FLAG | VARCHAR2 | 1 |  |  | THREADING_FLAG |
| STATUS | VARCHAR2 | 1 |  | Yes | STATUS |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACTIVE | VARCHAR2 | 1 |  |  | ACTIVE |
| ATTRIBUTE_NUMBER1 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  | 18 |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| SUPERSEDING_DBI_ID | NUMBER |  | 18 |  | SUPERSEDING_DBI_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_DICT_DBIS_FK1 | Unique | Default | DATABASE_ITEM_ID, ORA_SEED_SET1 |
| PER_EXT_DICT_DBIS_FK11 | Unique | Default | DATABASE_ITEM_ID, ORA_SEED_SET2 |
| PER_EXT_DICT_DBIS_FK2 | Unique | Default | BASE_USER_NAME, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| PER_EXT_DICT_DBIS_FK21 | Unique | Default | BASE_USER_NAME, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ENTERPRISE_ID, ORA_SEED_SET2 |
| PER_EXT_DICT_DBIS_N20 | Non Unique | Default | SGUID |
| PER_EXT_DICT_DBIS_PK | Unique | Default | DICTIONARY_DBI_ID, ORA_SEED_SET1 |
| PER_EXT_DICT_DBIS_PK1 | Unique | Default | DICTIONARY_DBI_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
