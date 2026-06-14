# PER_JOB_SEC_PROFILE_JOBS

Job Security Profile Jobs Table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobsecprofilejobs-25695.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobsecprofilejobs-25695.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_SEC_PROFILE_JOBS_PK | JOB_SEC_PROFILE_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_SEC_PROFILE_JOB_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| JOB_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_JOB_SECURITY_PROFILES table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| INCLUDE_EXCLUDE_FLAG | VARCHAR2 | 1 |  | Yes | Job security profiles are not in use - leave blank |
| JOB_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_JOBS_F table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_JOB_SEC_PROFILE_JOBS_FK1 | Non Unique | FUSION_TS_TX_DATA | JOB_SECURITY_PROFILE_ID |
| PER_JOB_SEC_PROFILE_JOBS_PK | Unique | Default | JOB_SEC_PROFILE_JOB_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
