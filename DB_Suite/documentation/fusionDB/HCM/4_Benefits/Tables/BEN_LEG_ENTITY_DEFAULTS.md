# BEN_LEG_ENTITY_DEFAULTS

BEN_LEG_ENTITY_DEFAULTS stores legal entity default setup for default and unrestricted relationships.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlegentitydefaults-11035.html#benlegentitydefaults-11035](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlegentitydefaults-11035.html#benlegentitydefaults-11035)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LEG_ENTITY_DEFAULTS_PK | LEG_ENTITY_DEFAULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| LEG_ENTITY_DEFAULT_ID | NUMBER |  | 18 | Yes | LEG_ENTITY_DEFAULT_ID |  |
| DATE_FROM | DATE |  |  | Yes | DATE_FROM |  |
| DATE_TO | DATE |  |  | Yes | DATE_TO |  |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| MULTI_ASSIGNMENT_FLAG | VARCHAR2 | 30 |  |  | MULTI_ASSIGNMENT_FLAG |  |
| BENEFIT_RELATION_NAME | VARCHAR2 | 30 |  |  | BENEFIT_RELATION_NAME |  |
| ADD_ASGN_TREAT_CD | VARCHAR2 | 30 |  |  | ADD_ASGN_TREAT_CD |  |
| ADD_PRI_ASGN_TREAT_CD | VARCHAR2 | 30 |  |  | ADD_PRI_ASGN_TREAT_CD |  |
| TERM_PRI_ASGN_TREAT_CD | VARCHAR2 | 30 |  |  | TERM_PRI_ASGN_TREAT_CD |  |
| DEFAULT_PAYROLL_ID | NUMBER |  | 18 |  | DEFAULT_PAYROLL_ID |  |
| BENEFIT_ASGN_CREATE_CD | VARCHAR2 | 30 |  |  | BENEFIT_ASGN_CREATE_CD |  |
| LED_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | LED_ATTRIBUTE_CATEGORY | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE1 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE2 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE3 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE4 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE5 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE6 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE7 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE8 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE9 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE10 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE11 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE12 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE13 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE14 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE15 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE16 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE17 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE18 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE19 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE20 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE21 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE22 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE23 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE24 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE25 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE26 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE27 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE28 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE29 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | LED_ATTRIBUTE30 | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LED_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legal Entity Default Attributes (BEN_LEG_ENTITY_DEFAULTS_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PRODUCT_CD | VARCHAR2 | 30 |  | Yes | PRODUCT_CD |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |  |
| CREATE_FOR | VARCHAR2 | 30 |  |  | CREATE_FOR |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LEG_ENTITY_DEFAULTS_FK1 | Non Unique | Default | LEGAL_ENTITY_ID |
| BEN_LEG_ENTITY_DEFAULTS_PK | Unique | Default | LEG_ENTITY_DEFAULT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
