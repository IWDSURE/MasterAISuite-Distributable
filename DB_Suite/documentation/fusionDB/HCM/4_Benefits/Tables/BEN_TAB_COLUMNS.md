# BEN_TAB_COLUMNS

This Table is used as the seeded data only. To get List of Values populated and validating while creation of Person Change and Related Person Change for the columns SOURCE_TABLE,SOURCE_COLUMN,OLD_VAL,NEW_VAL.
Person Change and Related Person Change is in Benefit Life Events.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bentabcolumns-8371.html#bentabcolumns-8371](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bentabcolumns-8371.html#bentabcolumns-8371)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_TAB_COLUMNS_PK | TABLE_NAME, COLUMN_NAME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TABLE_NAME | VARCHAR2 | 30 |  | Yes | TABLE_NAME |
| COLUMN_NAME | VARCHAR2 | 30 |  | Yes | COLUMN_NAME |
| LOOKUP_SOURCE | VARCHAR2 | 30 |  |  | LOOKUP_SOURCE |
| LOOKUP_SOURCE_COLUMN | VARCHAR2 | 30 |  |  | LOOKUP_SOURCE_COLUMN |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | ACTIVE_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_TAB_COLUMNS_PK | Unique | Default | TABLE_NAME, COLUMN_NAME, ORA_SEED_SET1 |
| BEN_TAB_COLUMNS_PK1 | Unique | Default | TABLE_NAME, COLUMN_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
