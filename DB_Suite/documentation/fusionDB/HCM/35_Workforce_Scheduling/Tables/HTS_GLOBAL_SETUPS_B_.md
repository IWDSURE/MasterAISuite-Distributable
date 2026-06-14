# HTS_GLOBAL_SETUPS_B_

Base table containing Schedule Global Setup Options used by diffrent schedule apllications.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupsb-29455.html#htsglobalsetupsb-29455](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupsb-29455.html#htsglobalsetupsb-29455)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_GLOBAL_SETUPS_B_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, SETUP_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PARAM_ID | NUMBER |  | 18 | Yes | Primary key. Unique system generated identifier for a Global Setup Options |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Standard Enterprise Identifier column for multi tenancy support |
| PARAMETER_CODE | VARCHAR2 | 80 |  |  | The parameter unique code. Used as Alternate Key |
| VALUE_TYPE | VARCHAR2 | 30 |  |  | The value type indicates whether the value is in number, text, or date format. |
| VALUE_NUMBER | NUMBER |  |  |  | stores the parameter numerical value |
| VALUE_TEXT | VARCHAR2 | 500 |  |  | stores the parameter text value |
| VALUE_DATE | DATE |  |  |  | stores the parameter date value |
| LIST_OF_VALUES_SRC | VARCHAR2 | 30 |  |  | Source of Value List |
| LIST_OF_VALUES_NAME | VARCHAR2 | 250 |  |  | Lookup type or View name |
| PARAMETER_CATEGORY | VARCHAR2 | 30 |  |  | Parameter category |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_GLOBAL_SETUPS_B_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, SETUP_PARAM_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
