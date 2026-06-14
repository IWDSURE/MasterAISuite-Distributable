# IRC_CX_PROVIDERS

List of the supported external providers. Seeded values.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxproviders-6690.html#irccxproviders-6690](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxproviders-6690.html#irccxproviders-6690)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_PROVIDERS_PK | PROVIDER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROVIDER_ID | NUMBER |  | 18 | Yes | Identifier of the external provider. System generated value. |
| PROVIDER_CODE | VARCHAR2 | 40 |  | Yes | Code of the external provider which will be used by UI to handle external provider properly. |
| PROVIDER_NAME | VARCHAR2 | 240 |  | Yes | Name of the given external provider. It will be displayed in Drop Down. |
| PROVIDER_TYPE | VARCHAR2 | 40 |  | Yes | Name of the setting needed to recognize external provider. |
| PROVIDER_DESCRIPTION | VARCHAR2 | 1000 |  |  | Description of this external provider. Optional value can be used for information purpose. |
| SUPPORTED_FLAG | VARCHAR2 | 1 |  | Yes | Flag that is saying if this external provider is supported by ORC. |
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
| IRC_CX_PROVIDERS_N1 | Non Unique | FUSION_TS_SEED | PROVIDER_TYPE |
| IRC_CX_PROVIDERS_PK | Unique | FUSION_TS_SEED | PROVIDER_ID, ORA_SEED_SET1 |
| IRC_CX_PROVIDERS_PK1 | Unique | FUSION_TS_SEED | PROVIDER_ID, ORA_SEED_SET2 |
| IRC_CX_PROVIDERS_U1 | Unique | FUSION_TS_SEED | PROVIDER_CODE, ORA_SEED_SET1 |
| IRC_CX_PROVIDERS_U11 | Unique | FUSION_TS_SEED | PROVIDER_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
