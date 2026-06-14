# PAY_OLD_RANGE_ITEMS_F_

This table contains the values or sets of values used in the calculation of a value definition. For example, for a value definition of total rate calculation type, ranges for rates of 0 to 1000 use 5 percent while rates of 1000 to 10000 use 10 percent.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payoldrangeitemsf-20214.html#payoldrangeitemsf-20214](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payoldrangeitemsf-20214.html#payoldrangeitemsf-20214)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RANGE_ITEMS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, RANGE_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANGE_ITEM_ID | NUMBER |  | 18 | Yes | RANGE_ITEM_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| VALUE_DEFN_ID | NUMBER |  | 18 |  | VALUE_DEFN_ID |
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
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PAY_OLD_RANGE_ITEMS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, RANGE_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| PAY_RANGE_ITEMS_FN1_ | Non Unique | Default | RANGE_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE | Obsolete |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
