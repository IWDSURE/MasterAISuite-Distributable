# PER_PRSN_SEC_MATRLZED_CACHE

This table will hold materialized cache data for list of persons a user has access to.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprsnsecmatrlzedcache-23920.html#perprsnsecmatrlzedcache-23920](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprsnsecmatrlzedcache-23920.html#perprsnsecmatrlzedcache-23920)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PRSN_SEC_MATRLZED_CAC_PK | PERSON_ID, LAST_REFRESH_DATE, PRIVILEGE, USER_GUID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_GUID | VARCHAR2 | 64 |  | Yes | This field represents user guid or user session for which data is being cached. |
| PRIVILEGE | VARCHAR2 | 512 |  | Yes | This field represents user's privilege based on which data is being cached in this table. |
| PERSON_ID | NUMBER |  | 18 | Yes | This field represents an internal ID for the person to which user has access to. |
| LAST_REFRESH_DATE | TIMESTAMP |  |  | Yes | This field represents an internal ID for the assignment to which user has access to. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PRSN_SEC_MATRLZED_CACHE_U1 | Unique | Default | PERSON_ID, LAST_REFRESH_DATE, PRIVILEGE, USER_GUID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
