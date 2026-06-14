# IRC_TP_CATEGORIES_TL

Stores translation data for third party integration categories.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctpcategoriestl-26442.html#irctpcategoriestl-26442](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctpcategoriestl-26442.html#irctpcategoriestl-26442)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TP_CATEGORIES_TL_PK | CATEGORY_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_ID | NUMBER |  | 18 | Yes | Part of the primary key and also foreign key to IRC_TP_CATEGORIES_B table |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CATEGORY_NAME | VARCHAR2 | 300 |  | Yes | Stores the translatable name of this category. |
| SUB_CATEGORY_NAME | VARCHAR2 | 300 |  |  | Stores the translatable name of this sub-category. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | Stores the translatable description of this category. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TP_CATEGORIES_TL_PK | Unique | FUSION_TS_SEED | CATEGORY_ID, LANGUAGE, ORA_SEED_SET1 |
| IRC_TP_CATEGORIES_TL_PK1 | Unique | FUSION_TS_SEED | CATEGORY_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
