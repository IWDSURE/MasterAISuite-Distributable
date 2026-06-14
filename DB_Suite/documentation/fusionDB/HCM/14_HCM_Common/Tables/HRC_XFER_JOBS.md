# HRC_XFER_JOBS

The table is used to keep a record on any information for a particular transfer job (but actually can be used by an HRC job)

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcxferjobs-21845.html#hrcxferjobs-21845](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcxferjobs-21845.html#hrcxferjobs-21845)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_XFER_JOBS_PK | XFER_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFER_JOB_ID | NUMBER |  | 18 | Yes | Surrogate Primary Key populated by sequence |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ESS_TYPE | VARCHAR2 | 250 |  | Yes | Foreign Key to the ESS schema which identifies an ESS TYPE (eg: ESS Inbound Job) |
| ESS_DEFINITION | VARCHAR2 | 800 |  | Yes | Foreign Key to the ESS schema which identifies as ESS Definition |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_XFER_JOBS_N1 | Non Unique | Default | ESS_DEFINITION, ENTERPRISE_ID |
| HRC_XFER_JOBS_PK | Unique | Default | XFER_JOB_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
