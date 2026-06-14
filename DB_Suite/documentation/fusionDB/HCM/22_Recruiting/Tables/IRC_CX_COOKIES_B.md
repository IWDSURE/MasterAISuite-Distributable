# IRC_CX_COOKIES_B

Site cookie messages settings. Cookie message can by only one per site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxcookiesb-31605.html#irccxcookiesb-31605](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxcookiesb-31605.html#irccxcookiesb-31605)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_COOKIES_B_PK | COOKIE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| COOKIE_ID | NUMBER |  | 18 | Yes | Primary a key. Identifier of the site cookie. System generated value. |  |
| IS_ENABLED_CUSTOM_COOKIE | NUMBER |  | 1 | Yes | Flag to show custom cookie section |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object |  |
| IS_ENABLED_COOKIE_PREFERENCES | NUMBER |  | 1 | Yes | Flag to show cookie preferences |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| IS_ENABLED_COOKIE_MESSAGES | NUMBER |  | 1 | Yes | Indicates if cookie message should be enabled of not. 1 true 0 false |  |
| IS_ENABLED_DECLINE_BUTTON | NUMBER |  | 1 | Yes | Indicates if decline button should be enabled of not. 1 true 0 false |  |
| SITE_ID | NUMBER |  | 18 | Yes | Foreign key to the IRC_CX_SITES_B as cookie message can by only one per site |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_CX_COOKIES_B_PK | Unique | FUSION_TS_SEED | COOKIE_ID |  |
| IRC_CX_COOKIES_B_U1 | Unique | FUSION_TS_SEED | COOKIE_ID, MODULE_ID | Obsolete |
| IRC_CX_COOKIES_B_U2 | Unique | FUSION_TS_SEED | SITE_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
