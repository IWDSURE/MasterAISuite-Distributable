# IRC_CX_COOKIES_TL

Site cookie messages translated settings. Cookie message can by only one per site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxcookiestl-28671.html#irccxcookiestl-28671](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxcookiestl-28671.html#irccxcookiestl-28671)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_COOKIES_TL_PK | COOKIE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| COOKIE_ID | NUMBER |  | 18 | Yes | Identifier of the cookie. System generated value. |  |
| COOKIE_LINK_LABEL | VARCHAR2 | 4000 |  |  | Cookie Link Label |  |
| PREFERENCES_BUTTON_LABEL | VARCHAR2 | 4000 |  |  | Cookie Preferences Button Label |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| PREFERENCES_SAVE_BUTTON_LABEL | VARCHAR2 | 4000 |  |  | Cookie Preferences Save Button Label |  |
| STRICT_CATEGORY_MESSAGE | CLOB |  |  |  | Description for Strictly Necessary Cookie Category |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ANALYTICAL_CATEGORY_MESSAGE | CLOB |  |  |  | Description for Analytical Cookie Category |  |
| FUNCTIONAL_CATEGORY_MESSAGE | CLOB |  |  |  | Description for Functional Cookie Category |  |
| CUSTOM_CATEGORY_BUTTON_LABEL | VARCHAR2 | 4000 |  |  | Custom Category Button Label |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| CUSTOM_CATEGORY_DESCRIPTION | CLOB |  |  |  | Description for Custom Cookie Category |  |
| POP_UP_MESSAGE | VARCHAR2 | 4000 |  |  | Column containing translatable cookie popup message. |  |
| POLICY_MESSAGE | CLOB |  |  |  | Column containing translatable cookie policy message site. |  |
| ACCEPT_BUTTON_LABEL | VARCHAR2 | 4000 |  |  | Column containing translatable label of accept button. |  |
| DECLINE_BUTTON_LABEL | VARCHAR2 | 4000 |  |  | Column containing translatable label of decline button |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_COOKIES_TL_PK | Unique | FUSION_TS_SEED | COOKIE_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
