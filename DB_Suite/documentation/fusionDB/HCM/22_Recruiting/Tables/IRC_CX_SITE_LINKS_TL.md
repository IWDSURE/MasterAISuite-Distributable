# IRC_CX_SITE_LINKS_TL

Details of language specific links properties.  Theme links Table. MLS table with theme  links specific properties.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitelinkstl-13870.html#irccxsitelinkstl-13870](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxsitelinkstl-13870.html#irccxsitelinkstl-13870)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_SITE_LINKS_TL_PK | LINK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LINK_ID | NUMBER |  | 18 | Yes | Identifier of the site link. System generated value. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LINK_NAME | VARCHAR2 | 1000 |  |  | Link name displayed on FSM administration page. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| LINK_URL | VARCHAR2 | 2048 |  |  | LINK URL. LINK URL for specific language |  |
| LINK_TEXT | VARCHAR2 | 240 |  |  | LINK_TEXT Short link text for specific language |  |
| LINK_ATTRIBUTE1 | VARCHAR2 | 2048 |  |  | Attribute to store additional information |  |
| LINK_ATTRIBUTE2 | VARCHAR2 | 2048 |  |  | Attribute to store additional information |  |
| LINK_ATTRIBUTE3 | VARCHAR2 | 2048 |  |  | Attribute to store additional information |  |
| LINK_DESC | VARCHAR2 | 4000 |  |  | Attribute to store description of the link |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LINK_CLOB_ATTRIBUTE1 | CLOB |  |  |  | Attribute to store additional information |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_SITE_LINKS_TL_PK | Unique | FUSION_TS_SEED | LINK_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
