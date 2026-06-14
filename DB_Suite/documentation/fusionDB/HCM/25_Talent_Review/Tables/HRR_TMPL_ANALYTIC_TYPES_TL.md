# HRR_TMPL_ANALYTIC_TYPES_TL

This is the langugae table for analytic types

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplanalytictypestl-26623.html#hrrtmplanalytictypestl-26623](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplanalytictypestl-26623.html#hrrtmplanalytictypestl-26623)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_TMPL_ANALYTIC_TYPES_TL_PK | ANALYTIC_TYPE_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ANALYTIC_TYPE_ID | NUMBER |  | 18 | Yes | Primary Key of HRR_ANALYTIC_TYPES_TL |  |
| ANALYTIC_VIEW_NAME | VARCHAR2 | 240 |  | Yes | View Name of the Box chart |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| VERTICAL_AXIS_LABEL | VARCHAR2 | 400 |  |  | Label of Vertical Axis | Obsolete |
| HORIZONTAL_AXIS_LABEL | VARCHAR2 | 400 |  |  | Label of Horizontal Axis | Obsolete |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRR_TMPL_ANALYTIC_TYPES_TL_N1 | Non Unique | FUSION_TS_TX_DATA | ANALYTIC_TYPE_ID, BUSINESS_GROUP_ID | Obsolete |
| HRR_TMPL_ANALYTIC_TYPES_TL_U1 | Unique | FUSION_TS_TX_DATA | ANALYTIC_TYPE_ID, BUSINESS_GROUP_ID, LANGUAGE |  |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
