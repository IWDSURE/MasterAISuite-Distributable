# WLF_LI_TYPE_PROVIDERS

Table to store learning item types for various providers

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflitypeproviders-20372.html#wlflitypeproviders-20372](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflitypeproviders-20372.html#wlflitypeproviders-20372)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_TYPE_PROVIDERS_PK | LI_TYPE_PROVIDER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LI_TYPE_PROVIDER_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_TYPE | VARCHAR2 | 30 |  | Yes | Provider Type |
| LEARNING_ITEM_TYPE | VARCHAR2 | 30 |  | Yes | OLC learning item type |
| PROVIDER_LI_TYPE | VARCHAR2 | 100 |  | Yes | Provider owned learning item type |
| LEARNING_ITEM_TYPE_MUTABLE | VARCHAR2 | 1 |  |  | Learning Item Type mutable flag |
| LEARNING_ITEM_TYPE_RULE | VARCHAR2 | 4000 |  |  | Learning Item Type Rule for provider and olc learning item type |
| APPLY_RULE_EXTENSIBLE_FLAG | VARCHAR2 | 1 |  |  | Apply rule extensible type flag |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_TYPE_PROVIDERS_N1 | Non Unique | WLF_LI_TYPE_PROVIDERS_N1 | PROVIDER_TYPE |
| WLF_LI_TYPE_PROVIDERS_PK | Unique | Default | LI_TYPE_PROVIDER_ID, ORA_SEED_SET1 |
| WLF_LI_TYPE_PROVIDERS_PK2 | Unique | Default | LI_TYPE_PROVIDER_ID, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
