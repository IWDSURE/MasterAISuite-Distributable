# PAY_RULES_F

This table contains business rule definitions, which generate fast formulas to extend basic validation for costing override rules.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrulesf-29206.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrulesf-29206.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RULES_F_PK | RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RULE_SEQUENCE | NUMBER |  | 18 |  | RULE_SEQUENCE |
| RULE_NAME | VARCHAR2 | 100 |  |  | RULE_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| APPLY_TO_BALANCE_ACCOUNT | VARCHAR2 | 10 |  |  | APPLY_TO_BALANCE_ACCOUNT |
| APPLY_TO_COST_ACCOUNT | VARCHAR2 | 10 |  |  | APPLY_TO_COST_ACCOUNT |
| APPLY_TO_OVERRIDE_ACCOUNT | VARCHAR2 | 10 |  |  | APPLY_TO_OVERRIDE_ACCOUNT |
| RULE_SOURCE_TYPE | VARCHAR2 | 22 |  | Yes | RULE_SOURCE_TYPE |
| RULE_SOURCE_ID | NUMBER |  | 18 |  | RULE_SOURCE_ID |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RULES_F_N1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_RULES_F_PK | Unique | Default | RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
