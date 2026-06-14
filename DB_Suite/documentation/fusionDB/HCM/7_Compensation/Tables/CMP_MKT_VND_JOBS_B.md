# CMP_MKT_VND_JOBS_B

Table contains Compensation Vendor Jobs

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndjobsb-9612.html#cmpmktvndjobsb-9612](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndjobsb-9612.html#cmpmktvndjobsb-9612)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_VND_JOBS_PK | JOB_LIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_LIST_ID | NUMBER |  | 18 | Yes | Job List Id |
| VENDOR_ID | NUMBER |  | 18 | Yes | Vendor Id |
| VENDOR_JOB_CODE | VARCHAR2 | 30 |  | Yes | Vendor Job Code |
| JOB_FUNCTION_ID | NUMBER |  | 18 |  | Job Function Id |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Job Family Id |
| CAREER_STREAM_ID | NUMBER |  | 18 |  | Carer Stream Id |
| CAREER_LEVEL_ID | NUMBER |  | 18 |  | Career Level Id |
| OTHER_LEVEL_ID | NUMBER |  | 18 |  | Other Level Id |
| VENDOR_JOB_MAPPING_CODE | VARCHAR2 | 30 |  |  | Indicates if the composite is mapped to internal HR Job or Position. |
| JOB_ID | NUMBER |  | 18 |  | HR Job Id |
| POSITION_ID | NUMBER |  | 18 |  | HR Position Id |
| STATUS | VARCHAR2 | 30 |  | Yes | Vendor Status |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| JOB_MATCH_PERCENT | NUMBER |  |  |  | Job Matching Percent |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_VND_JOBS_B_U1 | Unique | Default | JOB_LIST_ID |
| CMP_MKT_VND_JOBS_B_U2 | Unique | Default | JOB_LIST_ID, VENDOR_ID, VENDOR_JOB_CODE |
| CMP_MKT_VND_JOBS_B_U3 | Unique | Default | VENDOR_ID, VENDOR_JOB_CODE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
