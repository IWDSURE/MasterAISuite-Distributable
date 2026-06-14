# HRC_TXN_CONFIG

This table is used to configure the groovy expressions used in tac eg object_name, Effective_date.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconfig-27411.html#hrctxnconfig-27411](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconfig-27411.html#hrctxnconfig-27411)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_DESC_CONFIG_PK | TXN_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_CONFIG_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| PROCESS_ID | NUMBER |  | 18 | Yes | processid of hrc_arm_process_vl |
| VALUE_NAME | VARCHAR2 | 100 |  | Yes | the name of the value to be derived from VALUE_EXPRESSION |
| VALUE_EXPRESSION | VARCHAR2 | 500 |  | Yes | Groovy expression for getting values |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_CONFIG_N20 | Non Unique | Default | SGUID |
| HRC_TXN_DESC_CONFIG_U1 | Unique | Default | PROCESS_ID, ORA_SEED_SET1 |
| HRC_TXN_DESC_CONFIG_U11 | Unique | Default | PROCESS_ID, ORA_SEED_SET2 |
| HRC_TXN_DESC_CONFIG_U2 | Unique | Default | TXN_CONFIG_ID, ORA_SEED_SET1 |
| HRC_TXN_DESC_CONFIG_U21 | Unique | Default | TXN_CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
