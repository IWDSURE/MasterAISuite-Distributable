# HWM_LAYER

A type of time collection in the repository.  For example, reported time, which corresponds to the time card time record group, the day time record group and the time entry time record.  Layers can be abstract, which typically include more than a single layer, e.g., reported time and absence time.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmlayer-17682.html#hwmlayer-17682](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmlayer-17682.html#hwmlayer-17682)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_LAYER_PK | LAYER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LAYER_ID | NUMBER |  | 18 | Yes | TM_MSG_TKNS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAYER_CODE | VARCHAR2 | 20 |  | Yes | LAYER_CODE |
| NAME | VARCHAR2 | 255 |  | Yes | TOKEN_NAME |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| AUDITABLE | VARCHAR2 | 30 |  |  | Yes or No |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_LAYER_U1 | Unique | FUSION_TS_TX_DATA | LAYER_CODE, ORA_SEED_SET1 |
| HWM_LAYER_U11 | Unique | FUSION_TS_TX_DATA | LAYER_CODE, ORA_SEED_SET2 |
| HWM_TM_LAYER_PK | Unique | FUSION_TS_TX_DATA | LAYER_ID, ORA_SEED_SET1 |
| HWM_TM_LAYER_PK1 | Unique | FUSION_TS_TX_DATA | LAYER_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
