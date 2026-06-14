# IRC_GV_VIEW_OWNERS

This table is used to store the view owners details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvviewowners-19759.html#ircgvviewowners-19759](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvviewowners-19759.html#ircgvviewowners-19759)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GV_VIEW_OWNERS_PK | VIEW_OWNER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VIEW_OWNER_ID | NUMBER |  | 20 | Yes | Primary Key for this table. Auto Generated Key. |
| VIEW_ID | NUMBER |  | 20 | Yes | Foreign key IRC_GV_VIEWS_B table. |
| OWNER_CODE | VARCHAR2 | 512 |  |  | This column stores the user name or role code or site as the owner code who owns the view. |
| OWNER_TYPE | VARCHAR2 | 100 |  |  | This column stores the owner type as ORA_GV_ROLE if the view  type was "ROLE" , ORA_GV_SITE if the view  type was "SITE" and ORA_GV_USER if the view  type was "Personal" |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GV_VIEW_OWNERS_FK1 | Non Unique | Default | VIEW_ID |
| IRC_GV_VIEW_OWNERS_PK | Unique | Default | VIEW_OWNER_ID, ORA_SEED_SET1 |
| IRC_GV_VIEW_OWNERS_PK1 | Unique | Default | VIEW_OWNER_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
