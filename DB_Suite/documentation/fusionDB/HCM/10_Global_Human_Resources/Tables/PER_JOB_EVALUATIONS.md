# PER_JOB_EVALUATIONS

PER_JOB_EVALUATIONS holds the schemes and systems that the Enterprise uses to evaluate the jobs and positions stored in PER_JOBS_F and HR_ALL_POSITIONS_F. For each one, either the JOB_ID column or the POSITION_ID column will be populated, but not both.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobevaluations-29058.html#perjobevaluations-29058](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobevaluations-29058.html#perjobevaluations-29058)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_EVALUATION_PK | JOB_EVALUATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| JOB_EVALUATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| JOB_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOBS_F table. |  | Active |
| POSITION_ID | NUMBER |  | 18 |  | Foreign Key to HR_ALL_POSITIONS_F table. |  | Active |
| EVALUATION_SYSTEM | VARCHAR2 | 30 |  | Yes | Evaluation system used for jobs or positions, for example Hay System. |  | Active |
| DATE_EVALUATED | DATE |  |  | Yes | Date of the evaluation. |  | Active |
| MEASURED_IN | VARCHAR2 | 30 |  |  | Measurement unit for the evaluation, for example points. |  |  |
| OVERALL_SCORE | NUMBER |  | 18 |  | Total number of points for the seeded hay evaluation system. |  | Active |
| ACCOUNTABILITY | NUMBER |  | 18 |  | Accountability is a seeded criterion for the hay evaluation system. |  | Active |
| KNOWHOW | NUMBER |  | 18 |  | Knowhow is a seeded criterion for the hay evaluation system. |  | Active |
| PROBLEM_SOLVING | NUMBER |  | 18 |  | Problem Solving is a seeded criterion for the hay evaluation system. |  |  |
| WORKING_CONDITIONS | NUMBER |  | 18 |  | Working Conditions is a seeded criterion for the hay evaluation system. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Evaluation Criteria Attributes (PER_EVALUATION_CRITERIA_DFF) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_JOB_EVALUATIONS_N1 | Non Unique | FUSION_TS_TX_DATA | BUSINESS_GROUP_ID |  |
| PER_JOB_EVALUATIONS_N2 | Non Unique | FUSION_TS_TX_DATA | JOB_ID | Active |
| PER_JOB_EVALUATIONS_N3 | Non Unique | FUSION_TS_TX_DATA | POSITION_ID |  |
| PER_JOB_EVALUATIONS_PK | Unique | Default | JOB_EVALUATION_ID |  |
| PER_JOB_EVALUATIONS_U1 | Unique | Default | LAST_UPDATE_DATE, JOB_EVALUATION_ID |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
