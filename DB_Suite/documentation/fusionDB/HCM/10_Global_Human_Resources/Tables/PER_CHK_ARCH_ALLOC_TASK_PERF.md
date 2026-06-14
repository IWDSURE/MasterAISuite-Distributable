# PER_CHK_ARCH_ALLOC_TASK_PERF

This table records performer details for an allocated task.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloctaskperf-25061.html#perchkarchalloctaskperf-25061](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloctaskperf-25061.html#perchkarchalloctaskperf-25061)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ARCH_TASK_PERF_PK | TASK_PERFORMER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_PERFORMER_ID | NUMBER |  | 18 | Yes | TASK_PERFORMER_ID |
| ALLOCATED_TASK_ID | NUMBER |  | 18 | Yes | ALLOCATED_TASK_ID |
| PERFORMER_TYPE | VARCHAR2 | 30 |  | Yes | PERFORMER_TYPE |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| USER_GUID | VARCHAR2 | 64 |  |  | USER_GUID |
| USERNAME | VARCHAR2 | 100 |  |  | USERNAME |
| ACTIVE_FLAG | VARCHAR2 | 4 |  | Yes | ACTIVE_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PARTY_ID | NUMBER |  | 18 |  | PARTY_ID |
| SUPPLIER_SITE_ID | NUMBER |  | 18 |  | SUPPLIER_SITE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_ARCH_TASK_PERF_PK | Unique | Default | TASK_PERFORMER_ID |
| PER_CHK_ARCH_TASK_PERF_N1 | Non Unique | Default | ALLOCATED_TASK_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
