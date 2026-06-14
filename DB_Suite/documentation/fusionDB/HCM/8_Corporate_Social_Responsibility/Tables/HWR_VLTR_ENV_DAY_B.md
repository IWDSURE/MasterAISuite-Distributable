# HWR_VLTR_ENV_DAY_B

This tables stores base values of environmental day information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrenvdayb-26360.html#hwrvltrenvdayb-26360](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrenvdayb-26360.html#hwrvltrenvdayb-26360)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_ENV_DAY_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| TYPE | VARCHAR2 | 400 |  |  | TYPE |
| LEARN_MORE_LINK | VARCHAR2 | 400 |  |  | LEARN_MORE_LINK |
| SEQUENCE | NUMBER |  | 18 |  | SEQUENCE |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_ENV_DAY_B_U1 | Unique | Default | ID, ORA_SEED_SET1 |
| HWR_VLTR_ENV_DAY_B_U11 | Unique | Default | ID, ORA_SEED_SET2 |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
