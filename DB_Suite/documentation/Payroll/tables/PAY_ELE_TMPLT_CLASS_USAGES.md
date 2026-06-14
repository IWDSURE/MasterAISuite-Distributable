# PAY_ELE_TMPLT_CLASS_USAGES

This table contains information about which element templates are applicable for each element classification. For example, the flat amount calculation template is only applicable for earnings classifications.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeletmpltclassusages-20188.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeletmpltclassusages-20188.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_TMPLT_CLASS_USAGES_PK | ELE_TEMPLATE_CLASSIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELE_TEMPLATE_CLASSIFICATION_ID | NUMBER |  | 18 | Yes | ELE_TEMPLATE_CLASSIFICATION_ID |
| CLASSIFICATION_ID | NUMBER |  | 18 | Yes | CLASSIFICATION_ID |
| SECONDARY_CLASSIFICATION_ID | NUMBER |  | 18 |  | SECONDARY_CLASSIFICATION_ID |
| CATEGORY | VARCHAR2 | 30 |  |  | CATEGORY |
| BASE_CALCULATION_RULE_NAME | VARCHAR2 | 250 |  |  | BASE_CALCULATION_RULE_NAME |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | TEMPLATE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| PAYROLL_LICENSE | VARCHAR2 | 30 |  |  | PAYROLL_LICENSE |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELE_TMPLT_CLASS_USAGES_PK | Unique | Default | ELE_TEMPLATE_CLASSIFICATION_ID, ORA_SEED_SET1 |
| PAY_ELE_TMPLT_CLASS_USAGES_PK1 | Unique | Default | ELE_TEMPLATE_CLASSIFICATION_ID, ORA_SEED_SET2 |
| PAY_ELE_TMPLT_CLASS_USAGES_UK2 | Unique | Default | CLASSIFICATION_ID, TEMPLATE_ID, SECONDARY_CLASSIFICATION_ID, LEGISLATION_CODE, PAYROLL_LICENSE, ORA_SEED_SET1 |
| PAY_ELE_TMPLT_CLASS_USAGE_N20 | Non Unique | Default | SGUID |
| PAY_ELE_TMPLT_CLASS_USAGE_UK21 | Unique | Default | CLASSIFICATION_ID, TEMPLATE_ID, SECONDARY_CLASSIFICATION_ID, LEGISLATION_CODE, PAYROLL_LICENSE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
