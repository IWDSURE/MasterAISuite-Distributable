# HTS_LABOR_DEMAND_PRFL_DEFS

labor demand instances defined for a scheduler profile

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemandprfldefs-25108.html#htslabordemandprfldefs-25108](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemandprfldefs-25108.html#htslabordemandprfldefs-25108)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_LABOR_DEMAND_PRFL_DEFS_PK | LBR_DMD_PRFL_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LBR_DMD_PRFL_DEF_ID | NUMBER |  | 18 | Yes | LBR_DMND_PROF_DEF_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| LBR_DMD_PRFL_SET_ID | NUMBER |  | 18 |  | PROFILE_ID |
| TM_PATTERN_ID | NUMBER |  | 18 |  | TM_PATTERN_ID |
| LBR_DEMAND_ID | NUMBER |  | 18 | Yes | LBR_DEMAND_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_LABOR_DEMAND_PRFL_DEFS_N1 | Non Unique | Default | LBR_DMD_PRFL_SET_ID |
| HTS_LABOR_DEMAND_PRFL_DEFS_PK | Unique | Default | LBR_DMD_PRFL_DEF_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
