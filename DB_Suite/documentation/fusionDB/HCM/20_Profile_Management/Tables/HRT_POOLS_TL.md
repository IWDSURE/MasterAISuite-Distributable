# HRT_POOLS_TL

Translatable table for HRT_POOLS_B

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolstl-4986.html#hrtpoolstl-4986](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpoolstl-4986.html#hrtpoolstl-4986)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_POOLS_TL_PK | ENTERPRISE_ID, POOL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| POOL_ID | NUMBER |  | 18 | Yes | System generated primary key | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| POOL_NAME | VARCHAR2 | 240 |  | Yes | Talent Pool Name | Active |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The description of the talent pool |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_POOLS_TL_N1 | Non Unique | Default | POOL_NAME |
| HRT_POOLS_TL_N2 | Non Unique | Default | DESCRIPTION |
| HRT_POOLS_TL_PK | Unique | Default | ENTERPRISE_ID, POOL_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
