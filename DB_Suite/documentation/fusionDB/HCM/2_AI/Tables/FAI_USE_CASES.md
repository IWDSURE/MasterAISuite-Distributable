# FAI_USE_CASES

This table contains prompt use cases in which Generative AI is employed.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiusecases-25988.html#faiusecases-25988](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiusecases-25988.html#faiusecases-25988)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_USE_CASES_PK | USE_CASE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USE_CASE_ID | VARCHAR2 | 32 |  | Yes | The system generated surrogate key. |
| USE_CASE_IDENTIFIER | VARCHAR2 | 80 |  | Yes | This column indicates the prompt use case. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_USE_CASES_U1 | Unique | Default | USE_CASE_ID, ORA_SEED_SET1 |
| FAI_USE_CASES_U11 | Unique | Default | USE_CASE_ID, ORA_SEED_SET2 |
| FAI_USE_CASES_U2 | Unique | Default | USE_CASE_IDENTIFIER, ORA_SEED_SET1 |
| FAI_USE_CASES_U21 | Unique | Default | USE_CASE_IDENTIFIER, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
