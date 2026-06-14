# FF_DATABASE_ITEMS_B

This table contains read-only formula variables whose values are database query results.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffdatabaseitemsb-27689.html#ffdatabaseitemsb-27689](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffdatabaseitemsb-27689.html#ffdatabaseitemsb-27689)

## Primary Key

| Name | Columns |
|------|----------|
| FF_DATABASE_ITEMS_PK | DATABASE_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATABASE_ITEM_ID | NUMBER |  | 18 | Yes | Unique identifier for the database item. |
| BASE_USER_NAME | VARCHAR2 | 255 |  | Yes | Unique name for the database item. |
| USER_ENTITY_ID | NUMBER |  | 18 | Yes | Identifier for the user entity. Foreign key to FF_USER_ENTITIES. |
| DATA_TYPE | VARCHAR2 | 2 |  | Yes | Data type of the database item. |
| NULL_ALLOWED_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether a NULL value will cause a formula error. |
| DEFINITION_TEXT | VARCHAR2 | 1000 |  | Yes | Select item text for use in the built-up SQL statement. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| FF_DATABASE_ITEMS_B_N1 | Non Unique | Default | MODULE_ID |  |
| FF_DATABASE_ITEMS_B_N2 | Non Unique | Default | UPPER("BASE_USER_NAME") |  |
| FF_DATABASE_ITEMS_B_N20 | Non Unique | Default | SGUID |  |
| FF_DATABASE_ITEMS_B_N3 | Non Unique | Default | BASE_USER_NAME |  |
| FF_DATABASE_ITEMS_B_PK | Unique | Default | DATABASE_ITEM_ID, ORA_SEED_SET1 |  |
| FF_DATABASE_ITEMS_B_PK1 | Unique | Default | DATABASE_ITEM_ID, ORA_SEED_SET2 |  |
| FF_DATABASE_ITEMS_B_U1 | Unique | Default | BASE_USER_NAME, USER_ENTITY_ID | Obsolete |
| FF_DATABASE_ITEMS_B_UK1 | Unique | Default | UPPER("BASE_USER_NAME"), USER_ENTITY_ID | Obsolete |
| FF_DATABASE_ITEMS_FK1 | Non Unique | Default | USER_ENTITY_ID |  |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
