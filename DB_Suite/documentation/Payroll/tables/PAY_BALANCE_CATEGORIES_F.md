# PAY_BALANCE_CATEGORIES_F

This table contains balance category definitions, which are independent subsets of balance types.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancecategoriesf-5602.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancecategoriesf-5602.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_CATEGORIES_F_PK | BALANCE_CATEGORY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| BALANCE_CATEGORY_ID | NUMBER |  | 18 | Yes | BALANCE_CATEGORY_ID |  |
| BASE_CATEGORY_NAME | VARCHAR2 | 30 |  | Yes | BASE_CATEGORY_NAME |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BASE_BALANCE_CATEGORY_ID | NUMBER |  | 18 |  | BASE_BALANCE_CATEGORY_ID |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SAVE_RUN_BALANCE_ENABLED | VARCHAR2 | 30 |  |  | SAVE_RUN_BALANCE_ENABLED |  |
| APPLICATION_ID | NUMBER |  | 18 |  | Application ID for the application that owns the Category |  |
| PBC_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | PBC_INFORMATION_CATEGORY | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| PBC_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Balance Category Information (PAY_BALANCE_CATEGORIES_DDF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BALANCE_CATEGORIES_F_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_BALANCE_CATEGORIES_F_N2 | Non Unique | Default | BASE_BALANCE_CATEGORY_ID, LEGISLATION_CODE |
| PAY_BALANCE_CATEGORIES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_BALANCE_CATEGORIES_F_PK | Unique | Default | BALANCE_CATEGORY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_BALANCE_CATEGORIES_F_PK1 | Unique | Default | BALANCE_CATEGORY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_BALANCE_CATEGORIES_F_U1 | Unique | Default | BASE_CATEGORY_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_BALANCE_CATEGORIES_F_U11 | Unique | Default | BASE_CATEGORY_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
