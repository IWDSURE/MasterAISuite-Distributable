# IRC_LC_REASON_GROUPS_TL

IRC_LC_REASON_GROUPS_TL: multilingual table for the groups, it holds group name an group description.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcreasongroupstl-27328.html#irclcreasongroupstl-27328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcreasongroupstl-27328.html#irclcreasongroupstl-27328)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_REASON_GROUPS_TL_PK | REASON_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REASON_GROUP_ID | NUMBER |  | 18 | Yes | REASON GROUP ID : Part of primary key. Defines a unique reason group in corresponding B table. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| REASON_GROUP_NAME | VARCHAR2 | 512 |  | Yes | ACTION NAME To BE DISPLAYED for the given action ID. Needs to be transalated |  |
| REASON_GROUP_COMMENTS | VARCHAR2 | 1000 |  |  | REASON GROUP COMMENTS: commetns explaining the group purpose,  needs to be translated |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_REASON_GROUPS_TL_U1 | Unique | Default | REASON_GROUP_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
