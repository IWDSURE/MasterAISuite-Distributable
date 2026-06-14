# FAI_SAM_BASE_SEQUENCE_DEF_B

This table holds the base sequence definition

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisambasesequencedefb-25242.html#faisambasesequencedefb-25242](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisambasesequencedefb-25242.html#faisambasesequencedefb-25242)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_BASE_SEQUENCE_DEF_B_PK | BASE_SEQUENCE_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BASE_SEQUENCE_DEF_ID | NUMBER |  | 18 | Yes | Primary Key Base Sequence Definition |
| TYPE | VARCHAR2 | 80 |  |  | Type of Base Sequence Definition |
| BASE_SEQUENCE_KEY | VARCHAR2 | 240 |  |  | Key of the Base Sequence Definition |
| SEQUENCER | VARCHAR2 | 240 |  |  | Sequencer of the Base Sequence Defintion |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES table |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_BASE_SEQ_DEF_B_N1 | Non Unique | FUSION_TS_TX_IDX | BASE_SEQUENCE_DEF_ID, TYPE |
| FAI_SAM_BASE_SEQ_DEF_B_PK | Unique | FUSION_TS_SEED | BASE_SEQUENCE_DEF_ID, ORA_SEED_SET1 |
| FAI_SAM_BASE_SEQ_DEF_B_PK1 | Unique | FUSION_TS_SEED | BASE_SEQUENCE_DEF_ID, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
