# HRM_POOL_SEC_PROF_JOB_FAMILIE_

Table to store job families added in a talent pool security profile.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpoolsecprofjobfamilie-22837.html#hrmpoolsecprofjobfamilie-22837](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpoolsecprofjobfamilie-22837.html#hrmpoolsecprofjobfamilie-22837)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_POOL_SEC_PROF_JOB_FMLY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, POOL_SEC_PROF_JOB_FAMILY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| POOL_SEC_PROF_JOB_FAMILY_ID | NUMBER |  | 18 | Yes | Uniquely identifies the job family added to talent pool security profile. | Active |
| POOL_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Forigen key column for hrm_pool_security_profiles table. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. | Active |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Selected Job Family id in talent pool security profile. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRM_POOL_SEC_PROF_JOB_FMLY_PK_ | Unique | HRM_POOL_SEC_PROF_JOB_FMLY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, POOL_SEC_PROF_JOB_FAMILY_ID | Active |
| HRM_POOL_SEC_PROF_JOB_FMLY_U1_ | Unique | HRM_POOL_SEC_PROF_JOB_FMLY_N1_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, POOL_SECURITY_PROFILE_ID, JOB_FAMILY_ID | Active |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
