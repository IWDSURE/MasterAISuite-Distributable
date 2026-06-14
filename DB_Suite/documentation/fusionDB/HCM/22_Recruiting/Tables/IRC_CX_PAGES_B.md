# IRC_CX_PAGES_B

Table in which Site template settings are storred. Each setting is unique per template.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxpagesb-17164.html#irccxpagesb-17164](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxpagesb-17164.html#irccxpagesb-17164)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_PAGES_B_PK | PAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PAGE_ID | NUMBER |  | 18 | Yes | Primary key, auto generated value. |  |
| TEMPLATE_ID | NUMBER |  | 18 |  | Template ID, refers to IRC_CX_SITE_TEMPLATES_B.TEMPLATE_ID |  |
| HEADER_ID | NUMBER |  | 18 |  | Foreign key to irc_cx_headers_b table. |  |
| TYPE | VARCHAR2 | 32 |  | Yes | Type of the Custom Page, will be used by UI in order to determine type of page. |  |
| VERSION | NUMBER |  | 18 | Yes | Version of the Custom Page, will be used by UI in order to determine in which release custom page was created. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ELEMENT_ID | NUMBER |  | 18 | Yes | Foreign key to the elements table, used for joins. |  |
| SITE_CODE | VARCHAR2 | 200 |  |  | Deprecated column, to be removed |  |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Foreign key to the SITES table. |  |
| PAGE_CODE | VARCHAR2 | 240 |  | Yes | Public unique code that identifies the page (calculated on back-end side upon insert). |  |
| STATUS_CODE | VARCHAR2 | 20 |  | Yes | Status of the page , if it is published or draft. |  |
| PUBLISHED_DATE | TIMESTAMP |  |  |  | The date when the page was published. |  |
| ELEMENT_TYPE | VARCHAR2 | 20 |  | Yes | Type of this element , the only possible value will be PAGE. |  |
| PAGE_URL_NAME | VARCHAR2 | 240 |  |  | Page Display Name for URL configured by the customer in the site editor visible in the URL |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_PAGES_B_N1 | Non Unique | Default | SITE_NUMBER |
| IRC_CX_PAGES_B_U1 | Unique | Default | PAGE_ID |
| IRC_CX_PAGES_B_U2 | Unique | Default | ELEMENT_ID |
| IRC_CX_PAGES_B_U3 | Unique | Default | PAGE_CODE, SITE_NUMBER, STATUS_CODE |
| IRC_CX_PAGES_B_FK2 | Non Unique | Default | TEMPLATE_ID |
| IRC_CX_PAGES_B_FK3 | Non Unique | Default | HEADER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
