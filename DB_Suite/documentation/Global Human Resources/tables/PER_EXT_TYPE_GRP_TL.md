# PER_EXT_TYPE_GRP_TL

Translation table for parameters of an extract type.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexttypegrptl-4564.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexttypegrptl-4564.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_TYPE_GRP_TL_PK | EXT_TYPE_GRP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| EXT_TYPE_GRP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EXT_TYPE_GRP_NAME | VARCHAR2 | 80 |  | Yes | Denotes name of the extract type. |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Denotes description for the extract type. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_TYPE_GRP_TL_PK | Unique | FUSION_TS_TX_DATA | EXT_TYPE_GRP_ID, LANGUAGE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
