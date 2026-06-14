# HRT_PROFILE_EXTRA_INFO_B

To store the extra attributes of a profile we are creating a new table HRT_PROFILE_EXTRA_INFO_B.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileextrainfob-11474.html#hrtprofileextrainfob-11474](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileextrainfob-11474.html#hrtprofileextrainfob-11474)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_EXTRA_INFO_B_PK | PROFILE_EXTRA_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_EXTRA_INFO_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILES_B |
| JOB_LEVEL_CODE | VARCHAR2 | 30 |  |  | Identifier of job |
| RISK_CODE | VARCHAR2 | 30 |  |  | Job risk or position risk |
| CRITICALITY_REASON | VARCHAR2 | 30 |  |  | Comments on criticality of specific job |
| SUCCESSION_PLAN_REQUIRED | VARCHAR2 | 30 |  |  | Job required succession plan or not |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_EXTRA_INFO_B_U1 | Unique | Default | PROFILE_EXTRA_INFO_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
