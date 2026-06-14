# BEN_COMP_OBJ_CACHE

BEN_COMP_OBJECT_CACHE holds the compensation objects cache for a run of the manage life events process.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencompobjcache-17646.html#bencompobjcache-17646](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencompobjcache-17646.html#bencompobjcache-17646)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_COMP_OBJ_CACHE_PK | COMP_OBJ_CACHE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMP_OBJ_CACHE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal entity assigned to the compensation object. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CACHE_TIMESTAMP | DATE |  |  | Yes | Cache Timestamp. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODE_CD | VARCHAR2 | 30 |  |  | Mode |
| NO_PLANS | VARCHAR2 | 30 |  |  | No Plans |
| NO_PROGRAMS | VARCHAR2 | 30 |  |  | No Programs |
| PGM_ID | NUMBER |  |  |  | Foreign Key to BEN_PGM_F |
| PL_ID | NUMBER |  |  |  | Foreign Key to BEN_PL_F |
| PL_TYP_ID | NUMBER |  |  |  | Foreign Key to BEN_PL_TYP_F |
| EFFECTIVE_DATE | DATE |  |  | Yes | Effective date. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_COMP_OBJ_CACHE_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |
| BEN_COMP_OBJ_CACHE_FK2 | Non Unique | Default | LEGAL_ENTITY_ID |
| BEN_COMP_OBJ_CACHE_PK | Unique | Default | COMP_OBJ_CACHE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
