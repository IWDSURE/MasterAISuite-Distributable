# HWR_DI_CON_IMP_EXP

This table is used to store the content of imported/exported flows.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiconimpexp-6425.html#hwrdiconimpexp-6425](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiconimpexp-6425.html#hwrdiconimpexp-6425)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_CON_IMP_EXP_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the id column of the connector import export table. |
| UUID | VARCHAR2 | 500 |  |  | This is the unique Identifier of the connector transaction created during object creation. |
| NAME | VARCHAR2 | 500 |  |  | This is the file name of the connector transaction. |
| CONTENT | CLOB |  |  |  | This is the content of the connector transaction. It represents the different artifact necessary create a connector. |
| TRANSACTION_TYPE | VARCHAR2 | 20 |  |  | This is the column TRANSACTION_TYPE, expected value is either IMPORT or EXPORT |
| VERSION | VARCHAR2 | 20 |  |  | This is the version of the api used to generate the connector transaction. |
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
| HWR_DI_CON_IMP_EXP_U1 | Unique | Default | ID, ORA_SEED_SET1 |
| HWR_DI_CON_IMP_EXP_U11 | Unique | Default | ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
