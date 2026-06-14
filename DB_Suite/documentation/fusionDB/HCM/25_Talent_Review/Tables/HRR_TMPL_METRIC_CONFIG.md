# HRR_TMPL_METRIC_CONFIG

This mapping table is child table of HRR_DASHBOARD_TMPLS_B and it maps HRR_DASHBOARDS  table and HRR_TMPL_ANALYTIC_TYPES_B table.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplmetricconfig-14713.html#hrrtmplmetricconfig-14713](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplmetricconfig-14713.html#hrrtmplmetricconfig-14713)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_TMPL_METRIC_CONFIG_PK | ENTERPRISE_ID, METRIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| RATING_MODEL_ID | NUMBER |  | 18 | Yes | Rating model of the metric |
| USE_AS_AXIS_FLAG | VARCHAR2 | 30 |  |  | Dashboard template metric flag for use as axis option |
| METRIC_ID | NUMBER |  | 18 | Yes | System generated primary key to this table. |
| USE_AS_UNDERLAY_FLAG | VARCHAR2 | 30 |  |  | Dashboard template metric flag for use as underlay option |
| READ_ONLY_FLAG | VARCHAR2 | 30 |  |  | Dashboard template metric flag for read only option |
| DASHBOARD_TMPL_ID | NUMBER |  | 18 |  | Foreign key to HRR_DASHBOARD_TMPLS_B table |
| METRIC_CODE | VARCHAR2 | 240 |  |  | The metric or rating type which will be mapped in this row. |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Content type id of the rating which will be mapped in this row. |
| DASHBOARD_COLUMN_NAME | VARCHAR2 | 32 |  |  | This indicates column name in HRR_DASHBOARDS table which will be storing the value for the particular METRIC_CODE. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SECTION_ID | NUMBER |  | 18 |  | Section id introduced for the custom talent ratings . |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_TMPL_METRIC_CONFIG_FK1 | Non Unique | FUSION_TS_TX_DATA | DASHBOARD_TMPL_ID, ENTERPRISE_ID |
| HRR_TMPL_METRIC_CONFIG_N1 | Non Unique | FUSION_TS_TX_DATA | SECTION_ID |
| HRR_TMPL_METRIC_CONFIG_PK | Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, METRIC_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
