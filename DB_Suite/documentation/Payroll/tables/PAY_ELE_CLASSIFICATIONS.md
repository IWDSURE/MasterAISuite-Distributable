# PAY_ELE_CLASSIFICATIONS

This table contains element classifications that define groups of elements for legislative and informational needs. Primary classifications are specific to a legislation and are predefined for all supported payroll legislations. Secondary or sub-classifications are specific to a legislative group and may be predefined for a specific legislation. Secondary classifications can be associated with an element to manage taxability rules.All types of classifications have a role in creating balance feeds automatically when balances and elements are created.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeleclassifications-27962.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeleclassifications-27962.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_CLASSIFICATIONS_PK | CLASSIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASSIFICATION_ID | NUMBER |  | 18 | Yes | CLASSIFICATION_ID |
| DATE_FROM | DATE |  |  | Yes | DATE_FROM |
| DATE_TO | DATE |  |  |  | DATE_TO |
| BASE_CLASSIFICATION_NAME | VARCHAR2 | 160 |  | Yes | BASE_CLASSIFICATION_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| NON_PAYMENTS_FLAG | VARCHAR2 | 30 |  |  | NON_PAYMENTS_FLAG |
| DEFAULT_LOW_PRIORITY | NUMBER |  | 9 |  | DEFAULT_LOW_PRIORITY |
| DEFAULT_PRIORITY | NUMBER |  | 9 |  | DEFAULT_PRIORITY |
| DEFAULT_HIGH_PRIORITY | NUMBER |  | 9 |  | DEFAULT_HIGH_PRIORITY |
| COSTABLE_FLAG | VARCHAR2 | 30 |  |  | COSTABLE_FLAG |
| COSTING_DEBIT_OR_CREDIT | VARCHAR2 | 30 |  |  | COSTING_DEBIT_OR_CREDIT |
| DISTRIBUTABLE_OVER_FLAG | VARCHAR2 | 30 |  |  | DISTRIBUTABLE_OVER_FLAG |
| FREQ_RULE_ENABLED | VARCHAR2 | 30 |  |  | FREQ_RULE_ENABLED |
| PROCESS_WHEN_EARNING | VARCHAR2 | 30 |  |  | PROCESS_WHEN_EARNING |
| PARENT_CLASSIFICATION_ID | NUMBER |  | 18 |  | PARENT_CLASSIFICATION_ID |
| SECONDARY_CLASSIFICATION_FLAG | VARCHAR2 | 30 |  |  | SECONDARY_CLASSIFICATION_FLAG |
| CREATE_BY_DEFAULT_FLAG | VARCHAR2 | 30 |  |  | CREATE_BY_DEFAULT_FLAG |
| BASE_CLASSIFICATION_ID | NUMBER |  | 18 |  | BASE_CLASSIFICATION_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PEC_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: category. |
| PEC_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION3 | VARCHAR2 | 150 |  |  | PEC_INFORMATION3 |
| PEC_INFORMATION4 | VARCHAR2 | 150 |  |  | PEC_INFORMATION4 |
| PEC_INFORMATION5 | VARCHAR2 | 150 |  |  | PEC_INFORMATION5 |
| PEC_INFORMATION6 | VARCHAR2 | 150 |  |  | PEC_INFORMATION6 |
| PEC_INFORMATION7 | VARCHAR2 | 150 |  |  | PEC_INFORMATION7 |
| PEC_INFORMATION8 | VARCHAR2 | 150 |  |  | PEC_INFORMATION8 |
| PEC_INFORMATION9 | VARCHAR2 | 150 |  |  | PEC_INFORMATION9 |
| PEC_INFORMATION10 | VARCHAR2 | 150 |  |  | PEC_INFORMATION10 |
| PEC_INFORMATION11 | VARCHAR2 | 150 |  |  | PEC_INFORMATION11 |
| PEC_INFORMATION12 | VARCHAR2 | 150 |  |  | PEC_INFORMATION12 |
| PEC_INFORMATION13 | VARCHAR2 | 150 |  |  | PEC_INFORMATION13 |
| PEC_INFORMATION14 | VARCHAR2 | 150 |  |  | PEC_INFORMATION14 |
| PEC_INFORMATION15 | VARCHAR2 | 150 |  |  | PEC_INFORMATION15 |
| PEC_INFORMATION16 | VARCHAR2 | 150 |  |  | PEC_INFORMATION16 |
| PEC_INFORMATION17 | VARCHAR2 | 150 |  |  | PEC_INFORMATION17 |
| PEC_INFORMATION18 | VARCHAR2 | 150 |  |  | PEC_INFORMATION18 |
| PEC_INFORMATION19 | VARCHAR2 | 150 |  |  | PEC_INFORMATION19 |
| PEC_INFORMATION20 | VARCHAR2 | 150 |  |  | PEC_INFORMATION20 |
| PEC_INFORMATION21 | VARCHAR2 | 150 |  |  | PEC_INFORMATION21 |
| PEC_INFORMATION22 | VARCHAR2 | 150 |  |  | PEC_INFORMATION22 |
| PEC_INFORMATION23 | VARCHAR2 | 150 |  |  | PEC_INFORMATION23 |
| PEC_INFORMATION24 | VARCHAR2 | 150 |  |  | PEC_INFORMATION24 |
| PEC_INFORMATION25 | VARCHAR2 | 150 |  |  | PEC_INFORMATION25 |
| PEC_INFORMATION26 | VARCHAR2 | 150 |  |  | PEC_INFORMATION26 |
| PEC_INFORMATION27 | VARCHAR2 | 150 |  |  | PEC_INFORMATION27 |
| PEC_INFORMATION28 | VARCHAR2 | 150 |  |  | PEC_INFORMATION28 |
| PEC_INFORMATION29 | VARCHAR2 | 150 |  |  | PEC_INFORMATION29 |
| PEC_INFORMATION30 | VARCHAR2 | 20 |  |  | PEC_INFORMATION30 |
| PEC_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| PEC_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELE_CLASSIFICATIONS_N1 | Non Unique | Default | PARENT_CLASSIFICATION_ID |
| PAY_ELE_CLASSIFICATIONS_N2 | Non Unique | Default | BASE_CLASSIFICATION_ID, LEGISLATION_CODE |
| PAY_ELE_CLASSIFICATIONS_N3 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_ELE_CLASSIFICATIONS_PK | Unique | Default | CLASSIFICATION_ID, ORA_SEED_SET1 |
| PAY_ELE_CLASSIFICATIONS_PK1 | Unique | Default | CLASSIFICATION_ID, ORA_SEED_SET2 |
| PAY_ELE_CLASSIFICATIONS_U1 | Unique | Default | BASE_CLASSIFICATION_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_ELE_CLASSIFICATIONS_U11 | Unique | Default | BASE_CLASSIFICATION_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
