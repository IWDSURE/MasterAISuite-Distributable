# PAY_ELEMENT_LINKS_F

This table contains the eligibility rules that link elements to groups of employees. An assignment must match the eligibility criteria defined for the element link before it can have an entry of that element. Default values for the element input values can be set or overridden for each link. The criteria values themselves are not held on the element link entity directly. Instead, these are held on a criteria combination table (PAY_ELEMENT_CRITERIA).

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementlinksf-9080.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementlinksf-9080.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_LINKS_F_PK | ELEMENT_LINK_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELEMENT_LINK_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_TYPES_F. |  |
| STANDARD_LINK_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether an element is standard (Y) or non-standard (N). |  |
| ELEMENT_CRITERIA_ID | NUMBER |  | 18 | Yes | ELEMENT_CRITERIA_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ELEMENT_LINK_NAME | VARCHAR2 | 80 |  |  | ELEMENT_LINK_NAME |  |
| STARTING_TIME_DEF_ID | NUMBER |  | 18 |  | STARTING_TIME_DEF_ID |  |
| ENDING_TIME_DEF_ID | NUMBER |  | 18 |  | ENDING_TIME_DEF_ID |  |
| DEFAULTING_FORMULA_ID | NUMBER |  | 18 |  | DEFAULTING_FORMULA_ID |  |
| CALCULATION_FORMULA_ID | NUMBER |  | 18 |  | CALCULATION_FORMULA_ID |  |
| VALIDATION_FORMULA_ID | NUMBER |  | 18 |  | VALIDATION_FORMULA_ID |  |
| VALIDATION_OVERRIDE_MESSAGE | VARCHAR2 | 30 |  |  | VALIDATION_OVERRIDE_MESSAGE |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Link Attributes (PAY_ELEMENT_LINKS_DFF) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| COSTING_LINK_FLAG | VARCHAR2 | 30 |  |  | Used to identify a special costing eligibility. The default value for this will be null, in which case it is a "normal" eligibility. If it contains the value 'Y', then it is considered to be a special costing link. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELEMENT_LINKS_F_N1 | Non Unique | Default | ELEMENT_CRITERIA_ID |
| PAY_ELEMENT_LINKS_F_N2 | Non Unique | Default | ELEMENT_TYPE_ID |
| PAY_ELEMENT_LINKS_F_N3 | Non Unique | Default | UPPER("ELEMENT_LINK_NAME") |
| PAY_ELEMENT_LINKS_F_PK | Unique | Default | ELEMENT_LINK_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
