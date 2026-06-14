# HRC_DL_BUS_OBJ_INCLUSIONS

HRC_DL_BUS_OBJ_INCLUSIONS table is used by data laoder to restrict the business objects available to customers.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusobjinclusions-11796.html#hrcdlbusobjinclusions-11796](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusobjinclusions-11796.html#hrcdlbusobjinclusions-11796)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_OBJ_INCLUSIONS_PK | BUS_OBJ_INCLUSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUS_OBJ_INCLUSION_ID | NUMBER |  | 18 | Yes | BUS_OBJ_INCLUSION_ID |
| DYNAMIC_HIERARCHY | VARCHAR2 | 1 |  |  | DYNAMIC_HIERARCHY |
| HSDL_SECURED | VARCHAR2 | 30 |  |  | HSDL_SECURED |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| HSDL_ENABLED | VARCHAR2 | 30 |  | Yes | HSDL_ENABLED |
| DOWNLOAD_ENABLED | VARCHAR2 | 30 |  | Yes | DOWNLOAD_ENABLED |
| INCLUSION_ENABLED | VARCHAR2 | 20 |  | Yes | INCLUSION_ENABLED |
| ROLLBACK_ENABLED | VARCHAR2 | 1 |  |  | ROLLBACK_ENABLED |
| ORACLE_SEARCH_ENABLED | VARCHAR2 | 1 |  |  | ORACLE_SEARCH_ENABLED |
| POST_PROCESS_ENABLED | VARCHAR2 | 1 |  |  | POST_PROCESS_ENABLED |
| SGUID | VARCHAR2 | 32 |  | Yes | The seed global unique identifier. Oracle internal use only. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BUS_OBJ_INCLUSIONS_PK | Unique | Default | BUS_OBJ_INCLUSION_ID, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJ_INCLUSIONS_PK1 | Unique | Default | BUS_OBJ_INCLUSION_ID, ORA_SEED_SET2 |
| HRC_DL_BUS_OBJ_INCLUSIONS_U1 | Unique | Default | BUSINESS_OBJECT_ID, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJ_INCLUSIONS_U11 | Unique | Default | BUSINESS_OBJECT_ID, ORA_SEED_SET2 |
| HRC_DL_BUS_OBJ_INCLUSIONS_U2 | Unique | Default | SGUID, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJ_INCLUSIONS_U21 | Unique | Default | SGUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
