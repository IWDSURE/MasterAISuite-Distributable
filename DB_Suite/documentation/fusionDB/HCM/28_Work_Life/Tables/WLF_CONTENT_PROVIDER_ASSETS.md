# WLF_CONTENT_PROVIDER_ASSETS

Table to maintain imported Learning Content by specific vendor to enable quick lookup in Learn

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcontentproviderassets-18370.html#wlfcontentproviderassets-18370](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcontentproviderassets-18370.html#wlfcontentproviderassets-18370)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SKILLSOFT_ASSETS_PK | ASSET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_ID | NUMBER |  | 18 | Yes | ASSET_ID - the database id |
| ADDITIONAL_INFO | VARCHAR2 | 4000 |  |  | This column is used to store the additional info like launch_url of the content provider asset. |
| PROVIDER_CODE | VARCHAR2 | 30 |  | Yes | PROVIDER_CODE - the content provider code value |
| UPDATE_TYPE | VARCHAR2 | 30 |  | Yes | UPDATE_TYPE |
| INGESTION_DATE | DATE |  |  |  | INGESTION_DATE |
| INGESTION_STATUS | VARCHAR2 | 30 |  | Yes | INGESTION_STATUS |
| ASSET_IDENTIFIER | VARCHAR2 | 2000 |  | Yes | ASSET_IDENTIFIER |
| NORMALIZED_IDENTIFIER | VARCHAR2 | 2000 |  |  | NORMALIZED_IDENTIFIER |
| ASSET_LANGUAGE | VARCHAR2 | 30 |  |  | ASSET_LANGUAGE |
| ISO_LANGUAGE_CODE | VARCHAR2 | 30 |  |  | ISO_LANGUAGE_CODE |
| ASSET_TYPE | VARCHAR2 | 30 |  | Yes | ASSET_TYPE |
| ASSET_TITLE | VARCHAR2 | 250 |  | Yes | ASSET_TITLE |
| ASSET_DESCRIPTION_SHORT | VARCHAR2 | 4000 |  |  | The Asset Description truncated to 4000 characters with HTML encoding removed |
| ASSET_DESCRIPTION_LONG | CLOB |  |  |  | The Asset Description unchanged |
| ASSET_CONTENT | CLOB |  |  | Yes | ASSET_CONTENT - opaque data as defined by Provider and Type values |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| CATALOG_INGEST_MODE | VARCHAR2 | 30 |  |  | The mode in which to ingest this Asset |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CONTENT_PROVIDER_ASSETS_N1 | Non Unique | Default | PROVIDER_CODE, NORMALIZED_IDENTIFIER |
| WLF_CONTENT_PROVIDER_ASSETS_N2 | Non Unique | Default | ISO_LANGUAGE_CODE |
| WLF_CONTENT_VENDOR_ASSETS_PK | Unique | Default | ASSET_ID |
| WLF_CONTENT_VENDOR_ASSETS_U1 | Unique | Default | PROVIDER_CODE, ASSET_IDENTIFIER |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
