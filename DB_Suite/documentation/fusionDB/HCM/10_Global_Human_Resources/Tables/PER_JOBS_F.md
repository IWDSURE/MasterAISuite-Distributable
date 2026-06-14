# PER_JOBS_F

PER_JOBS_F holds jobs that have been defined for an Enterprise. Jobs define the role that an employee can perform in the enterprise, and they are independent of specific organizations.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobsf-21081.html#perjobsf-21081](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobsf-21081.html#perjobsf-21081)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOBS_F_PK | JOB_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  | Active |
| PROGRESSION_JOB_ID | NUMBER |  | 18 |  | Next possible job during promotion |  |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  | Active |
| JOB_CODE | VARCHAR2 | 30 |  | Yes | Code of the job. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| SET_ID | NUMBER |  | 18 | Yes | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |  | Active |
| BENCHMARK_JOB_ID | NUMBER |  | 18 |  | Identifier of the benchmark job. |  | Active |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOB_FAMILY_F table. |  | Active |
| JOB_SUB_FAMILY | VARCHAR2 | 30 |  |  | Sub Family that the Job is grouped in. |  |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |  |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Indicates if a job is active or inactive. |  | Active |
| BENCHMARK_JOB_FLAG | VARCHAR2 | 30 |  |  | Indicates if this job is a benchmark job. |  | Active |
| APPROVAL_AUTHORITY | NUMBER |  | 38 |  | Integer number to identify levels across jobs which are used for approvals if the job list builder is used. |  | Active |
| SCHEDULING_GROUP | VARCHAR2 | 30 |  |  | Scheduling Group of the job. All the jobs belonging to a scheduling group follow a common work schedule. |  |  |
| MANAGER_LEVEL | VARCHAR2 | 30 |  |  | Indicates the management level of the job. |  |  |
| MED_CHECKUP_REQ | VARCHAR2 | 30 |  |  | Indicates if the job requires medical checkup. |  | Active |
| STANDARD_WORKING_HOURS | NUMBER |  | 22 |  | Number of standard working hours. |  |  |
| STANDARD_WORKING_FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the standard working hours. |  |  |
| STD_ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The standard annual working duration for the job. |  |  |
| ANNUAL_WORKING_DURATION_UNITS | VARCHAR2 | 10 |  |  | The unit of measure in hours, days, weeks, or months for the standard annual working duration. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| CATEGORY_CODE | VARCHAR2 | 80 |  | Yes | Extensible Flexfield Category Code |  |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Attributes (PER_JOBS_DFF) |  |
| REGULAR_TEMPORARY | VARCHAR2 | 30 |  |  | Indicates if a job is regular or temporary. |  | Active |
| FULL_PART_TIME | VARCHAR2 | 30 |  |  | Indicates if a job is full-time or part-time. |  | Active |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Code of the job function. |  | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | Grade Ladder |  |  |
| REQUISITION_TEMPLATE_ID | NUMBER |  | 18 |  | Identifier of the Requisition Template |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_JOBS_F_N11 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| PER_JOBS_F_N12 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| PER_JOBS_F_N13 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| PER_JOBS_F_N14 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| PER_JOBS_F_N15 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| PER_JOBS_F_N16 | Non Unique | Default | ATTRIBUTE6 |
| PER_JOBS_F_N17 | Non Unique | Default | ATTRIBUTE7 |
| PER_JOBS_F_N18 | Non Unique | Default | ATTRIBUTE8 |
| PER_JOBS_F_N19 | Non Unique | Default | ATTRIBUTE9 |
| PER_JOBS_F_N2 | Non Unique | FUSION_TS_TX_DATA | BUSINESS_GROUP_ID |
| PER_JOBS_F_N20 | Non Unique | Default | ATTRIBUTE10 |
| PER_JOBS_F_N3 | Non Unique | FUSION_TS_TX_DATA | SET_ID |
| PER_JOBS_F_N31 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| PER_JOBS_F_N32 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| PER_JOBS_F_N33 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| PER_JOBS_F_N34 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| PER_JOBS_F_N35 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| PER_JOBS_F_N4 | Non Unique | FUSION_TS_TX_DATA | UPPER("JOB_CODE") |
| PER_JOBS_F_N41 | Non Unique | Default | ATTRIBUTE_DATE1 |
| PER_JOBS_F_N42 | Non Unique | Default | ATTRIBUTE_DATE2 |
| PER_JOBS_F_N43 | Non Unique | Default | ATTRIBUTE_DATE3 |
| PER_JOBS_F_N44 | Non Unique | Default | ATTRIBUTE_DATE4 |
| PER_JOBS_F_N45 | Non Unique | Default | ATTRIBUTE_DATE5 |
| PER_JOBS_F_PK | Unique | FUSION_TS_TX_DATA | JOB_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_JOBS_F_U1 | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, JOB_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
