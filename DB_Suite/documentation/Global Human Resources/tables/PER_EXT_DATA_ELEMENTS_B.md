# PER_EXT_DATA_ELEMENTS_B

Data Elements used in extracts.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdataelementsb-7662.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdataelementsb-7662.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_DATA_ELEMENTS_B_PK | EXT_DATA_ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| EXT_DATA_ELEMENT_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |  |
| UPDATABLE_DATA_ELEMENT | VARCHAR2 | 30 |  |  | Determines if Data element can be updated in Results UI |  |
| VO_NAME | VARCHAR2 | 400 |  |  | VO_NAME - To show meaningful information instead showing ID values in Result UI |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| BASE_DATA_ELEMENT_NAME | VARCHAR2 | 80 |  |  | Base Name of the Data Element |  |
| START_DATE | DATE |  |  |  | The date from which the data element is active. |  |
| END_DATE | DATE |  |  |  | The date till when the data element is active. |  |
| REPORT_RECORD_ID | NUMBER |  | 18 |  | The record id of the data element |  |
| XML_TAG_NAME | VARCHAR2 | 80 |  |  | XML Tag Name of data element |  |
| SHORT_CODE | VARCHAR2 | 30 |  |  | Short Code for the extract data element. |  |
| TYPE_CODE | VARCHAR2 | 30 |  |  | Data Element type eg: DBI Group, Rule, etc. |  |
| DATA_TYPE | VARCHAR2 | 80 |  |  | Data Type of the Data Element |  |
| DBI_GROUP_ID | NUMBER |  | 18 |  | Database Item Group Id for Database Item Group type data element |  |
| RULE_ID | NUMBER |  | 18 |  | Fast Formula Id for Rule Type data element |  |
| EXT_PARAM_ID | NUMBER |  | 18 |  | Parameter Id for Parameter type data element |  |
| STRING_VALUE | VARCHAR2 | 300 |  |  | The value of String for string type data element |  |
| GROUP_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Group function code, eg; SUM, COUNT, MIN, etc |  |
| GROUP_RECORD_ID | NUMBER |  | 18 |  | Record Id for group type data element |  |
| GROUP_DATA_ELEMENT_ID | NUMBER |  | 18 |  | Data Element Id for group type data element |  |
| FUNCTION_EXPRESSION | VARCHAR2 | 2000 |  |  | Function expression relating to conditional grouping, calculation element or decode values |  |
| TRANSFORMED_EXPRESSION | VARCHAR2 | 2000 |  |  | Transformed expression: conditional grouping expression transformed into equivalent SQL |  |
| DEFAULT_VALUE | VARCHAR2 | 600 |  |  | Default value for data element |  |
| REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Data Element Required Flag |  |
| HIDE_FLAG | VARCHAR2 | 30 |  |  | Data Element Hide flag |  |
| UI_HIDE_FLAG | VARCHAR2 | 30 |  |  | Determines whether this data element's value is shown in the Results UI or not. |  |
| CONTEXT_FLAG | VARCHAR2 | 30 |  |  | Decides whether the data element is a context or not. Based on this View Archive Result UI will display the value in different region |  |
| MARK_AS_CHANGED | VARCHAR2 | 30 |  |  | This flag indicates that this data element has to be processed and displayed in report irrespective of whether it is changed or not. |  |
| KEY_FLAG | VARCHAR2 | 30 |  |  | This flag identifies if this data element is a unique key data element in the record. |  |
| INFORMATION_LABEL | VARCHAR2 | 80 |  |  | UI Prompt /Label |  |
| INFORMATION_COLUMN | NUMBER |  | 30 |  | Pay_Action_Information column number |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Extract Data Element Attributes (PER_EXT_DATA_ELEMENTS_DFF) |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_DATA_ELEMENTS_B_FK1 | Non Unique | Default | REPORT_RECORD_ID, BASE_DATA_ELEMENT_NAME |
| PER_EXT_DATA_ELEMENTS_B_N20 | Non Unique | Default | SGUID |
| PER_EXT_DATA_ELEMENTS_B_PK | Unique | Default | EXT_DATA_ELEMENT_ID, ORA_SEED_SET1 |
| PER_EXT_DATA_ELEMENTS_B_PK1 | Unique | Default | EXT_DATA_ELEMENT_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
