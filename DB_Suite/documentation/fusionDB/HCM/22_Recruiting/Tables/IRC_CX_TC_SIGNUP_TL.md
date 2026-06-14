# IRC_CX_TC_SIGNUP_TL

Site cookie messages translated settings. Cookie message can by only one per site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxtcsignuptl-20353.html#irccxtcsignuptl-20353](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxtcsignuptl-20353.html#irccxtcsignuptl-20353)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_TC_SIGNUP_TL_PK | SITE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SITE_ID | NUMBER |  | 18 | Yes | Primary a key. Identifier of the talent community setting. System generated value. |  |
| TITLE | VARCHAR2 | 1000 |  |  | Title of the Talent Community Signup popup. |  |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | Text inside Talent Community Signup popup. |  |
| BUTTON_LABEL | VARCHAR2 | 1000 |  |  | Label of the button on Talent Community Signup popup. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_TC_SIGNUP_TL_U1 | Unique | FUSION_TS_SEED | SITE_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
