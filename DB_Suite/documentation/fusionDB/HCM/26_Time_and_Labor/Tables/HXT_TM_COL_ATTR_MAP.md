# HXT_TM_COL_ATTR_MAP

The table contains the mapping between the data dictionary attribute to the columns of the timecard UI tables.  The consistent mapping across timecards ensure timekeeper can pull up multiple timecards in the same table.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmcolattrmap-19508.html#hxttmcolattrmap-19508](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttmcolattrmap-19508.html#hxttmcolattrmap-19508)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TM_COL_ATTR_MAP_PK | TM_COL_ATTR_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_COL_ATTR_MAP_ID | NUMBER |  | 18 | Yes | TM_COL_ATTR_MAP_ID |
| TCLAYST_ID | NUMBER |  | 18 |  | TCLAYST_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LOCATION | VARCHAR2 | 32 |  |  | LOCATION |
| COLUMN_INDEX | NUMBER |  |  |  | COLUMN_INDEX |
| DATA_TYPE | VARCHAR2 | 20 |  |  | DATA_TYPE |
| ATTRIBUTE_ID_STRING | VARCHAR2 | 64 |  |  | ATTRIBUTE_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 150 |  |  | ATTRIBUTE_NAME |
| ALLOCATED_COLUMN_NAME | VARCHAR2 | 64 |  |  | ALLOCATED_COLUMN_NAME |
| TM_COL_ATTR_MAP_CD | VARCHAR2 | 100 |  |  | Alternate key |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TM_COL_ATTR_MAP_N20 | Non Unique | Default | SGUID |
| HXT_TM_COL_ATTR_MAP_U1 | Unique | Default | TM_COL_ATTR_MAP_ID, ORA_SEED_SET1 |
| HXT_TM_COL_ATTR_MAP_U11 | Unique | Default | TM_COL_ATTR_MAP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
