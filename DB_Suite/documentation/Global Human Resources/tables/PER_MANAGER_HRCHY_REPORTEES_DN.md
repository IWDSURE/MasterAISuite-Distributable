# PER_MANAGER_HRCHY_REPORTEES_DN

This table stores the column flattened manager hierarchy details. The denormalized details are derived from the supervisors tables and stored in this table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchyreporteesdn-19752.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchyreporteesdn-19752.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| MANAGER_ID | NUMBER |  | 18 | Yes | Uniquely identifies a person.Foreign key to PER_ALL_PEOPLE_F . | Active |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies an assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| MANAGER_TYPE | VARCHAR2 | 30 |  | Yes | Identifies the role this supervisor has with regards to the overall organization structure: functional, project leader, etc. | Active |
| MANAGER_LEVEL | NUMBER |  | 5 | Yes | MANAGER_LEVEL |  |
| LEVEL1_REPORTEE_PERSON_ID | NUMBER |  | 18 | Yes | Uniquely identifies an LEVEL1 reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL1_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies the LEVEL1 reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL2_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies an LEVEL 2	 reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL2_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 2  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL3_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 3  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL3_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 3  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL4_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 4  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL4_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 4  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL5_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 5  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL5_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 5  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL6_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 6  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL6_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 6  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL7_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 7  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL7_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 7  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL8_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 8  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL8_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 8  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL9_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 9  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL9_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 9  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL10_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 10  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL10_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 10  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL11_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 11  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL11_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 11  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL12_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 12  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL12_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 12  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL13_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 13  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL13_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 13  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL14_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 14  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL14_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 14  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL15_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 15  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL15_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 15  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL16_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 16  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL16_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 16  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL17_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 17  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL17_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 17  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL18_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 18  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL18_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 18  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL19_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 19  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL19_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 19  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
| LEVEL20_REPORTEE_PERSON_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 20  reportee's person record. Foreign key to PER_ALL_PEOPLE_F' |  |
| LEVEL20_REPORTEE_ASSIGNMENT_ID | NUMBER |  | 18 |  | Uniquely identifies the LEVEL 20  reportee's assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  |
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
| PER_MANAGER_HRCHY_REPORTEES_N1 | Non Unique | Default | MANAGER_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, MANAGER_TYPE, MANAGER_LEVEL |
| PER_MANAGER_HRCHY_REPORTEES_N2 | Non Unique | Default | LEVEL15_REPORTEE_PERSON_ID, LEVEL15_REPORTEE_ASSIGNMENT_ID |
| PER_MANAGER_HRCHY_REPORTEES_N3 | Non Unique | Default | LEVEL1_REPORTEE_PERSON_ID, LEVEL1_REPORTEE_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, MANAGER_TYPE |
| PER_MANAGER_HRCHY_REPORTEES_N4 | Non Unique | Default | LEVEL1_REPORTEE_ASSIGNMENT_ID, MANAGER_ASSIGNMENT_ID, EFFECTIVE_END_DATE, MANAGER_LEVEL |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
