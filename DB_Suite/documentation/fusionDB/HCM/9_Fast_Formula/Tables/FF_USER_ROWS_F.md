# FF_USER_ROWS_F

FF_USER_ROWS_F is a date-tracked table that holds the definitions for rows in user defined tables. Rows can hold an exact value, or a low-high range of values to provide the match to a supplied user value. For example you may want to define one table with rows based on ranges of salary values, and another table based on exact grade values.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffuserrowsf-6155.html#ffuserrowsf-6155](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffuserrowsf-6155.html#ffuserrowsf-6155)

## Primary Key

| Name | Columns |
|------|----------|
| FF_USER_ROWS_F_PK | USER_ROW_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ROW_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ROW_LOW_RANGE_OR_NAME | VARCHAR2 | 80 |  | Yes | Lower value for range match of user key, or actual value for exact match. |
| USER_TABLE_ID | NUMBER |  | 18 | Yes | Foreign key to FF_USER_TABLES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ROW_HIGH_RANGE | VARCHAR2 | 80 |  |  | Upper value for range match of user key. |
| DISPLAY_SEQUENCE | NUMBER |  | 5 |  | Display sequence to use in preference to numeric/alpha order. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_USER_ROWS_F_FK1 | Non Unique | Default | USER_TABLE_ID |
| FF_USER_ROWS_F_N2 | Non Unique | Default | UPPER("ROW_LOW_RANGE_OR_NAME"), USER_TABLE_ID |
| FF_USER_ROWS_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| FF_USER_ROWS_F_PK | Unique | Default | USER_ROW_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| FF_USER_ROWS_F_PK1 | Unique | Default | USER_ROW_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
