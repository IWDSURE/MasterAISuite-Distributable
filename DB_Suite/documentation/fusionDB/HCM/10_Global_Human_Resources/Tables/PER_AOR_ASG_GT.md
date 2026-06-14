# PER_AOR_ASG_GT

This global temporary table holds the details of assignment details for a thread and this will be used to calculate assignment representatives .

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorasggt-25356.html#peraorasggt-25356](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraorasggt-25356.html#peraorasggt-25356)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | This is a system generated primary key. Surrogate key. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies person holding an assignment or a set of Employment/Placement Terms. Foreign key to PER_PERSONS. |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  | Yes | Identifies the type of record: either assignment (employee, CWK, applicant, non-workers) or a set of Terms. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Department Identifier, it is optional. |
| JOB_ID | NUMBER |  | 18 |  | Foreign key to PER_JOBS_F. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign key to HR_LOCATIONS_ALL_F. |
| POSITION_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_POSITIONS_F. |
| GRADE_ID | NUMBER |  | 18 |  | Foreign key to PER_GRADES_F. |
| BARGAINING_UNIT_CODE | VARCHAR2 | 30 |  |  | Bargaining unit code. |
| EMPLOYMENT_CATEGORY | VARCHAR2 | 30 |  |  | User defined category. For example Full-Time Permanent or Part-Time Permanent. Lookup Type = ?EMP_CAT?. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ASSIGNMENT_STATUS_TYPE | VARCHAR2 | 30 |  | Yes | Denormalized status of the assignment. This is derived using the Assignment Status Type ID. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Represents Legal Entity. Might be null for Applicants. |
| LEGISLATION_CODE | VARCHAR2 | 150 |  |  | Legislation code derived from the Legal Entity. Might be null for Applicants. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Determinant for ?Set Enabled? tables and those using BU as a partitioning key. |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
