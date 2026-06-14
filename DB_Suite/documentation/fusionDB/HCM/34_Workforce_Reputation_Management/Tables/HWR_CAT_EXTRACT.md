# HWR_CAT_EXTRACT

This table contains category BLOB information

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcatextract-23651.html#hwrcatextract-23651](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcatextract-23651.html#hwrcatextract-23651)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CAT_EXTRACT_PK | EXTRACTION_FILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTRACTION_FILE_ID | NUMBER |  | 18 | Yes | This column defines the id of the extraction file |
| NAME | VARCHAR2 | 80 |  | Yes | This column contains the name of the extraction file |
| EXTRACTION_FILE | BLOB |  |  | Yes | This column contains the content of the extraction file. |
| LOCALE | VARCHAR2 | 20 |  | Yes | This column contains the locale of the extraction file. |
| TYPE | VARCHAR2 | 80 |  | Yes | This column contains the type of the extraction file. |
| PRODUCT | VARCHAR2 | 80 |  | Yes | This column contains the porduct code of the extraction file. |
| IS_SEEDED_DATA | VARCHAR2 | 1 |  | Yes | A flag to indicate the whether the extraction file is seeded: Y for yes, N for no |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| HWR_CAT_EXTRACT_U1 | Unique | FUSION_TS_SEED | EXTRACTION_FILE_ID, ORA_SEED_SET1 |
| HWR_CAT_EXTRACT_U11 | Unique | FUSION_TS_SEED | EXTRACTION_FILE_ID, ORA_SEED_SET2 |
| HWR_CAT_EXTRACT_U2 | Unique | FUSION_TS_SEED | NAME, LOCALE, TYPE, PRODUCT, ORA_SEED_SET1 |
| HWR_CAT_EXTRACT_U21 | Unique | FUSION_TS_SEED | NAME, LOCALE, TYPE, PRODUCT, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
