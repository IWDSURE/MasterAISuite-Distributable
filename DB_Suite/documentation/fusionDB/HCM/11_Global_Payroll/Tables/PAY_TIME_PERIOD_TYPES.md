# PAY_TIME_PERIOD_TYPES

This table contains the predefined list of valid period types used to define calendars for payroll processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimeperiodtypes-29130.html#paytimeperiodtypes-29130](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimeperiodtypes-29130.html#paytimeperiodtypes-29130)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TIME_PERIOD_TYPES_PK | PERIOD_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PERIOD_TYPE | VARCHAR2 | 30 |  | Yes | PERIOD_TYPE |  |
| NUMBER_PER_FISCAL_YEAR | NUMBER |  | 18 |  | NUMBER_PER_FISCAL_YEAR |  |
| YEAR_TYPE_IN_NAME | VARCHAR2 | 1 |  |  | YEAR_TYPE_IN_NAME |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |  |
| SYSTEM_FLAG | VARCHAR2 | 30 |  |  | SYSTEM_FLAG |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| PROGRAM_APPLICATION_ID | NUMBER |  | 18 |  | PROGRAM_APPLICATION_ID |  |
| PROGRAM_ID | NUMBER |  | 18 |  | PROGRAM_ID |  |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | PROGRAM_UPDATE_DATE |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Period Type Attributes (PAY_TIME_PERIOD_TYPES_DFF) |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| DISPLAY_PERIOD_TYPE | VARCHAR2 | 60 |  |  | DISPLAY_PERIOD_TYPE |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TIME_PERIOD_TYPES_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_TIME_PERIOD_TYPES_PK | Unique | Default | PERIOD_TYPE, ORA_SEED_SET1 |
| PAY_TIME_PERIOD_TYPES_PK1 | Unique | Default | PERIOD_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
