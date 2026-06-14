# IRC_CX_CTM_FONTS_TL

Details of the sites for candidate experience

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxctmfontstl-28932.html#irccxctmfontstl-28932](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxctmfontstl-28932.html#irccxctmfontstl-28932)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_CTM_FONTS_TL_PK | CUSTOM_FONT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CUSTOM_FONT_ID | NUMBER |  | 18 | Yes | PRIMARY KEY. Custom fonts are fonts added by the clientustom fonts are fonts added by the client |  |
| FONT_NAME | VARCHAR2 | 4000 |  | Yes | USER DEFINED CUSTOM FONT NAME.Custom fonts are fonts added by the clientustom fonts are fonts added by the client |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
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
| IRC_CX_CTM_FONTS_TL_U1 | Unique | Default | CUSTOM_FONT_ID, FONT_NAME, LANGUAGE |
| IRC_CX_CTM_FONTS_TL_U2 | Unique | Default | CUSTOM_FONT_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
