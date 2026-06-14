# IRC_CX_SITES_TL

Translated details of the sites

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitestl-18157.html#irccxsitestl-18157](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitestl-18157.html#irccxsitestl-18157)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITES_TL_PK | SITE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SITE_ID | NUMBER |  | 18 | Yes | Identifier of the site. System generated value. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| SITE_NAME | VARCHAR2 | 240 |  | Yes | Name of the site which is used to publish the jobs. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| SMART_SEARCH_SUGGESTION | VARCHAR2 | 1000 |  |  | Suggested message to display in the smart search panel |  |
| OG_IMAGE_SRC | VARCHAR2 | 1000 |  |  | The image src of the client logo will be displayed when sharing the page on social platforms. |  |
| SEO_ORGANIZATION_NAME | VARCHAR2 | 300 |  |  | The name of the organization defined for SEO. |  |
| SEO_ORGANIZATION_SAME_AS | VARCHAR2 | 4000 |  |  | The organization URLs defined for SEO. |  |
| SEO_ORGANIZATION_LOGO | VARCHAR2 | 1000 |  |  | The organization logo defined for SEO. |  |
| SEO_DESCRIPTION | VARCHAR2 | 1000 |  |  | The description for SEO. |  |
| SEO_KEYWORDS | VARCHAR2 | 4000 |  |  | Set of comma separated SEO keywords. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITES_TL_PK | Unique | FUSION_TS_SEED | SITE_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
