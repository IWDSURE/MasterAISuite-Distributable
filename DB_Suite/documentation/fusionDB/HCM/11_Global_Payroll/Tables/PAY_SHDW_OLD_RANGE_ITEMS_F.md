# PAY_SHDW_OLD_RANGE_ITEMS_F

This table contains the values or sets of values used in the calculation of a value definition. For example, for a value definition of total rate calculation type, ranges for rates of 0 to 1000 use 5 percent while rates of 1000 to 10000 use 10 percent.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payshdwoldrangeitemsf-8268.html#payshdwoldrangeitemsf-8268](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payshdwoldrangeitemsf-8268.html#payshdwoldrangeitemsf-8268)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_SHDW_RANGE_ITEMS_F_PK | RANGE_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANGE_ITEM_ID | NUMBER |  | 18 | Yes | RANGE_ITEM_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| VALUE_DEFN_ID | NUMBER |  | 18 | Yes | VALUE_DEFN_ID |
| LOW_VALUE | NUMBER |  | 32 |  | LOW_VALUE |
| LOW_VALUE_TEXT | VARCHAR2 | 256 |  |  | LOW_VALUE_TEXT |
| HIGH_VALUE | NUMBER |  | 32 |  | HIGH_VALUE |
| HIGH_VALUE_TEXT | VARCHAR2 | 256 |  |  | HIGH_VALUE_TEXT |
| CALC_TYPE_ID | NUMBER |  | 18 |  | CALC_TYPE_ID |
| VALUE1 | VARCHAR2 | 60 |  |  | VALUE1 |
| VALUE2 | VARCHAR2 | 60 |  |  | VALUE2 |
| VALUE3 | VARCHAR2 | 60 |  |  | VALUE3 |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_SHDW_OLD_RANGE_ITEMS_F_PK | Unique | Default | RANGE_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_SHDW_RANGE_ITEMS_F_FK1 | Non Unique | Default | VALUE_DEFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
