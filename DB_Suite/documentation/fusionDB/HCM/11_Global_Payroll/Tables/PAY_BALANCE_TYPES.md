# PAY_BALANCE_TYPES

This table contains the definitions of balances used in calculations and reporting.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancetypes-13672.html#paybalancetypes-13672](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancetypes-13672.html#paybalancetypes-13672)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_TYPES_PK | BALANCE_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| BALANCE_TYPE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | Foreign key to FND_CURRENCIES. |  |
| BASE_BALANCE_NAME | VARCHAR2 | 80 |  | Yes | BASE_BALANCE_NAME |  |
| BALANCE_UOM | VARCHAR2 | 30 |  | Yes | Unit of measure, for example, Money. |  |
| REMUNERATION_FLAG | VARCHAR2 | 30 |  |  | REMUNERATION_FLAG |  |
| BALANCE_CATEGORY_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_BALANCE_CATEGORIES_F |  |
| BASE_BALANCE_TYPE_ID | NUMBER |  | 18 |  | Associated balance type to allow defined relationship |  |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_INPUT_VALUES_F for primary balance |  |
| APPLICATION_ID | NUMBER |  | 18 |  | Which non Payroll Application owns the record |  |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | DEDUCTION_TYPE_ID |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Balance Type Attributes (PAY_BALANCE_TYPES_DFF) |
| COMMENTS | CLOB |  |  |  | Descriptive information about the balance type. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| PBT_INFORMATION_CATEGORY | VARCHAR2 | 80 |  |  | Descriptive Flexfield: category. |  |
| PBT_INFORMATION_CHAR1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_CHAR30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| PBT_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BALANCE_TYPES_N1 | Non Unique | Default | INPUT_VALUE_ID |
| PAY_BALANCE_TYPES_PK | Unique | Default | BALANCE_TYPE_ID, ORA_SEED_SET1 |
| PAY_BALANCE_TYPES_PK1 | Unique | Default | BALANCE_TYPE_ID, ORA_SEED_SET2 |
| PAY_BALANCE_TYPES_U1 | Unique | Default | BASE_BALANCE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_BALANCE_TYPES_U11 | Unique | Default | BASE_BALANCE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
