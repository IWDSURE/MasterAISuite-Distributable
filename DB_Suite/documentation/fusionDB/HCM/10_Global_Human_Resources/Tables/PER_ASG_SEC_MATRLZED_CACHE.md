# PER_ASG_SEC_MATRLZED_CACHE

This table will hold materialized cache data for list of assignments a user has access to.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgsecmatrlzedcache-8665.html#perasgsecmatrlzedcache-8665](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perasgsecmatrlzedcache-8665.html#perasgsecmatrlzedcache-8665)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASG_SEC_MATRLZED_CACH_PK | ASSIGNMENT_ID, LAST_REFRESH_DATE, PRIVILEGE, USER_GUID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_GUID | VARCHAR2 | 64 |  | Yes | This field represents user guid or user session for which data is being cached. |
| PRIVILEGE | VARCHAR2 | 512 |  | Yes | This field represents user's privilege based on which data is being cached in this table. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | This field represents an internal ID for the assignment to which user has access to. |
| LAST_REFRESH_DATE | TIMESTAMP |  |  | Yes | This field represents last time when cache was refreshed. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ASG_SEC_MATRLZED_CACHE_U1 | Unique | Default | ASSIGNMENT_ID, LAST_REFRESH_DATE, PRIVILEGE, USER_GUID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
