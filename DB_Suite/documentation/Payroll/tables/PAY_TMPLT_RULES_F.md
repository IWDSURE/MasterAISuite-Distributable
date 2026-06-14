# PAY_TMPLT_RULES_F

This Table holds the Rule Information for The element Template Wizard

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulesf-12100.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulesf-12100.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_RULES_F_PK | RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RULE_NAME | VARCHAR2 | 30 |  | Yes | RULE_NAME |
| BASE_RULE_ID | NUMBER |  | 18 |  | BASE_RULE_ID |
| RULE_OPTIONS_TYPE | VARCHAR2 | 30 |  | Yes | RULE_OPTIONS_TYPE |
| RULE_OPTIONS_VALUE | VARCHAR2 | 250 |  |  | RULE_OPTIONS_VALUE |
| RULE_TYPE | VARCHAR2 | 5 |  | Yes | RULE_TYPE |
| RULE_DISPLAY_TYPE | VARCHAR2 | 5 |  | Yes | RULE_DISPLAY_TYPE |
| RULE_OPTION_ATTRIBUTE_ID | VARCHAR2 | 30 |  |  | RULE_OPTION_ATTRIBUTE_TYPE |
| RULE_OPTION_ATTRIBUTE_VALUE | VARCHAR2 | 30 |  |  | RULE_OPTION_ATTRIBUTE_VALUE |
| DEFAULT_VALUE | VARCHAR2 | 200 |  |  | Default Value for the rule |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TEMPLATE_ID | NUMBER |  | 18 |  | TEMPLATE_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | Indicates the global unique identifier. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TMPLT_RULES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_TMPLT_RULES_F_PK2 | Unique | Default | RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_TMPLT_RULES_F_PK21 | Unique | Default | RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_TMPLT_RULES_F_U2 | Unique | Default | RULE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_TMPLT_RULES_F_U21 | Unique | Default | RULE_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
