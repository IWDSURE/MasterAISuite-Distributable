# PAY_VALUE_INSTS_F

This table contains details of how a value is calculated in payroll processing using range items, calculation types, and allowed overrides.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvalueinstsf-21666.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvalueinstsf-21666.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_VALUE_INSTS_F_PK | VALUE_INST_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VALUE_INST_ID | NUMBER |  | 18 | Yes | VALUE_INST_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CALC_TYPE_ID | NUMBER |  | 18 | Yes | CALC_TYPE_ID |
| PARENT_VALUE_DEFN_ID | NUMBER |  | 18 |  | PARENT_VALUE_DEFN_ID |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| DIR_OVERRIDE_USAGE_ID | NUMBER |  | 18 |  | DIR_OVERRIDE_USAGE_ID |
| OVERRIDE_VALUE | VARCHAR2 | 60 |  |  | Value of an Override |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | CURRENCY_CODE |
| UOM | VARCHAR2 | 30 |  |  | Unit of Measure |
| PERIODICITY | VARCHAR2 | 30 |  |  | PERIODICITY |
| PERIODICITY_TYPE | VARCHAR2 | 5 |  |  | This denotes the type of the periodicity. For example is it time based, Annually, Monthly, etc or unit based, widgets, meals, etc. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_VALUE_INSTS_F_N1 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_VALUE_INSTS_F_N2 | Non Unique | Default | SOURCE_ID, LEGISLATION_CODE |
| PAY_VALUE_INSTS_F_N20 | Non Unique | Default | EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_VALUE_INSTS_F_N5 | Non Unique | Default | PARENT_VALUE_DEFN_ID, SOURCE_ID, SOURCE_TYPE |
| PAY_VALUE_INSTS_F_PK | Unique | Default | VALUE_INST_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
