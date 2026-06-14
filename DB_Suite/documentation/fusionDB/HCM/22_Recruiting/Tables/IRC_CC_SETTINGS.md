# IRC_CC_SETTINGS

Table in which Site template settings are storred. Each setting is unique per template.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircccsettings-16918.html#ircccsettings-16918](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircccsettings-16918.html#ircccsettings-16918)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CC_SETTINGS_PK | SETTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SETTING_ID | NUMBER |  | 18 | Yes | Primary key of the template setting. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ELEMENT_ID | NUMBER |  | 18 | Yes | Foreign key to the elements table, used for joins. |  |
| SETTING_KEY | VARCHAR2 | 4000 |  | Yes | Stores the key of the template setting. |  |
| SETTING_VALUE | VARCHAR2 | 4000 |  |  | Stores the value of the template setting |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CC_SETTINGS_U1 | Unique | Default | ELEMENT_ID, SETTING_KEY |
| IRC_CC_SETTINGS_U2 | Unique | Default | SETTING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
