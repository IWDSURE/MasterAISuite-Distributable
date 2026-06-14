# HRA_TMPL_PERIODS_TL

This table stores the translated Template Periods.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplperiodstl-5561.html#hratmplperiodstl-5561](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplperiodstl-5561.html#hratmplperiodstl-5561)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_TMPL_PERIODS_TL_PK | TMPL_PERIOD_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TMPL_PERIOD_ID | NUMBER |  | 18 | Yes | Foreign key of Template Periods and part of the composite primary key |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| CUSTOMARY_NAME | VARCHAR2 | 240 |  | Yes | Translated customary name of Template Periods. |  |
| SHORT_NAME | VARCHAR2 | 10 |  | Yes | Indicates a short version of the customary name. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_TMPL_PERIODS_TL_N1 | Non Unique | Default | CUSTOMARY_NAME, LANGUAGE |
| HRA_TMPL_PERIODS_TL_N2 | Non Unique | Default | UPPER("CUSTOMARY_NAME") |
| HRA_TMPL_PERIODS_TL_PK | Unique | Default | TMPL_PERIOD_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
