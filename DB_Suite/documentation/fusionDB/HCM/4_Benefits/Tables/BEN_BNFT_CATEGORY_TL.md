# BEN_BNFT_CATEGORY_TL

BEN_BNFT_CATEGORY_TL holds MLS translated data from main table, BEN_BNFT_CATEGORY.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftcategorytl-10682.html#benbnftcategorytl-10682](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftcategorytl-10682.html#benbnftcategorytl-10682)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BNFT_CATEGORY_TL_PK | CATEGORY_CD, USAGE_CD, LANGUAGE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_CD | VARCHAR2 | 30 |  | Yes | Foreign Key to BEN_BNFT_CATEGORY. |
| USAGE_CD | VARCHAR2 | 30 |  | Yes | Foreign Key to BEN_BNFT_CATEGORY. |
| USER_NAME | VARCHAR2 | 200 |  |  | Name of the translated user name. |
| PRMRY_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated primary rate label. |
| SCNDRY_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated secondary rate label. |
| OTHR_PRETAX_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated other pretax rate label. |
| OTHR_AFTERTAX_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated other aftertax rate label. |
| OTHR_TAXABLE_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated other taxable rate label. |
| OTHR_NONTAX_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated other nontax rate label. |
| OTHR_NOTAPPLICABLE_RT_LABEL | VARCHAR2 | 128 |  | Yes | Name of the translated other not applicable rate label. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CATEGORY_HELP_TEXT | CLOB |  |  |  | Translated help text for the corresponding self service or administrative usage code. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BNFT_CATEGORY_TL_U1 | Unique | Default | CATEGORY_CD, USAGE_CD, LANGUAGE, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| BEN_BNFT_CATEGORY_TL_U2 | Unique | BEN_BNFT_CATEGORY_TL_U2 | CATEGORY_CD, USAGE_CD, LANGUAGE, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
