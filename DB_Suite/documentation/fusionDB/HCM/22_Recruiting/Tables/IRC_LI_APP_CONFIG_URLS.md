# IRC_LI_APP_CONFIG_URLS

Stores the URLs used in LinkedIn customer application activation of LinkedIn integration in Recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircliappconfigurls-15537.html#ircliappconfigurls-15537](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircliappconfigurls-15537.html#ircliappconfigurls-15537)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_APP_CONFIG_URLS_PK | APP_URL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APP_URL_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| APP_URL | VARCHAR2 | 500 |  | Yes | Various URLs used for the provisioning application created for the integration |
| APP_URL_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the code identifying the URL type of the URL used in provisioning of application for  linkedin integration. The corresponding lookup type is ORA_IRC_LI_CONFIG_URL_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_APP_CONFIG_URLS_FK | Non Unique | FUSION_TS_SEED | PROVISIONING_ID |
| IRC_LI_APP_CONFIG_URLS_PK | Unique | FUSION_TS_SEED | APP_URL_ID, ORA_SEED_SET1 |
| IRC_LI_APP_CONFIG_URLS_PK1 | Unique | FUSION_TS_SEED | APP_URL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
