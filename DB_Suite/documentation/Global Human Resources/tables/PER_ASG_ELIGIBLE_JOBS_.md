# PER_ASG_ELIGIBLE_JOBS_

This table stores all the information about the eligible jobs that a worker has been authorized to work under. This is not a date effective table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgeligiblejobs-7544.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgeligiblejobs-7544.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASG_ELIGIBLE_JOBS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASG_ELG_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASG_ELG_JOB_ID | NUMBER |  | 18 | Yes | This is a system generated primary key for this table |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | This is a foreign key to PER_ALL_ASSIGNMENTS_M table. |
| PERSON_ID | NUMBER |  | 18 |  | This is a Foreign key to PER_PERSONS table. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| JOB_ID | NUMBER |  | 18 |  | This is a foreign key to PER_JOBS_F. |
| FROM_DATE | DATE |  |  |  | Start date of the authorized eligible job. |
| TO_DATE | DATE |  |  |  | End date of the authorized eligible job. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ASG_ELIG_OBJ_ID | NUMBER |  | 18 |  | This is a duplicate id which will be used as the object id for the transaction approval purpose. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OVERRIDE_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate whether the Derived Rate will be overridden |
| RATE | NUMBER |  | 30 |  | Overridden rate of the elligible job. |
| FREQUENCY | VARCHAR2 | 40 |  |  | Frequency if rate is overridden. |
| CURRENCY | VARCHAR2 | 30 |  |  | Currency if rate is overridden. |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | This is the Primary Key for the Job Family Table PER_JOB_FAMILY_F |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Determinant for Set Enabled tables and those using BU as a partitioning key. |
| RATE_DEFINITION_ID | NUMBER |  | 18 |  | This is the Primary Key for the Rate Definitions table PAY_RATE_DEFINITIONS_F. |
| ATTR1_VALUE | VARCHAR2 | 2000 |  |  | This column has been added for future use purpose. |
| ATTR2_VALUE | VARCHAR2 | 2000 |  |  | This column has been added for future use purpose. |
| ATTR_NUMBER1 | NUMBER |  |  |  | This column has been added for future use purpose. |
| ATTR_NUMBER2 | NUMBER |  |  |  | This column has been added for future use purpose. |
| ATTR_DATE1 | DATE |  |  |  | This column has been added for future use purpose. |
| ATTR_DATE2 | DATE |  |  |  | This column has been added for future use purpose. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAEJN1_ | Non Unique | Default | ASG_ELG_JOB_ID, LAST_UPDATE_DATE |
| PER_ASG_ELIGIBLE_JOBS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASG_ELG_JOB_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
