# PAY_DIR_OVERRIDE_USAGES_F

This table contains the overrides for a particular card component, with the values that can be set for that override.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydiroverrideusagesf-16213.html#paydiroverrideusagesf-16213](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydiroverrideusagesf-16213.html#paydiroverrideusagesf-16213)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_OVERRIDE_USAGES_F_PK | DIR_OVERRIDE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_OVERRIDE_USAGE_ID | NUMBER |  | 18 | Yes | DIR_OVERRIDE_USAGE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DIR_CARD_COMP_DEF_ID | NUMBER |  | 18 | Yes | DIR_CARD_COMP_DEF_ID |
| ALLOW_OVERRIDES_ID | NUMBER |  | 18 | Yes | ALLOW_OVERRIDES_ID |
| CONTEXT_VALUE1 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE1 |
| CONTEXT_VALUE2 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE2 |
| CONTEXT_VALUE3 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE3 |
| CONTEXT_VALUE4 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE4 |
| CONTEXT_VALUE5 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE5 |
| CONTEXT_VALUE6 | VARCHAR2 | 150 |  |  | CONTEXT_VALUE6 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| VO_NAME | VARCHAR2 | 100 |  |  | VALUE_SET_ID |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | DISPLAY_SEQUENCE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| DISPLAY_FLAG | VARCHAR2 | 4 |  |  | DISPLAY_FLAG |
| DEFAULT_VALUE | VARCHAR2 | 150 |  |  | DEFAULT_VALUE |
| ENABLE_FLAG | VARCHAR2 | 4 |  |  | ENABLE_FLAG |
| RESOLVER_TYPE | VARCHAR2 | 32 |  |  | RESOLVER_TYPE |
| RESOLVER_IDENTIFIER | VARCHAR2 | 4000 |  |  | RESOLVER_IDENTIFIER |
| DISPLAY_TYPE | VARCHAR2 | 32 |  |  | DISPLAY_TYPE |
| SPECIAL_PURPOSE | VARCHAR2 | 30 |  |  | SPECIAL_PURPOSE |
| DISPLAY_ATTR_LIST | VARCHAR2 | 240 |  |  | DISPLAY_ATTR_LIST |
| RETURN_ATTR_NAME | VARCHAR2 | 100 |  |  | RETURN_ATTR_NAME |
| LIST_VIEW_CRIT_LIST | VARCHAR2 | 500 |  |  | LIST_VIEW_CRIT_LIST |
| LIST_BIND_MAP | VARCHAR2 | 4000 |  |  | LIST_BIND_MAP |
| LIST_QUERY_CRITERIA | VARCHAR2 | 240 |  |  | LIST_QUERY_CRITERIA |
| GROUP_TEXT_TYPE | VARCHAR2 | 32 |  |  | GROUP_TEXT_TYPE |
| GROUP_TEXT_IDENTIFIER | VARCHAR2 | 150 |  |  | GROUP_TEXT_IDENTIFIER |
| LABEL_TEXT_TYPE | VARCHAR2 | 32 |  |  | LABEL_TEXT_TYPE |
| LABEL_TEXT_IDENTIFIER | VARCHAR2 | 150 |  |  | LABEL_TEXT_IDENTIFIER |
| GROUP_SEQUENCE | NUMBER | 18 |  |  | GROUP_SEQUENCE |
| HELP_TEXT_TYPE | VARCHAR2 | 32 |  |  | HELP_TEXT_TYPE |
| HELP_TEXT_IDENTIFIER | VARCHAR2 | 150 |  |  | HELP_TEXT_IDENTIFIER |
| CATEGORY_CODE | VARCHAR2 | 150 |  |  | CATEGORY_CODE |
| VALUE_SET_CODE | VARCHAR2 | 60 |  |  | VALUE_SET_CODE |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIR_OVERRIDE_USAGES_F_N1 | Non Unique | Default | DIR_CARD_COMP_DEF_ID, ALLOW_OVERRIDES_ID |
| PAY_DIR_OVERRIDE_USAGES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_OVERRIDE_USAGES_F_N3 | Non Unique | Default | DIR_CARD_COMP_DEF_ID, DISPLAY_TYPE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_OVERRIDE_USAGES_F_PK | Unique | Default | DIR_OVERRIDE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_DIR_OVERRIDE_USAGES_F_PK1 | Unique | Default | DIR_OVERRIDE_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
