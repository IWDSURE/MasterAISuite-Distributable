# PAY_ELE_CLASSIFICATIONS_TL

This table contains translation information for PAY_ELE_CLASSIFICATIONS.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeleclassificationstl-28911.html#payeleclassificationstl-28911](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeleclassificationstl-28911.html#payeleclassificationstl-28911)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_CLASSIFICATIONS_TL_PK | CLASSIFICATION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASSIFICATION_ID | NUMBER |  | 18 | Yes | CLASSIFICATION_ID |
| CLASSIFICATION_NAME | VARCHAR2 | 120 |  | Yes | CLASSIFICATION_NAME |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| DESCRIPTION | VARCHAR2 | 80 |  |  | DESCRIPTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ELE_CLASSIFICATIONS_TL_N1 | Non Unique | Default | CLASSIFICATION_NAME, LANGUAGE |
| PAY_ELE_CLASSIFICATIONS_TL_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_ELE_CLASSIFICATIONS_TL_N3 | Non Unique | Default | UPPER("CLASSIFICATION_NAME") |
| PAY_ELE_CLASSIFICATIONS_TL_PK | Unique | Default | CLASSIFICATION_ID, LANGUAGE, ORA_SEED_SET1 |
| PAY_ELE_CLASSIFICATIONS_TL_PK1 | Unique | Default | CLASSIFICATION_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
