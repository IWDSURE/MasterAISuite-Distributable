# PER_EXT_DELIVERY_OPTIONS_B

Delivery options used in Extract Definition.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdeliveryoptionsb-3980.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdeliveryoptionsb-3980.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_DELIVERY_OPTIONS_B_PK | EXT_DELIVERY_OPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_DELIVERY_OPTION_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| PARENT_DELIVERY_OPTION_ID | NUMBER |  | 18 |  | Parent Delivery Option Id is used to support hierarchy |
| BASE_DELIVERY_OPTION_NAME | VARCHAR2 | 80 |  |  | Base Name of the Delivery Option |
| DATE_FROM | DATE |  |  |  | The start Date of the delivery option |
| DATE_TO | DATE |  |  |  | The End Date of the delivery option |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Definition Id to which the Delivery Option belongs to |
| CALENDAR_CODE | VARCHAR2 | 80 |  |  | Calendar Code used |
| REP_DOCUMENT_ID | NUMBER |  | 18 |  | Document Type Id in Documents of Record |
| DELIVERY_TYPE | VARCHAR2 | 40 |  |  | Mode of Delivery |
| BIP_REPORT_NAME | VARCHAR2 | 2000 |  |  | Report Name in BIP Server |
| BIP_TEMPLATE_NAME | VARCHAR2 | 2000 |  |  | Template  Name in BIP Server |
| OUTPUT_TYPE | VARCHAR2 | 2000 |  |  | Output type overrides the definition output type |
| OUTPUT_NAME | VARCHAR2 | 2000 |  |  | Output name overwrites definition output name |
| OUTPUT_DIRECTORY_NAME | VARCHAR2 | 2000 |  |  | Name of the output directory |
| FILTER_NODE | VARCHAR2 | 2000 |  |  | Filter Node in data XML file |
| BURSTING_NODE | VARCHAR2 | 2000 |  |  | Bursting Node in data XML file |
| OVERRIDE_DELIVERY_OPTION_ID | NUMBER |  | 18 |  | The delivery option id which will be overridden |
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
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| MANDATORY_FLAG | VARCHAR2 | 30 |  |  | The flag indicates whether the delivery option is mandatory for considering a run to be successful or not. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_DELIVERY_OPTIONS_B_PK | Unique | FUSION_TS_TX_DATA | EXT_DELIVERY_OPTION_ID, ORA_SEED_SET1 |
| PER_EXT_DELIVERY_OPTIONS_B_PK1 | Unique | FUSION_TS_TX_DATA | EXT_DELIVERY_OPTION_ID, ORA_SEED_SET2 |
| PER_EXT_DELIVERY_OPTIONS_N20 | Non Unique | Default | SGUID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
