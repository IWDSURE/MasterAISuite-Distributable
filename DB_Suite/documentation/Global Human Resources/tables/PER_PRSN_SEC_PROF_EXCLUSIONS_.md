# PER_PRSN_SEC_PROF_EXCLUSIONS_

PER_PERSON_SEC_PROF_EXCLUSIONS to store exclusion relates security preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprsnsecprofexclusions-11930.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprsnsecprofexclusions-11930.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERSON_SEC_PROF_EXCL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_SEC_PROF_EXCL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_SEC_PROF_EXCL_ID | NUMBER |  | 18 | Yes | PERSON_SEC_PROF_EXCL_ID |
| PERSON_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSON_SECURITY_PROFILES table. |
| EXCLUSION_RULE_ID | NUMBER |  | 18 |  | Foreign Key to PER_EXCLUSION_RULES table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERSON_SEC_PROF_EXCLN1_ | Non Unique | Default | PERSON_SEC_PROF_EXCL_ID, LAST_UPDATE_DATE |
| PER_PRSN_SEC_PROF_EXCL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_SEC_PROF_EXCL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
