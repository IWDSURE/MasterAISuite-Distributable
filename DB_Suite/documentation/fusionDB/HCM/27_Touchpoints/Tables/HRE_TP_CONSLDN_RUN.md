# HRE_TP_CONSLDN_RUN

Base table which has the parent ess request id of the touchpoint consolidation process.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretpconsldnrun-23150.html#hretpconsldnrun-23150](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretpconsldnrun-23150.html#hretpconsldnrun-23150)

## Primary Key

| Name | Columns |
|------|----------|
| HRE_TP_CONSLDN_RUN_PK | CONSLDN_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONSLDN_RUN_ID | NUMBER |  | 18 | Yes | System generated primary key for this table. |
| ESS_PARENT_REQUEST_ID | NUMBER |  | 18 |  | Parent ESS Request Id. |
| LAST_RUN_DATE | TIMESTAMP |  |  |  | The timestamp of last run of this job |
| COMPLETION_STATUS | VARCHAR2 | 64 |  |  | The completion status of the job |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TP_CONSLDN_RUN_PK | Unique | Default | CONSLDN_RUN_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
