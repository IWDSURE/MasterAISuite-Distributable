# HRC_DL_BUS_OBJ_USE_EXCLNS

HRC_DL_BUS_OBJ_USE_EXCLNS is seeded to specify excluded objects for a particular client loader to qualify support in Data Loader.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusobjuseexclns-21805.html#hrcdlbusobjuseexclns-21805](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusobjuseexclns-21805.html#hrcdlbusobjuseexclns-21805)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_OBJ_USE_EXCLNS_PK | USE_EXCLUSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USE_EXCLUSION_ID | NUMBER |  | 18 | Yes | USE_EXCLUSION_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| LOADER_USE_EXCLUSION | VARCHAR2 | 30 |  | Yes | LOADER_USE_EXCLUSION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BUS_OBJ_USE_EXCLNS_N20 | Non Unique | Default | SGUID |
| HRC_DL_BUS_OBJ_USE_EXCLNS_PK | Unique | Default | USE_EXCLUSION_ID, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJ_USE_EXCLNS_PK1 | Unique | Default | USE_EXCLUSION_ID, ORA_SEED_SET2 |
| HRC_DL_BUS_OBJ_USE_EXCLNS_U1 | Unique | Default | BUSINESS_OBJECT_ID, LOADER_USE_EXCLUSION, ORA_SEED_SET1 |
| HRC_DL_BUS_OBJ_USE_EXCLNS_U11 | Unique | Default | BUSINESS_OBJECT_ID, LOADER_USE_EXCLUSION, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
