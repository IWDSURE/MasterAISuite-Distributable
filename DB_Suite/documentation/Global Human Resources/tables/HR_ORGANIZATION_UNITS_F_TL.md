# HR_ORGANIZATION_UNITS_F_TL

This table stores the translatable data for  HR_ALL_ORGANIZATION_UNITS_F.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationunitsftl-10676.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationunitsftl-10676.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ORGANIZATION_UNITS_F_TL_PK | ORGANIZATION_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 240 |  | Yes | Denotes the translated name for the Organization Unit. |
| TITLE | VARCHAR2 | 240 |  |  | Denotes the translated title for the Organization Unit. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ALL_ORG_UNITS_F_TL_N1 | Non Unique | Default | LANGUAGE, NAME |
| HR_ALL_ORG_UNITS_F_TL_N3 | Non Unique | Default | LAST_UPDATE_DATE |
| HR_ORGANIZATION_UNITS_F_TL_N2 | Non Unique | Default | UPPER("NAME"), LANGUAGE, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |
| HR_ORGANIZATION_UNITS_F_TL_N4 | Non Unique | Default | LANGUAGE, TITLE |
| HR_ORGANIZATION_UNITS_F_TL_N5 | Non Unique | Default | UPPER("TITLE"), LANGUAGE, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |
| HR_ORGANIZATION_UNITS_F_TL_PK | Unique | Default | ORGANIZATION_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
