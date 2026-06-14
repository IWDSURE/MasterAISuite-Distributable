# IRC_GV_DEFAULT_VIEWS

This table stores the views which are marked as Default by the respective users.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvdefaultviews-27513.html#ircgvdefaultviews-27513](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvdefaultviews-27513.html#ircgvdefaultviews-27513)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GV_DEFAULT_VIEWS_PK | DEFAULT_VIEW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEFAULT_VIEW_ID | NUMBER |  | 18 | Yes | Primary Key for the table. System Generated. |
| VIEW_ID | NUMBER |  | 18 | Yes | Foreign key IRC_GV_VIEWS_B table. |
| GV_CONTEXT_CODE | VARCHAR2 | 100 |  | Yes | Stores the context code for which all the views will be stored. For example : Context can be ORA_SUBMISSION and all the views related to Job Application would be specified with this context code. |
| VIEW_OWNER | VARCHAR2 | 100 |  | Yes | Stores the user name who has marked this view as default view. This will also store value as 'SITE' if the defined view is being published for the site level by the administrator. The Seeded Views will be having default view owner as 'SITE'. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| IRC_GV_DEFAULT_VIEWS_PK | Unique | Default | DEFAULT_VIEW_ID, ORA_SEED_SET1 |
| IRC_GV_DEFAULT_VIEWS_PK1 | Unique | Default | DEFAULT_VIEW_ID, ORA_SEED_SET2 |
| IRC_GV_DEFAULT_VIEWS_U1 | Unique | Default | VIEW_ID, VIEW_OWNER, GV_CONTEXT_CODE, ORA_SEED_SET1 |
| IRC_GV_DEFAULT_VIEWS_U11 | Unique | Default | VIEW_ID, VIEW_OWNER, GV_CONTEXT_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
