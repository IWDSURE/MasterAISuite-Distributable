# HRC_DL_CANDIDATE_IMPORTS

HRC_DL_CANDIDATE_IMPORTS table is used to hold details about imported candidates from external system.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlcandidateimports-27407.html#hrcdlcandidateimports-27407](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlcandidateimports-27407.html#hrcdlcandidateimports-27407)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_CANDIDATE_IMPORTS_PK | CANDIDATE_IMPORT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CANDIDATE_IMPORT_ID | NUMBER |  | 18 | Yes | CANDIDATE_IMPORT_ID |
| APPLICANT_NUMBER | VARCHAR2 | 30 |  |  | APPLICANT_NUMBER |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID |
| IMPORT_DATE | DATE |  |  | Yes | IMPORT_DATE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| LAST_NAME | VARCHAR2 | 150 |  |  | LAST_NAME |
| FIRST_NAME | VARCHAR2 | 150 |  |  | FIRST_NAME |
| MIDDLE_NAMES | VARCHAR2 | 80 |  |  | MIDDLE_NAMES |
| PROPOSED_START_DATE | DATE |  |  |  | PROPOSED_START_DATE |
| MANAGER_ID | NUMBER |  | 18 |  | MANAGER_ID |
| DEPARTMENT_ID | NUMBER |  | 18 |  | DEPARTMENT_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| POSITION_ID | NUMBER |  | 18 |  | POSITION_ID |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| WORKER_LOAD_FLAG | VARCHAR2 | 30 |  |  | WORKER_LOAD_FLAG |
| TALENT_PROFILE_LOAD_FLAG | VARCHAR2 | 30 |  |  | TALENT_PROFILE_LOAD_FLAG |
| ELEMENT_ENTRY_LOAD_FLAG | VARCHAR2 | 30 |  |  | ELEMENT_ENTRY_LOAD_FLAG |
| SALARY_LOAD_FLAG | VARCHAR2 | 30 |  |  | SALARY_LOAD_FLAG |
| PAYROLL_ASG_LOAD_FLAG | VARCHAR2 | 30 |  |  | PAYROLL_ASG_LOAD_FLAG |
| SOURCE_SYSTEM_OWNER | VARCHAR2 | 256 |  |  | SOURCE_SYSTEM_OWNER |
| SOURCE_SYSTEM_ID | VARCHAR2 | 2000 |  |  | SOURCE_SYSTEM_ID |
| PERSON_NUMBER | VARCHAR2 | 30 |  |  | PERSON_NUMBER |
| ASSIGNMENT_NUMBER | VARCHAR2 | 50 |  |  | ASSIGNMENT_NUMBER |
| ASG_SOURCE_SYSTEM_ID | VARCHAR2 | 2000 |  |  | ASG_SOURCE_SYSTEM_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| LEGISLATION_CODE | VARCHAR2 | 150 |  |  | LEGISLATION_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PROPOSED_WORKER_SYSTEM_TYPE | VARCHAR2 | 30 |  |  | PROPOSED_WORKER_SYSTEM_TYPE |
| PROPOSED_WORKER_TYPE_ID | NUMBER |  | 18 |  | PROPOSED_WORKER_TYPE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_CANDIDATE_IMPORTS_N1 | Non Unique | Default | DATA_SET_ID |
| HRC_DL_CANDIDATE_IMPORTS_N2 | Non Unique | Default | ENTERPRISE_ID, MANAGER_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMPORTS_N3 | Non Unique | Default | APPLICANT_NUMBER |
| HRC_DL_CANDIDATE_IMPORTS_N4 | Non Unique | Default | SOURCE_SYSTEM_OWNER, SOURCE_SYSTEM_ID |
| HRC_DL_CANDIDATE_IMPORTS_N5 | Non Unique | Default | PERSON_NUMBER |
| HRC_DL_CANDIDATE_IMPORTS_N6 | Non Unique | Default | ASSIGNMENT_NUMBER |
| HRC_DL_CANDIDATE_IMPORTS_N7 | Non Unique | Default | SOURCE_SYSTEM_OWNER, ASG_SOURCE_SYSTEM_ID |
| HRC_DL_CANDIDATE_IMPORTS_N8 | Non Unique | Default | ASSIGNMENT_ID |
| HRC_DL_CANDIDATE_IMPORTS_N9 | Non Unique | Default | ENTERPRISE_ID, LAST_NAME, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMPORTS_U1 | Unique | Default | CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMPORTS_U2 | Unique | Default | PERSON_ID |
| HRC_DL_CANDIDATE_IMP_N10 | Non Unique | Default | ENTERPRISE_ID, FIRST_NAME, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N11 | Non Unique | Default | ENTERPRISE_ID, DEPARTMENT_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N12 | Non Unique | Default | ENTERPRISE_ID, LOCATION_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N13 | Non Unique | Default | ENTERPRISE_ID, LEGAL_EMPLOYER_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N14 | Non Unique | Default | ENTERPRISE_ID, BUSINESS_UNIT_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N15 | Non Unique | Default | ENTERPRISE_ID, JOB_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N16 | Non Unique | Default | ENTERPRISE_ID, POSITION_ID, CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_IMP_N17 | Non Unique | Default | ENTERPRISE_ID, GRADE_ID, CANDIDATE_IMPORT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
