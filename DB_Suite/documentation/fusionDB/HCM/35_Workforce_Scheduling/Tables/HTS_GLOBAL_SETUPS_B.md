# HTS_GLOBAL_SETUPS_B

Base table containing Schedule Global Setup Options used by diffrent schedule apllications.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupsb-5875.html#htsglobalsetupsb-5875](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupsb-5875.html#htsglobalsetupsb-5875)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_GLOBAL_SETUPS_B_PK | SETUP_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PARAM_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Global Setup Options |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| PARAMETER_CODE | VARCHAR2 | 80 |  | Yes | The parameter unique code. Used as Alternate Key |
| VALUE_TYPE | VARCHAR2 | 30 |  | Yes | The value type indicates whether the value is in number, text, or date format. |
| VALUE_NUMBER | NUMBER |  |  |  | stores the parameter numerical value |
| VALUE_TEXT | VARCHAR2 | 500 |  |  | stores the parameter text value |
| VALUE_DATE | DATE |  |  |  | stores the parameter date value |
| LIST_OF_VALUES_SRC | VARCHAR2 | 30 |  |  | Source of Value List |
| LIST_OF_VALUES_NAME | VARCHAR2 | 250 |  |  | Lookup type or View name |
| PARAMETER_CATEGORY | VARCHAR2 | 30 |  |  | Parameter category |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_GLOBAL_SETUPS_B_N40 | Non Unique | Default | SGUID |
| HTS_GLOBAL_SETUPS_B_U10 | Unique | Default | SETUP_PARAM_ID, ORA_SEED_SET1 |
| HTS_GLOBAL_SETUPS_B_U101 | Unique | Default | SETUP_PARAM_ID, ORA_SEED_SET2 |
| HTS_GLOBAL_SETUPS_B_U20 | Unique | Default | PARAMETER_CODE, ORA_SEED_SET1 |
| HTS_GLOBAL_SETUPS_B_U201 | Unique | Default | PARAMETER_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
