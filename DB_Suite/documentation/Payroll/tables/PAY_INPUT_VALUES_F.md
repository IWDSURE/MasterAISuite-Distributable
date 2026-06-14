# PAY_INPUT_VALUES_F

This table contains the input values for an element. Each input value has a unit of measure and can have validations and conditions defined to control the data entry when the element is assigned to a person. For example, an earning element may have an input value for hours worked.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payinputvaluesf-22176.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payinputvaluesf-22176.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_INPUT_VALUES_F_PK | INPUT_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DISPLAY_SEQUENCE | NUMBER |  | 5 | Yes | Display sequence number for the input value. |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | Element Type Identifier |
| GENERATE_DB_ITEMS_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether database items are generated for the input values. |
| HOT_DEFAULT_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether the default value is a HOT default. . |
| MANDATORY_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the input value is required for an entry.  (Validated by a lookup). |
| USER_ENTERABLE_FLAG | VARCHAR2 | 1 |  | Yes | USER_ENTERABLE_FLAG |
| BASE_NAME | VARCHAR2 | 80 |  | Yes | BASE_NAME |
| UOM | VARCHAR2 | 30 |  | Yes | Unit of measure for the input value (hours, monetary amount, etc). |
| USER_DISPLAY_FLAG | VARCHAR2 | 30 |  | Yes | USER_DISPLAY_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RESERVED_INPUT_VALUE | VARCHAR2 | 30 |  |  | RESERVED_INPUT_VALUE |
| RETRO_STATIC_FLAG | VARCHAR2 | 30 |  |  | RETRO_STATIC_FLAG |
| FORCE_RRV_MODE | VARCHAR2 | 30 |  |  | FORCE_RRV_MODE |
| DEFAULT_VALUE | VARCHAR2 | 60 |  |  | Default for the input value on entry.  Value may be overridden for an element link, and for specific entries. |
| FORMULA_ID | NUMBER |  | 18 |  | Formula to generate the input value |
| RATE_FORMULA_ID | NUMBER |  | 18 |  | Formula used by the Rate Engine to calculate the Rate contribution amount. |
| VALIDATION_OVERRIDE_MESSAGE | VARCHAR2 | 30 |  |  | VALIDATION_OVERRIDE_MESSAGE |
| LOOKUP_TYPE | VARCHAR2 | 30 |  |  | List of allowable input values |
| MIN_VALUE | VARCHAR2 | 60 |  |  | Minimum value allowed on entry.  May be overridden at the element link. |
| MAX_VALUE | VARCHAR2 | 60 |  |  | Maximum value allowed on entry.  May be overridden at the element link. |
| VO_NAME | VARCHAR2 | 200 |  |  | View object name used to validate the input value |
| VALUE_SET_CODE | VARCHAR2 | 200 |  |  | VALUE_SET_CODE |
| WARNING_OR_ERROR | VARCHAR2 | 30 |  |  | Indicates the kind of message that is generated if the input value is not valid for min/max or formula validation. |
| CONTEXT_ID | NUMBER |  | 18 |  | Identifier for the context. Foreign key to FF_CONTEXTS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_INPUT_VALUES_F_N2 | Non Unique | Default | CONTEXT_ID, ELEMENT_TYPE_ID |
| PAY_INPUT_VALUES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_INPUT_VALUES_F_N50 | Non Unique | Default | ELEMENT_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_INPUT_VALUES_F_PK | Unique | Default | INPUT_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_INPUT_VALUES_F_PK1 | Unique | Default | INPUT_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_INPUT_VALUES_F_U1 | Unique | Default | ELEMENT_TYPE_ID, BASE_NAME, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_INPUT_VALUES_F_U11 | Unique | Default | ELEMENT_TYPE_ID, BASE_NAME, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
