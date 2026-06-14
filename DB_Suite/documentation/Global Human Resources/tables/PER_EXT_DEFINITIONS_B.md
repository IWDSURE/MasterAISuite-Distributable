# PER_EXT_DEFINITIONS_B

Extract Definitions base table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdefinitionsb-26915.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdefinitionsb-26915.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_DEFINITIONS_B_PK | EXT_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| EXT_DEFINITION_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |  |
| UNFREEZE_COMMENTS | VARCHAR2 | 4000 |  |  | UNFREEZE_COMMENTS |  |
| UNFREEZE_DATE | DATE |  |  |  | UNFREEZE_DATE |  |
| FREEZE_STATUS | VARCHAR2 | 3 |  |  | FREEZE_STATUS |  |
| BASE_DEFINITION_NAME | VARCHAR2 | 80 |  |  | Base Name of the Definition |  |
| XML_TAG_NAME | VARCHAR2 | 80 |  |  | XML Tag Name of Definition |  |
| EXT_TYPE_CODE | VARCHAR2 | 30 |  |  | Type Code of Definition |  |
| CM_DISPLAY_FLAG | VARCHAR2 | 30 |  |  | Unused columns(Do not expose) |  |
| APPEND_REQUEST_ID_FLAG | VARCHAR2 | 30 |  |  | ESS Request Id appended  to output file name |  |
| KICKOFF_DELIVERY_FLAG | VARCHAR2 | 30 |  |  | Kick off delivery process flag |  |
| SPECIAL_HANDLING_FLAG | VARCHAR2 | 30 |  |  | Special Handling for ANSI Extracts |  |
| EXT_GLOBAL_FLAG | VARCHAR2 | 30 |  |  | Unused columns(Do not expose) |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| DELIVERY_EXT_DEFINITION_ID | NUMBER |  | 18 |  | Originating Extract Definition |  |
| DATE_START | DATE |  |  |  | The Date on which the extract definition and all its children would be created. |  |
| VALID_STATUS | VARCHAR2 | 30 |  |  | This flag shows whether the Extract definition is valid or not. |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Definition Attributes (PER_EXT_DEFINITIONS_DFF) |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| RUN_ELEVATED | VARCHAR2 | 1 |  |  | Run on Elevated Privilege. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| CREATOR_ID | NUMBER |  | 18 |  | Foreign key to table identified by CREATOR_TYPE. |  |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | Foreign key table of surrogate key identified by CREATOR_ID. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_DEFINITIONS_B_N1 | Non Unique | Default | CREATOR_ID, CREATOR_TYPE |
| PER_EXT_DEFINITIONS_B_N20 | Non Unique | Default | SGUID |
| PER_EXT_DEFINITIONS_B_PK | Unique | Default | EXT_DEFINITION_ID, ORA_SEED_SET1 |
| PER_EXT_DEFINITIONS_B_PK1 | Unique | Default | EXT_DEFINITION_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
