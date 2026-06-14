# IRC_CX_PAGES_TL

Table in which Site template settings are storred. Each setting is unique per template.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxpagestl-22641.html#irccxpagestl-22641](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxpagestl-22641.html#irccxpagestl-22641)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_PAGES_TL_PK | PAGE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PAGE_ID | NUMBER |  | 18 | Yes | Primary key, auto generated value. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| TITLE | VARCHAR2 | 200 |  | Yes | The title of the page, it will be displaed on browser window. |  |
| OG_IMAGE_SRC | VARCHAR2 | 1000 |  |  | The image src of the page, it will be displaed when sharing the page in social platforms. |  |
| OG_DESCRIPTION | VARCHAR2 | 1000 |  |  | Open Graph description of the page. |  |
| SEO_DESCRIPTION | VARCHAR2 | 4000 |  |  | Search Engine Optimization of the page. |  |
| SEO_KEYWORDS | VARCHAR2 | 4000 |  |  | Set of comma separated SEO keywords. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_PAGES_TL_U1 | Unique | Default | PAGE_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
