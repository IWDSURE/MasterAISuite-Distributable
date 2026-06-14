# FF_USER_TABLES

FF_USER_TABLES holds the table definitions for user defined tables. These tables are matrix structures of rows and columns that maintain date-tracked lists of values stored as cells for specific row/column combinations. Rows are defined in FF_USER_ROWS_F, columns are defined in FF_USER_COLUMNS and the actual cell values, which change over time, are held in FF_USER_COLUMN_INSTANCES_F. For example, you could define a table of union-negotiated rates for overtime and standard time that are dependent on grade level. The user table, UNION RATES, would have a row for each GRADE, and each row would be identified by an exact match with a specific grade. The table would have two columns, STANDARD RATE and OVERTIME RATE.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffusertables-31204.html#ffusertables-31204](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffusertables-31204.html#ffusertables-31204)

## Primary Key

| Name | Columns |
|------|----------|
| FF_USER_TABLES_PK | USER_TABLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_TABLE_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| BASE_USER_TABLE_NAME | VARCHAR2 | 80 |  | Yes | User name for the table. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| RANGE_OR_MATCH | VARCHAR2 | 30 |  | Yes | Indicates whether the user key is exact match or within range. |
| USER_KEY_UNITS | VARCHAR2 | 30 |  | Yes | Indicates the data type of the user key (number, date or character). The unit is number for range matching. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_USER_TABLES_N1 | Non Unique | Default | UPPER("BASE_USER_TABLE_NAME") |
| FF_USER_TABLES_PK | Unique | Default | USER_TABLE_ID, ORA_SEED_SET1 |
| FF_USER_TABLES_PK1 | Unique | Default | USER_TABLE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
