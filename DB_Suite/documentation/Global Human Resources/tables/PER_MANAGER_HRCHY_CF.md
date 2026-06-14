# PER_MANAGER_HRCHY_CF

This table stores the column flattened manager hierarchy details. The denormalized details are derived from the supervisors tables and stored in this table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchycf-14278.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchycf-14278.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Uniquely identifies an person. Foreign key to PER_ALL_PEOPLE_F | Active |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies an assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| MANAGER_TYPE | VARCHAR2 | 30 |  | Yes | Identifies the role this supervisor has with regards to the overall organization structure: functional, project leader, etc. | Active |
| LEVEL1_MANAGER_ID | NUMBER |  | 18 | Yes | Uniquely identifies an LEVEL1 manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL1_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies the LEVEL1 manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL2_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies an LEVEL 2	 manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL2_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 2  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL3_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 3  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL3_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 3  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL4_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 4  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL4_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 4  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL5_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 5  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL5_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 5  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL6_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 6  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL6_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 6  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL7_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 7  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL7_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 7  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL8_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 8  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL8_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 8  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL9_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 9  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL9_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 9  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL10_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 10  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL10_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 10  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL11_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 11  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL11_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 11  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL12_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 12  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL12_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 12  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL13_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 13  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL13_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 13  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL14_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 14  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL14_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 14  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL15_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 15  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL15_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 15  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL16_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 16  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL16_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 16  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL17_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 17  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL17_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 17  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL18_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 18  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL18_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 18  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL19_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 19  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL19_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 19  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL20_MANAGER_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 20  manager's person record. Foreign key to PER_ALL_PEOPLE_F. |  |
| LEVEL20_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 20  manager's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_MANAGER_HRCHY_CF_N1 | Non Unique | Default | ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, MANAGER_TYPE |
| PER_MANAGER_HRCHY_CF_U1 | Unique | Default | PERSON_ID, ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, MANAGER_TYPE, LEVEL1_MANAGER_ID, LEVEL1_MANAGER_ASSIGNMENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
