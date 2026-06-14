# WLF_RECOM_CONSUMER_CONFIG_B

This table stores consumer object details on which recommendations are created.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomconsumerconfigb-30744.html#wlfrecomconsumerconfigb-30744](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomconsumerconfigb-30744.html#wlfrecomconsumerconfigb-30744)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOM_CONSUMER_CONFIG_PK | RECOM_CONSUMER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOM_CONSUMER_CONFIG_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| OBJECT_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies the Object Category for which the configuration applies. |
| OBJECT_TYPE_LOOKUP | VARCHAR2 | 2000 |  |  | Represents lookup type of consumer object type. |
| OBJECT_SUB_TYPE_LOOKUP | VARCHAR2 | 2000 |  |  | Represents lookup type of consumer object type. |
| CONSUMER_IMPLEMENTATION_CLASS | VARCHAR2 | 4000 |  |  | Stores RecommendationConsumer Implementation class. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Specifies if the seed data row is enabled or not. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOM_CONSUMER_CONFIG_PK | Unique | Default | RECOM_CONSUMER_CONFIG_ID, ORA_SEED_SET1 |
| WLF_RECOM_CONSUMER_CONFIG_PK1 | Unique | Default | RECOM_CONSUMER_CONFIG_ID, ORA_SEED_SET2 |
| WLF_RECOM_CONSUMER_CONFIG_U1 | Unique | Default | OBJECT_CATEGORY, ORA_SEED_SET1 |
| WLF_RECOM_CONSUMER_CONFIG_U11 | Unique | Default | OBJECT_CATEGORY, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
