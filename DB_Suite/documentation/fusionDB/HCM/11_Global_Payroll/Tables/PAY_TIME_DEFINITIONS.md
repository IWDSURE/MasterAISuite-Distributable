# PAY_TIME_DEFINITIONS

This table contains details of period of time.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimedefinitions-30194.html#paytimedefinitions-30194](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimedefinitions-30194.html#paytimedefinitions-30194)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TIME_DEFINITIONS_PK | TIME_DEFINITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIME_DEFINITION_ID | NUMBER |  | 18 | Yes | TIME_DEFINITION_ID |
| SHORT_NAME | VARCHAR2 | 30 |  | Yes | SHORT_NAME |
| DEFINITION_NAME | VARCHAR2 | 80 |  | Yes | DEFINITION_NAME |
| DEFINITION_TYPE | VARCHAR2 | 30 |  |  | Indicates the Type of Time Definition. |
| PERIOD_TYPE | VARCHAR2 | 30 |  |  | PERIOD_TYPE |
| PERIOD_UNIT | VARCHAR2 | 30 |  |  | PERIOD_UNIT |
| DAY_ADJUSTMENT | VARCHAR2 | 30 |  |  | DAY_ADJUSTMENT |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| NUMBER_OF_YEARS | NUMBER |  | 18 |  | Number of Years a Static Period Time Definition has periods. |
| START_DATE | DATE |  |  |  | Date on which a Static Period Time Defintion Starts |
| BASE_TIME_DEFINITION_ID | NUMBER |  | 18 |  | BASE_TIME_DEFINITION_ID |
| PERIOD_TIME_DEFINITION_ID | NUMBER |  | 18 |  | Foreign Key to PAY_TIME_DEFINITIONS. |
| DATABASE_ITEM_ID | NUMBER |  | 18 |  | DATABASE_ITEM_ID |
| CREATOR_ID | NUMBER |  | 18 |  | Foreign Key to the source of the time definition. |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | Denotes the source of the time definition. |
| DYNAMIC_CODE | VARCHAR2 | 61 |  |  | DYNAMIC_CODE |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TIME_DEFINITIONS_PK | Unique | Default | TIME_DEFINITION_ID, ORA_SEED_SET1 |
| PAY_TIME_DEFINITIONS_PK1 | Unique | Default | TIME_DEFINITION_ID, ORA_SEED_SET2 |
| PAY_TIME_DEFINITIONS_U1 | Unique | Default | DEFINITION_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_TIME_DEFINITIONS_U11 | Unique | Default | DEFINITION_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
