# HWR_VLTR_FILE

This table stores upload file informations

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrfile-5955.html#hwrvltrfile-5955](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrfile-5955.html#hwrvltrfile-5955)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_FILE_PK | FILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILE_ID | NUMBER |  | 18 | Yes | FILE_ID |
| FILE_TYPE | VARCHAR2 | 100 |  |  | FILE_TYPE |
| FILE_NAME | VARCHAR2 | 100 |  |  | FILE_NAME |
| FILE_DATA | BLOB |  |  |  | FILE_DATA |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CROPPED_COORDINATES | CLOB |  |  |  | CROPPED_COORDINATES |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_FILE_U1 | Unique | Default | FILE_ID, ORA_SEED_SET1 |
| HWR_VLTR_FILE_U11 | Unique | Default | FILE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
