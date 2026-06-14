# PAY_BALANCE_DIMENSIONS

This table contains information allowing the summation of a balance.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancedimensions-11157.html#paybalancedimensions-11157](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancedimensions-11157.html#paybalancedimensions-11157)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_DIMENSIONS_PK | BALANCE_DIMENSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BALANCE_DIMENSION_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| APPLICATION_ID | NUMBER |  | 18 |  | Indicates which, non Payroll, application owns the record. |
| DIMENSION_LEVEL | VARCHAR2 | 30 |  | Yes | The level or group that the dimension describes |
| PERIOD_TYPE | VARCHAR2 | 30 |  | Yes | The period for which the dimension totals |
| ROUTE_ID | NUMBER |  | 18 | Yes | Foreign key to FF_ROUTES. |
| BASE_DB_ITEM_SUFFIX | VARCHAR2 | 80 |  | Yes | BASE_DB_ITEM_SUFFIX |
| BASE_DIMENSION_NAME | VARCHAR2 | 160 |  | Yes | BASE_DIMENSION_NAME |
| DIMENSION_TYPE | VARCHAR2 | 1 |  | Yes | Controls whether latest balance is created and if so, what type, person or assignment level. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | User Description. |
| PAYMENTS_FLAG | VARCHAR2 | 30 |  |  | One dimension only can be marked as being the PAYMENTS dimension. |
| EXPIRY_CHECKING_LEVEL | VARCHAR2 | 1 |  |  | Controls balance expiry strategy. |
| FEED_CHECKING_TYPE | VARCHAR2 | 1 |  |  | Controls feed checking strategy. |
| ASG_ACTION_BALANCE_DIM_ID | NUMBER |  | 18 |  | Used to calculate assignment contributions to group balance in rollback of group level run balances. |
| SAVE_RUN_BALANCE_ENABLED | VARCHAR2 | 30 |  |  | In conjunction with save_run_balance_enabled on pay_balance_categories_f, indicates whether run balances should be stored for defined balances with this dimension. |
| INITIAL_DATE | DATE |  |  |  | INITIAL_DATE |
| INITIAL_TIME_DEF_ID | NUMBER |  | 18 |  | INITIAL_TIME_DEF_ID |
| START_TIME_DEF_ID | NUMBER |  | 18 |  | START_TIME_DEF_ID |
| END_TIME_DEF_ID | NUMBER |  | 18 |  | END_TIME_DEF_ID |
| EXPIRY_TIME_DEF_ID | NUMBER |  | 18 |  | EXPIRY_TIME_DEF_ID |
| TIME_PERIOD_ID | NUMBER |  | 18 |  | TIME_PERIOD_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BALANCE_DIMENSIONS_PK | Unique | Default | BALANCE_DIMENSION_ID, ORA_SEED_SET1 |
| PAY_BALANCE_DIMENSIONS_PK1 | Unique | Default | BALANCE_DIMENSION_ID, ORA_SEED_SET2 |
| PAY_BALANCE_DIMENSIONS_UK1 | Unique | Default | BASE_DIMENSION_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_BALANCE_DIMENSIONS_UK11 | Unique | Default | BASE_DIMENSION_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |
| PAY_BALANCE_DIMENSIONS_UK2 | Unique | Default | BASE_DB_ITEM_SUFFIX, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_BALANCE_DIMENSIONS_UK21 | Unique | Default | BASE_DB_ITEM_SUFFIX, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
