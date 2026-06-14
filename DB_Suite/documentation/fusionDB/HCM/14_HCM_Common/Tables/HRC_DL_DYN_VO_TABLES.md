# HRC_DL_DYN_VO_TABLES

This table is used by data loader to facilitate dynamic BOs

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldynvotables-20849.html#hrcdldynvotables-20849](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldynvotables-20849.html#hrcdldynvotables-20849)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_DYN_VO_TABLES_PK | DYN_TABLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DYN_TABLE_ID | NUMBER |  |  | Yes | DYN_TABLE_ID |
| DYN_BUS_OBJ_ID | NUMBER |  |  | Yes | DYN_BUS_OBJ_ID |
| TABLE_NAME | VARCHAR2 | 30 |  | Yes | TABLE_NAME |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ENABLED | VARCHAR2 | 30 |  |  | ENABLED |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_DYN_VO_TABLES_N20 | Non Unique | Default | SGUID, ORA_SEED_SET1 |
| HRC_DL_DYN_VO_TABLES_N21 | Non Unique | Default | SGUID, ORA_SEED_SET2 |
| HRC_DL_DYN_VO_TABLES_PK | Unique | Default | DYN_TABLE_ID, ORA_SEED_SET1 |
| HRC_DL_DYN_VO_TABLES_PK1 | Unique | Default | DYN_TABLE_ID, ORA_SEED_SET2 |
| HRC_DL_DYN_VO_TABLES_U1 | Unique | Default | DYN_BUS_OBJ_ID, TABLE_NAME, ORA_SEED_SET1 |
| HRC_DL_DYN_VO_TABLES_U11 | Unique | Default | DYN_BUS_OBJ_ID, TABLE_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
