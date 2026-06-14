# PAY_REPORT_RECORDS_F

Record for the extracts definition, used by reporting processing code

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportrecordsf-25322.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payreportrecordsf-25322.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REPORT_RECORDS_F_PK | REPORT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| REPORT_RECORD_ID | NUMBER |  | 18 | Yes | REPORT_RECORD_ID |  |
| BASE_RECORD_NAME | VARCHAR2 | 80 |  | Yes | BASE_RECORD_NAME |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| REPORT_BLOCK_ID | NUMBER |  | 18 | Yes | REPORT_BLOCK_ID |  |
| TEMPLATE_RECORD_ID | NUMBER |  | 18 |  | TEMPLATE_RECORD_ID |  |
| XML_PROC_NAME | VARCHAR2 | 61 |  |  | XML_PROC_NAME |  |
| JAVA_CLASS_NAME | VARCHAR2 | 2000 |  |  | JAVA_CLASS_NAME |  |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |  |
| SEQUENCE | NUMBER |  | 5 | Yes | SEQUENCE |  |
| LAST_RUN_EXECUTED_MODE | VARCHAR2 | 30 |  | Yes | LAST_RUN_EXECUTED_MODE |  |
| OVERFLOW_MODE | VARCHAR2 | 30 |  | Yes | OVERFLOW_MODE |  |
| ACTION_LEVEL | VARCHAR2 | 30 |  |  | ACTION_LEVEL |  |
| FREQUENCY | NUMBER |  | 5 |  | FREQUENCY |  |
| NEXT_BLOCK_ID | NUMBER |  | 18 |  | NEXT_BLOCK_ID |  |
| XML_TAG_NAME | VARCHAR2 | 80 |  |  | XML_TAG_NAME |  |
| FLEX_STRUCTURE_CODE | VARCHAR2 | 80 |  |  | FLEX_STRUCTURE_CODE |  |
| TYPE_CODE | VARCHAR2 | 30 |  |  | TYPE_CODE |  |
| PROCESS_CODE | VARCHAR2 | 30 |  |  | PROCESS_CODE |  |
| BALANCE_GROUP_USAGE_ID | NUMBER |  | 18 |  | BALANCE_GROUP_USAGE_ID |  |
| REQUIRED_FLAG | VARCHAR2 | 30 |  |  | REQUIRED_FLAG |  |
| PREVENT_DUPLICATES_FLAG | VARCHAR2 | 30 |  |  | PREVENT_DUPLICATES_FLAG |  |
| HIDE_FLAG | VARCHAR2 | 30 |  |  | HIDE_FLAG |  |
| UPDATABLE_RECORD | VARCHAR2 | 1 |  |  | UPDATABLE_RECORD |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| CREATOR_ID | NUMBER |  | 18 |  | Creator id for template record id |  |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | Creator type for generated template records |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 152 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Report Record Attributes (PAY_REPORT_RECORDS_DFF) |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_REPORT_RECORDS_F_FK1 | Non Unique | Default | REPORT_BLOCK_ID, BASE_RECORD_NAME |
| PAY_REPORT_RECORDS_F_N1 | Non Unique | Default | BASE_RECORD_NAME |
| PAY_REPORT_RECORDS_F_N2 | Non Unique | Default | TEMPLATE_RECORD_ID |
| PAY_REPORT_RECORDS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_REPORT_RECORDS_F_N3 | Non Unique | Default | CREATOR_ID, CREATOR_TYPE |
| PAY_REPORT_RECORDS_F_N4 | Non Unique | Default | NEXT_BLOCK_ID |
| PAY_REPORT_RECORDS_F_PK | Unique | Default | REPORT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_REPORT_RECORDS_F_PK1 | Unique | Default | REPORT_RECORD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
