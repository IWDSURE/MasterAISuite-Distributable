# PAY_FORMULA_RESULT_RULES_F

This table contains the rules that control what happens to the results produced by a specific formula calculation. When a formula is attached to an element by a status processing rule, it may produce results. The formula result rules for an element determine the destination of those results.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payformularesultrulesf-23675.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payformularesultrulesf-23675.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FORMULA_RESULT_RULES_F_PK | FORMULA_RESULT_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_RESULT_RULE_ID | NUMBER |  | 18 | Yes | FORMULA_RESULT_RULE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| STATUS_PROCESSING_RULE_ID | NUMBER |  | 18 |  | STATUS_PROCESSING_RULE_ID |
| AUTO_INDIRECT_ID | NUMBER |  | 18 |  | Auto Indirect |
| RESULT_NAME | VARCHAR2 | 80 |  | Yes | RESULT_NAME |
| RESULT_RULE_TYPE | VARCHAR2 | 30 |  | Yes | RESULT_RULE_TYPE |
| SEVERITY_LEVEL | VARCHAR2 | 1 |  |  | SEVERITY_LEVEL |
| TARGET_LEVEL | VARCHAR2 | 1 |  |  | TARGET_LEVEL |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| CONTEXT_ID | NUMBER |  | 18 |  | Identifier for the context. Foreign key to FF_CONTEXTS. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_FORMULA_RESULT_RULES_F_N1 | Non Unique | Default | STATUS_PROCESSING_RULE_ID |
| PAY_FORMULA_RESULT_RULES_F_N2 | Non Unique | Default | ELEMENT_TYPE_ID |
| PAY_FORMULA_RESULT_RULES_F_N3 | Non Unique | Default | INPUT_VALUE_ID |
| PAY_FORMULA_RESULT_RULES_F_N4 | Non Unique | Default | AUTO_INDIRECT_ID |
| PAY_FORMULA_RESULT_RULES_F_PK | Unique | Default | FORMULA_RESULT_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_FORMULA_RESULT_RULES_F_PK1 | Unique | Default | FORMULA_RESULT_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_FORMULA_RESULT_RULES_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
