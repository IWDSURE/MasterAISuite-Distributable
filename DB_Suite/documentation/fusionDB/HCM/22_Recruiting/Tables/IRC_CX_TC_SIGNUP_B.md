# IRC_CX_TC_SIGNUP_B

Talent community configuration. Tallent community configuration can by only one per site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxtcsignupb-10090.html#irccxtcsignupb-10090](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxtcsignupb-10090.html#irccxtcsignupb-10090)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_TC_SIGNUP_B_PK | SITE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SITE_ID | NUMBER |  | 18 | Yes | Primary a key and foreign key to IRC_CX_SITES_B. Identifier of the talent community setting. System generated value. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| SHOW_AT_SEARCH_FLAG | NUMBER |  | 1 | Yes | Indicates if tc pop up should be visible on  search results. 1 true 0 false |  |
| SHOW_WHEN_NO_RESULTS_FLAG | NUMBER |  | 1 | Yes | Indicates if tc pop up should be shown when no search results found. 1 true 0 false |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Stores the status of the Object as a lookup code. The corresponding lookup type is ORA_IRC_OBJECT_STATUS. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_TC_SIGNUP_B_U1 | Unique | FUSION_TS_SEED | SITE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
