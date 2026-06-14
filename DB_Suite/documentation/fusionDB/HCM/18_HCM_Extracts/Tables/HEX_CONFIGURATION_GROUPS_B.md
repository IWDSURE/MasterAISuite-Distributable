# HEX_CONFIGURATION_GROUPS_B

The base table stores the details of the Process Configuration Groups referred in extracts.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigurationgroupsb-31313.html#hexconfigurationgroupsb-31313](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigurationgroupsb-31313.html#hexconfigurationgroupsb-31313)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_CONFIG_GROUPS_B_PK | CONFIGURATION_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIGURATION_GROUP_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| BASE_CONFIG_GROUP_CODE | VARCHAR2 | 80 |  | Yes | The column indicates the code of the configuration group. |
| PARENT_CONFIG_GROUP_NAME | VARCHAR2 | 80 |  |  | The column indicates the parent configuration group name used as source for creating the current configuration group. |
| LEGACY_PROCESS_CONFIG_CODE | VARCHAR2 | 80 |  |  | The column indicates the reference lookup code for deriving the language specific name. |
| LEGACY_COMPATIBLE | VARCHAR2 | 1 |  |  | The column indicates if the created configuration group is legacy compatible. Valid values are Y and N. Default is N. |
| ENABLED_FLAG | VARCHAR2 | 15 |  |  | ENABLED/HIDDEN/DEPRECATED/DISABLED |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_CONFIG_GROUPS_B_N1 | Non Unique | Default | BASE_CONFIG_GROUP_CODE |
| HEX_CONFIG_GROUPS_B_PK | Unique | Default | CONFIGURATION_GROUP_ID, ORA_SEED_SET1 |
| HEX_CONFIG_GROUPS_B_PK1 | Unique | Default | CONFIGURATION_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
