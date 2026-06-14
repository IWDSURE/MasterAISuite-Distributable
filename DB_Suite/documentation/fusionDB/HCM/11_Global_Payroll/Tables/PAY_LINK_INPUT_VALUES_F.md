# PAY_LINK_INPUT_VALUES_F

This table contains input value settings for a specific link rule to override the definitions for the element. For example, each link can have its own default values and warning levels.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylinkinputvaluesf-23464.html#paylinkinputvaluesf-23464](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylinkinputvaluesf-23464.html#paylinkinputvaluesf-23464)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_LINK_INPUT_VALUES_F_PK | LINK_INPUT_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LINK_INPUT_VALUE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ELEMENT_LINK_ID | NUMBER |  | 18 | Yes | Element Link Value Identifier |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Input Value Identifier |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DEFAULT_VALUE | VARCHAR2 | 60 |  |  | Default for the input value on entry.  May be overridden for a specific element entry. |
| MIN_VALUE | VARCHAR2 | 60 |  |  | Minimum value allowed on entry.  May be overridden for a specific element entry. |
| MAX_VALUE | VARCHAR2 | 60 |  |  | Maximum value allowed on entry.  May be overridden for a specific element entry. |
| WARNING_OR_ERROR | VARCHAR2 | 30 |  |  | Indicates whether a warning or error message is generated if the input value is not valid for formula validation. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_LINK_INPUT_VALUES_F_N2 | Non Unique | Default | INPUT_VALUE_ID |
| PAY_LINK_INPUT_VALUES_F_PK | Unique | Default | LINK_INPUT_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_LINK_INPUT_VALUES_F_U50 | Unique | Default | ELEMENT_LINK_ID, INPUT_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
