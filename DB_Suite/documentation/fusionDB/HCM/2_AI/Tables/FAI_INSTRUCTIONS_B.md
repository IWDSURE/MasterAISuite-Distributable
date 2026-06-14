# FAI_INSTRUCTIONS_B

This table stores instruction information.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiinstructionsb-22084.html#faiinstructionsb-22084](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiinstructionsb-22084.html#faiinstructionsb-22084)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_INSTRUCTIONS_B_PK | INSTRUCTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTRUCTION_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies instructions. |
| TOPIC_ID | NUMBER |  | 18 | Yes | Foreign key to FAI_TOPIC_B table. |
| INSTRUCTION_CODE | VARCHAR2 | 200 |  | Yes | Uniquely identifies instructions. |
| INTERNAL_NAME | VARCHAR2 | 200 |  | Yes | Internal name normally used by systems. |
| SEEDED_FLAG | VARCHAR2 | 1 |  | Yes | This column differentiates seeded data from customer created. |
| INSTRUCTION | CLOB |  |  |  | This column stores the instruction content. |
| STATUS | VARCHAR2 | 32 |  |  | This column provides topic status. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_INSTRUCTIONS_B_U1 | Unique | Default | INSTRUCTION_ID, ORA_SEED_SET1 |
| FAI_INSTRUCTIONS_B_U11 | Unique | Default | INSTRUCTION_ID, ORA_SEED_SET2 |
| FAI_INSTRUCTIONS_B_U2 | Unique | Default | INSTRUCTION_CODE, ORA_SEED_SET1 |
| FAI_INSTRUCTIONS_B_U21 | Unique | Default | INSTRUCTION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
