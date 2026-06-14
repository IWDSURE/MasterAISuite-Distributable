# PAY_OLD_VALUE_DEFNS_F_

This table contains details of how a value is calculated in payroll processing using range items, calculation types, and allowed overrides.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payoldvaluedefnsf-27706.html#payoldvaluedefnsf-27706](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payoldvaluedefnsf-27706.html#payoldvaluedefnsf-27706)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_VALUE_DEFINITIONS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, VALUE_DEFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VALUE_DEFN_ID | NUMBER |  | 18 | Yes | VALUE_DEFN_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BASE_NAME | VARCHAR2 | 120 |  |  | BASE_NAME |
| VALUE_GROUP_ID | NUMBER |  | 18 |  | VALUE_GROUP_ID |
| CALC_TYPE_ID | NUMBER |  | 18 |  | CALC_TYPE_ID |
| DATABASE_ITEM_ID | NUMBER |  | 18 |  | DATABASE_ITEM_ID |
| RANGE_DATABASE_ITEM_ID | NUMBER |  | 18 |  | RANGE_DATABASE_ITEM_ID |
| OVERRIDDEN_DB_ITEM_ID | NUMBER |  | 18 |  | Denotes the DB Item whose value is overridden by an entry for this Value Definition. |
| BASE_VALUE_DEFN_ID | NUMBER |  | 18 |  | BASE_VALUE_DEFN_ID |
| PARENT_VALUE_DEFN_ID | NUMBER |  | 18 |  | PARENT_VALUE_DEFN_ID |
| DATE_MODE | VARCHAR2 | 5 |  |  | DATE_MODE |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | SOURCE_TYPE |
| DIR_OVERRIDE_USAGE_ID | NUMBER |  | 18 |  | DIR_OVERRIDE_USAGE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CURRENCY_CODE | VARCHAR2 | 15 |  |  | CURRENCY_CODE |
| UOM | VARCHAR2 | 30 |  |  | Unit of Measure |
| PERIODICITY | VARCHAR2 | 30 |  |  | PERIODICITY |
| PERIODICITY_TYPE | VARCHAR2 | 5 |  |  | This denotes the type of the periodicity. For example is it time based, Annually, Monthly, etc or unit based, widgets, meals, etc. |
| DEFAULT_CALC_TYPE_ID | NUMBER |  | 18 |  | DEFAULT_CALC_TYPE_ID |
| EXPRESSION | VARCHAR2 | 30 |  |  | EXPRESSION |
| SEQUENCE | NUMBER |  | 18 |  | SEQUENCE |
| DEFAULT_FLAG | VARCHAR2 | 30 |  |  | DEFAULT_FLAG |
| VALUE_IDENTIFIER | VARCHAR2 | 30 |  |  | Identifies the Value in a multi leaf Value by Criteria. |
| GEOGRAPHY_TYPE_ID | NUMBER |  | 18 |  | Foreign key to HZ_GEOGRAPHIES. |
| VALUE_SET_CODE1 | VARCHAR2 | 200 |  |  | Value Set lookup code 1 |
| VALUE_SET_CODE2 | VARCHAR2 | 200 |  |  | Value Set lookup code 2 |
| VALUE_SET_CODE3 | VARCHAR2 | 200 |  |  | Value Set Lookup Code 3 |
| VO_NAME1 | VARCHAR2 | 100 |  |  | VALUE_SET1_ID |
| VO_NAME2 | VARCHAR2 | 100 |  |  | VALUE_SET2_ID |
| VO_NAME3 | VARCHAR2 | 100 |  |  | VALUE_SET3_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SEED_STATUS | VARCHAR2 | 1 |  |  | SEED_STATUS |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PAY_OLD_VALUE_DEFNS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, VALUE_DEFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |
| PAY_VALUE_DEFINITIONS_FN1_ | Non Unique | Default | VALUE_DEFN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE | Obsolete |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
