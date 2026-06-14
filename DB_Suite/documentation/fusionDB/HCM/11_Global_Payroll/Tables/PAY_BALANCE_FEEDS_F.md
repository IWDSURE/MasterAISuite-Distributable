# PAY_BALANCE_FEEDS_F

This table contains the details of how a given element input value contributes to a specific balance. The existence of a balance feed does not by itself guarantee that an input value will feed a balance, as there may be other restrictions. It is the intersection between PAY_BALANCE_TYPE and PAY_INPUT_VALUES_F.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancefeedsf-30649.html#paybalancefeedsf-30649](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancefeedsf-30649.html#paybalancefeedsf-30649)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BALANCE_FEEDS_F_PK | BALANCE_FEED_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BALANCE_FEED_ID | NUMBER |  | 18 | Yes | BALANCE_FEED_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BALANCE_TYPE_ID | NUMBER |  | 18 | Yes | BALANCE_TYPE_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| SCALE | NUMBER |  | 5 | Yes | SCALE |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| SOURCE_ID | NUMBER |  | 18 |  | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | The Entity of the Source ID denoting the table that the Id comes from. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BALANCE_FEEDS_F_N2 | Non Unique | Default | INPUT_VALUE_ID |
| PAY_BALANCE_FEEDS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_BALANCE_FEEDS_F_N3 | Non Unique | Default | ELEMENT_TYPE_ID, BALANCE_TYPE_ID |
| PAY_BALANCE_FEEDS_F_N4 | Non Unique | Default | BALANCE_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, SOURCE_ID |
| PAY_BALANCE_FEEDS_F_PK | Unique | Default | BALANCE_FEED_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_BALANCE_FEEDS_F_PK1 | Unique | Default | BALANCE_FEED_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_BALANCE_FEEDS_F_U1 | Unique | Default | BALANCE_TYPE_ID, INPUT_VALUE_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, SOURCE_ID, SOURCE_TYPE, ORA_SEED_SET1 |
| PAY_BALANCE_FEEDS_F_U11 | Unique | Default | BALANCE_TYPE_ID, INPUT_VALUE_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, SOURCE_ID, SOURCE_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
