# PER_DATA_SEC_COMPUTE_ACL

Temp table for compute user acl.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdataseccomputeacl-30863.html#perdataseccomputeacl-30863](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdataseccomputeacl-30863.html#perdataseccomputeacl-30863)

## Primary Key

| Name | Columns |
|------|----------|
| per_data_sec_compute_acl_PK | JOB_NUMBER, CHILD_SEQ |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_NAME | VARCHAR2 | 64 |  |  | ESS job name. |
| JOB_NUMBER | NUMBER |  | 18 | Yes | ESS job number. |
| CHILD_SEQ | NUMBER |  | 18 | Yes | Child ESS sequence. |
| USER_SET | CLOB |  |  |  | Set of users. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| per_data_sec_compute_acl_U1 | Unique | Default | JOB_NUMBER, CHILD_SEQ |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
