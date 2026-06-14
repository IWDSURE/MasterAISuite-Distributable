# HHR_VLTR_CAUSE_B

This table is created to store the causes

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrcauseb-27350.html#hhrvltrcauseb-27350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrcauseb-27350.html#hhrvltrcauseb-27350)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_CAUSE_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| IS_ENABLED | NUMBER |  | 1 |  | IS_ENABLED |
| IMAGE_ID | NUMBER |  | 18 | Yes | IMAGE_ID |
| IS_SEEDED | NUMBER |  | 1 | Yes | IS_SEEDED |
| IMAGE_URL | VARCHAR2 | 100 |  | Yes | IMAGE_URL |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| IMAGE_URL_1 | VARCHAR2 | 100 |  |  | IMAGE_URL_1 |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_CAUSE_B_U1 | Unique | FUSION_TS_TX_DATA | ID, ORA_SEED_SET1 |
| HHR_VLTR_CAUSE_B_U11 | Unique | FUSION_TS_TX_DATA | ID, ORA_SEED_SET2 |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
