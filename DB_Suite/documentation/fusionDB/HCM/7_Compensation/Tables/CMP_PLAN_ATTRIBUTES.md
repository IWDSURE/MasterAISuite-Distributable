# CMP_PLAN_ATTRIBUTES

Stores column defaulting and property information for a plan.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanattributes-18607.html#cmpplanattributes-18607](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanattributes-18607.html#cmpplanattributes-18607)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLAN_ATTRIBUTES_PK | PLAN_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | PLAN_ATTRIBUTE_ID |
| ZERO_AS_ALLOCATED_FLAG | VARCHAR2 | 1 |  |  | ZERO_AS_ALLOCATED_FLAG |
| EXT_RECORD_TYPE | VARCHAR2 | 30 |  |  | EXT_RECORD_TYPE |
| EXT_COLUMN | VARCHAR2 | 30 |  |  | EXT_COLUMN |
| LONG_TEXT_FLAG | VARCHAR2 | 1 |  |  | LONG_TEXT_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| DISPLAY_TOTAL_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_TOTAL_FLAG |
| REFRESH_DEFAULT_FLAG | VARCHAR2 | 1 |  |  | REFRESH_DEFAULT |
| PERSISTENT_FLAG | VARCHAR2 | 1 |  |  | PERSISTENT_FLAG |
| REFERENCE_PLAN_ID | NUMBER |  | 18 |  | REFERENCE_PLAN_ID |
| REFERENCE_PERIOD_CODE | VARCHAR2 | 30 |  |  | REFERENCE_PERIOD_CODE |
| REFERENCE_ITEM_NAME | VARCHAR2 | 60 |  |  | REFERENCE_ITEM_NAME |
| REFERENCE_ENABLED_FLAG | VARCHAR2 | 1 |  |  | REFERENCE_ENABLED_FLAG |
| DATA_TYPE | VARCHAR2 | 1 |  |  | DATA_TYPE |
| ATTRIBUTE_DELETED_FLAG | VARCHAR2 | 1 |  |  | ATTRIBUTE_DELETED_FLAG |
| ITEM_NAME_BUDGET | VARCHAR2 | 60 |  |  | ITEM_NAME_BUDGET |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_NAME |
| ITEM_NAME | VARCHAR2 | 60 |  |  | ITEM_NAME |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| POOL_ID | NUMBER |  | 18 |  | POOL_ID |
| STANDARD_RATE_ID | NUMBER |  | 18 |  | STANDARD_RATE_ID |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |
| DERIVED_FACTOR_ID | NUMBER |  | 18 |  | DERIVED_FACTOR_ID |
| DEFAULT_NUM | NUMBER |  |  |  | DEFAULT_NUM |
| DEFAULT_CHAR | VARCHAR2 | 30 |  |  | DEFAULT_CHAR |
| DEFAULT_DATE | DATE |  |  |  | DEFAULT_DATE |
| ROUNDING_CODE | VARCHAR2 | 30 |  |  | ROUNDING_CODE |
| DATE_CODE | VARCHAR2 | 30 |  |  | DATE_CODE |
| NUMBER_OF_DECIMALS | NUMBER |  |  |  | NUMBER_OF_DECIMALS |
| THOUSAND_SEPARATOR_FLAG | VARCHAR2 | 1 |  |  | THOUSAND_SEPARATOR_FLAG |
| MONETARY_FLAG | VARCHAR2 | 1 |  |  | MONETARY_FLAG |
| AUDIT_FLAG | VARCHAR2 | 1 |  |  | AUDIT_FLAG |
| COMP_TYPE | VARCHAR2 | 30 |  |  | COMP_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OVERRIDE_LOOKUP_FLAG | VARCHAR2 | 1 |  |  | OVERRIDE_LOOKUP_FLAG |
| CUSTOM_LOOKUP_TYPE_NAME | VARCHAR2 | 30 |  |  | CUSTOM_LOOKUP_TYPE_NAME |
| USE_CURRENCY_DECIMALS_FLAG | VARCHAR2 | 1 |  |  | USE_CURRENCY_DECIMALS_FLAG |
| USE_CURRENCY_ROUNDING_FLAG | VARCHAR2 | 1 |  |  | USE_CURRENCY_ROUNDING_FLAG |
| UPDATE_COND_CODE | VARCHAR2 | 30 |  |  | UPDATE_COND_CODE |
| ASG_SEG_TOTALS_COL_FLAG | VARCHAR2 | 1 |  |  | ASG_SEG_TOTALS_COL_FLAG |
| AUDIT_DIFF_FLAG | VARCHAR2 | 1 |  |  | AUDIT_DIFF_FLAG |
| CUSTOM_COMPONENT_ID | NUMBER |  | 18 |  | CUSTOM_COMPONENT_ID |
| COUNTRY_DISP_TYPE | VARCHAR2 | 30 |  |  | COUNTRY_DISP_TYPE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLAN_ATTRIBUTES_N1 | Non Unique | Default | PLAN_ID, ATTRIBUTE_NAME |
| CMP_PLAN_ATTRIBUTES_N2 | Non Unique | Default | COMPONENT_ID, ATTRIBUTE_NAME |
| CMP_PLAN_ATTRIBUTES_N3 | Non Unique | Default | POOL_ID, ATTRIBUTE_NAME |
| CMP_PLAN_ATTRIBUTES_N4 | Non Unique | Default | REFERENCE_PLAN_ID |
| CMP_PLAN_ATTRIBUTES_N5 | Non Unique | Default | COMP_TYPE |
| CMP_PLAN_ATTRIBUTES_N6 | Non Unique | Default | ITEM_NAME, PLAN_ID |
| CMP_PLAN_ATTRIBUTES_UK1 | Unique | Default | PLAN_ATTRIBUTE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
