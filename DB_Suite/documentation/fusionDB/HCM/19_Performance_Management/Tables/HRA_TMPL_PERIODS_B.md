# HRA_TMPL_PERIODS_B

This table stores the time periods for the template. For example, the Annual Appraisal template can have the time periods of FY07 and FY08, with different customary names for both

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplperiodsb-3279.html#hratmplperiodsb-3279](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplperiodsb-3279.html#hratmplperiodsb-3279)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_TMPL_PERIODS_B_PK | TMPL_PERIOD_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TMPL_PERIOD_ID | NUMBER |  | 18 | Yes | Primary key of Template Periods. |  |
| GOAL_ALGORITHM_TYPE_CODE | VARCHAR2 | 30 |  |  | Method used to populate goals while creating performance documents and importing goals |  |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | Indicates the Review Period that is used for each template period in template definition. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| TEMPLATE_DEFN_ID | NUMBER |  | 18 | Yes | Foreign key of Template Definition. |  |
| NOMINAL_FROM_DATE | DATE |  |  | Yes | Indicates the nominal start date of the performance period. |  |
| NOMINAL_TO_DATE | DATE |  |  | Yes | Indicates the nominal end date of the performance period. |  |
| AVAILABLE_TO_USE | VARCHAR2 | 30 |  |  | Flag indicating whether the template period is visible to user. |  |
| LOCK_MGR_SHARE_FOR_CALIB_FLAG | VARCHAR2 | 30 |  |  | Indicates that manager share document task is locked for template period. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_TMPL_PERIODS_B_N1 | Non Unique | Default | TEMPLATE_DEFN_ID |
| HRA_TMPL_PERIODS_B_PK | Unique | Default | TMPL_PERIOD_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
