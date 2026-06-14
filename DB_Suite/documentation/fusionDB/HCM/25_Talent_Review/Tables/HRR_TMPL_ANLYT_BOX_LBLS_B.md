# HRR_TMPL_ANLYT_BOX_LBLS_B

Talent Review Analytic Types table. This table s used to store labels for box chart boxes.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplanlytboxlblsb-21523.html#hrrtmplanlytboxlblsb-21523](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrtmplanlytboxlblsb-21523.html#hrrtmplanlytboxlblsb-21523)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_TMPL_ANLYT_BOX_LBLS_B_PK | ANALYTIC_BOX_LABEL_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ANALYTIC_BOX_LABEL_ID | NUMBER |  | 18 | Yes | Primary Key of HRR_ANALYTIC_BOX_LABELS |  |
| BOXCELL_BACKGROUND_COLOR | VARCHAR2 | 2000 |  |  | Background color on each nbox cell for XY rating view. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| ANALYTIC_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRR_ANALYTIC_TYPES_B table. |  |
| BOX_SEQUENCE | NUMBER |  | 18 | Yes | Sequence number of each box in the graph (box_chart). For box chart graph the assumption is box sequence will be bottom up and left to right. |  |
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
| HRR_TMPL_ANLYT_BOX_LBLS_B_N1 | Non Unique | FUSION_TS_TX_DATA | ANALYTIC_TYPE_ID, BUSINESS_GROUP_ID |
| HRR_TMPL_ANLYT_BOX_LBLS_B_U1 | Unique | FUSION_TS_TX_DATA | ANALYTIC_BOX_LABEL_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
