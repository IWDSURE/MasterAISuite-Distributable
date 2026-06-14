# PER_TALEO_IMPORT_RESULTS

This table stores information about successful candidates imported from Taleo to Fusion

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertaleoimportresults-17491.html#pertaleoimportresults-17491](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertaleoimportresults-17491.html#pertaleoimportresults-17491)

## Primary Key

| Name | Columns |
|------|----------|
| PER_TALEO_IMPORT_RESULTS_PK | TALEO_IMPORT_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TALEO_IMPORT_RESULT_ID | NUMBER |  | 18 | Yes | Primary key Identifier |
| APPLICANT_NUMBER | VARCHAR2 | 20 |  | Yes | Taleo Candidate Identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Identifier |
| DATA_SET_ID | NUMBER |  | 18 | Yes | HDL Batch identifier |
| LOGICAL_LINE_ID | NUMBER |  | 18 | Yes | HDL Batch identifier |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| RUN_DATE | DATE |  |  | Yes | Import   run Date |
| STATUS | VARCHAR2 | 30 |  | Yes | Import Status - Success or Failure |
| LAST_NAME | VARCHAR2 | 150 |  |  | New Hire Candidate Last Name |
| FIRST_NAME | VARCHAR2 | 150 |  |  | New Hire Candidate  First Name |
| MIDDLE_NAMES | VARCHAR2 | 80 |  |  | New Hire Candidate  Middle  Names |
| PROPOSED_START_DATE | DATE |  |  |  | Proposed Hire Date |
| MANAGER_ID | NUMBER |  | 18 |  | MANAGER_ID |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Department Identifier |
| LOCATION_ID | NUMBER |  | 18 |  | Location Identifier |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| WORKER_LOAD_FLAG | VARCHAR2 | 1 |  | Yes | HDL Status for worker load |
| TALENT_PROFILE_LOAD_FLAG | VARCHAR2 | 1 |  | Yes | HDL Status for talent profile load |
| COMP_ELMNT_ENTRY_LOAD_FLAG | VARCHAR2 | 1 |  | Yes | HDL Status for element entry load |
| COMP_SALARY_LOAD_FLAG | VARCHAR2 | 1 |  | Yes | HDL Status for Salary Load |
| REIMPORT_FLAG | VARCHAR2 | 1 |  | Yes | Re-import due to HDL Purge |
| ERROR_CODE | VARCHAR2 | 80 |  |  | Import Error Code |
| ERROR_DESCRIPTION | VARCHAR2 | 4000 |  |  | Import Error Description |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_TALEO_IMPORT_RESULTS_N1 | Non Unique | FUSION_TS_TX_IDX | MANAGER_ID |
| PER_TALEO_IMPORT_RESULTS_N2 | Non Unique | FUSION_TS_TX_IDX | LAST_NAME, FIRST_NAME |
| PER_TALEO_IMPORT_RESULTS_N3 | Non Unique | FUSION_TS_TX_IDX | RUN_DATE |
| PER_TALEO_IMPORT_RESULTS_N4 | Non Unique | FUSION_TS_TX_IDX | STATUS |
| PER_TALEO_IMPORT_RESULTS_N5 | Non Unique | FUSION_TS_TX_IDX | DEPARTMENT_ID |
| PER_TALEO_IMPORT_RESULTS_N6 | Non Unique | FUSION_TS_TX_IDX | LOCATION_ID |
| PER_TALEO_IMPORT_RESULTS_N7 | Non Unique | FUSION_TS_TX_IDX | LEGAL_EMPLOYER_ID |
| PER_TALEO_IMPORT_RESULTS_N8 | Non Unique | FUSION_TS_TX_IDX | BUSINESS_UNIT_ID |
| PER_TALEO_IMPORT_RESULTS_N9 | Non Unique | FUSION_TS_TX_IDX | JOB_ID |
| PER_TALEO_IMPORT_RESULTS_PK | Unique | FUSION_TS_TX_IDX | TALEO_IMPORT_RESULT_ID |
| PER_TALEO_IMP_RES_N10 | Non Unique | FUSION_TS_TX_IDX | POSITION_ID |
| PER_TALEO_IMP_RES_N11 | Non Unique | FUSION_TS_TX_IDX | GRADE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
