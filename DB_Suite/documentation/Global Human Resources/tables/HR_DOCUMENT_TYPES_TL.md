# HR_DOCUMENT_TYPES_TL

Translated Document Types for Documents of Record.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumenttypestl-10200.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumenttypestl-10200.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_DOCUMENT_TYPES_TL_PK | DOCUMENT_TYPE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DOCUMENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to table HR_DOCUMENT_TYPES |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| DOCUMENT_TYPE | VARCHAR2 | 80 |  | Yes | Translated name of document type. |  |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Translated description of document type. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| DOCUMENT_NAME_LABEL | VARCHAR2 | 200 |  |  | Translated label text for document name |  |
| DOCUMENT_NUMBER_LABEL | VARCHAR2 | 200 |  |  | Translated label text for document number |  |
| DATE_FROM_LABEL | VARCHAR2 | 200 |  |  | Translated label text for date from |  |
| DATE_TO_LABEL | VARCHAR2 | 200 |  |  | Translated label text for date to |  |
| ISSUING_AUTHORITY_LABEL | VARCHAR2 | 200 |  |  | Translated label text for issuing authority |  |
| ISSUED_DATE_LABEL | VARCHAR2 | 200 |  |  | Translated label text for issued date |  |
| ISSUING_COUNTRY_LABEL | VARCHAR2 | 200 |  |  | Translated label text for issuing country |  |
| ISSUING_LOCATION_LABEL | VARCHAR2 | 200 |  |  | Translated label text for issuing location |  |
| COMMENTS_LABEL | VARCHAR2 | 200 |  |  | Translated label text for comments |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_DOCUMENT_TYPES_TL_U1 | Unique | FUSION_TS_TX_IDX | DOCUMENT_TYPE_ID, LANGUAGE, ORA_SEED_SET1 |
| HR_DOCUMENT_TYPES_TL_U11 | Unique | FUSION_TS_TX_IDX | DOCUMENT_TYPE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
