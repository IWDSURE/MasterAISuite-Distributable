# IRC_LC_SETTING_ITEMS

IRC_LC_SETTING_ITEMS: the setting items are elements of the settings table, they will link to the various configurations, setting items will use the object type object code to for the linkage.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcsettingitems-20363.html#irclcsettingitems-20363](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcsettingitems-20363.html#irclcsettingitems-20363)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_SETTING_ITEMS_PK | SETTING_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SETTING_ITEM_ID | NUMBER |  | 18 | Yes | SETTING ITEM ID : Primary Key of the table. System generated. |  |
| ITEM_KEY_NAME | VARCHAR2 | 50 |  |  | Name API consumer has given to his setting item. Must be unique among all other setting items sharing a same SettingId. |  |
| SETTING_ITEM_CODE | VARCHAR2 | 256 |  | Yes | Stores the code for the code of the item, used to import/export. |  |
| SETTING_ID | NUMBER |  | 18 | Yes | Identifies the setting to which this item belongs to |  |
| OBJECT_TYPE | VARCHAR2 | 256 |  | Yes | Type of the object to which the setting item refers to |  |
| OBJECT_ID | NUMBER |  | 18 |  | Id of the object to which the setting item refers to |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| STRING_VALUE | VARCHAR2 | 124 |  |  | Stores the String value for a Setting Item |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_SETTING_ITEMS_FK1 | Non Unique | Default | SETTING_ID |
| IRC_LC_SETTING_ITEMS_U1 | Unique | Default | SETTING_ITEM_ID |
| IRC_LC_SETTING_ITEMS_U2 | Unique | Default | SETTING_ITEM_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
