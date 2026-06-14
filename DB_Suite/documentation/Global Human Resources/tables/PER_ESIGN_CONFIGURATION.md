# PER_ESIGN_CONFIGURATION

This table is used for storing docusign details

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peresignconfiguration-23680.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peresignconfiguration-23680.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ESIGN_CONFIGURATION_PK | ESIGN_CONFIGURATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ESIGN_CONFIGURATION_ID | NUMBER |  | 18 | Yes | ESIGN_CONFIGURATION_ID |
| INTEGRATION_CODE | VARCHAR2 | 80 |  | Yes | INTEGRATION_CODE |
| KEYS_CONFIGURED | VARCHAR2 | 4 |  | Yes | KEYS_CONFIGURED |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ESIGN_TYPE | VARCHAR2 | 30 |  | Yes | Specifies Esignature Type |
| PROVIDER_URL | VARCHAR2 | 500 |  |  | The URL of the degital signature provider |
| USER_DETAILS | VARCHAR2 | 240 |  |  | USER_DETAILS |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ESIGN_CONFIGURATION_U1 | Unique | Default | ESIGN_CONFIGURATION_ID, ORA_SEED_SET1 |
| PER_ESIGN_CONFIGURATION_U11 | Unique | Default | ESIGN_CONFIGURATION_ID, ORA_SEED_SET2 |
| PER_ESIGN_CONFIGURATION_U2 | Unique | Default | INTEGRATION_CODE, ORA_SEED_SET1 |
| PER_ESIGN_CONFIGURATION_U21 | Unique | Default | INTEGRATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
