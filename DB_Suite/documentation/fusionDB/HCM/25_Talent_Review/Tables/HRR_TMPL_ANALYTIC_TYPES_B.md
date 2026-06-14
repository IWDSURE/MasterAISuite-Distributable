# HRR_TMPL_ANALYTIC_TYPES_B

Talent Review Analytic Types table. This table is used to store different analytic types used in a graph (example, BOX_CHART)

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplanalytictypesb-25841.html#hrrtmplanalytictypesb-25841](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplanalytictypesb-25841.html#hrrtmplanalytictypesb-25841)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_TMPL_ANALYTIC_TYPES_B_PK | ANALYTIC_TYPE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ANALYTIC_TYPE_ID | NUMBER |  | 18 | Yes | Primary key of HRR_TMPL_ANALYTIC_TYPES_B |  |
| ANALYTIC_VIEW_MODE | VARCHAR2 | 30 |  | Yes | Defines if box view is XY mode or Single Measure mode |  |
| METRIC_CODE | VARCHAR2 | 30 |  |  | Specifies the metric to be used for Single measure view |  |
| DEFAULT_VIEW_FLAG | VARCHAR2 | 30 |  |  | Flag to specify if the current view is the default view |  |
| SUBMIT_BOX_ASGNMNT_FLAG | VARCHAR2 | 30 |  |  | Flag to check if the box labels need to be pushed to Profiles |  |
| VIEW_ROW_COUNT | VARCHAR2 | 30 |  |  | Specifies the number of rows for the single measure mode |  |
| VIEW_COLUMN_COUNT | VARCHAR2 | 30 |  |  | Specifies the number of columns for the single measure mode |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| DASHBOARD_TMPL_ID | NUMBER |  | 18 | Yes | Foreign Key of HRR_DASHBOARD_TMPLS_B |  |
| ANALYTIC_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Type of analytic graph. |  |
| HORIZONTAL_AXIS_CODE | VARCHAR2 | 30 |  |  | Horizontal axis value. |  |
| VERTICAL_AXIS_CODE | VARCHAR2 | 30 |  |  | Vertical axis value. |  |
| HORZ_RATING_MODEL_ID | NUMBER |  | 18 |  | Horizontal Rating Model Id | Obsolete |
| VERT_RATING_MODEL_ID | NUMBER |  | 18 |  | Vertical Rating Model Id | Obsolete |
| SCORE_RATING_MODEL_ID | NUMBER |  | 18 |  | Rating model for calibrating talent score. | Obsolete |
| RISK_RATING_MODEL_ID | NUMBER |  | 18 |  | Risk of Loss rating Model Id | Obsolete |
| IMPACT_RATING_MODEL_ID | NUMBER |  | 18 |  | Impact of Loss rating Model Id | Obsolete |
| COLOR_SCHEME_CODE | VARCHAR2 | 30 |  |  | Chart Box Color Scheme |  |
| DEFAULT_VIEW_TYPE | VARCHAR2 | 30 |  |  | Indicates the default view type in dashboard template | Obsolete |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
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
| HRR_TMPL_ANALYTIC_TYPES_B_N1 | Non Unique | FUSION_TS_TX_DATA | BUSINESS_GROUP_ID |
| HRR_TMPL_ANALYTIC_TYPES_B_N2 | Non Unique | FUSION_TS_TX_DATA | DASHBOARD_TMPL_ID, BUSINESS_GROUP_ID |
| HRR_TMPL_ANALYTIC_TYPES_B_U1 | Unique | FUSION_TS_TX_DATA | ANALYTIC_TYPE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
