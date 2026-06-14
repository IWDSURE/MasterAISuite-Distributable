# HTS_LABOR_DEMAND_PRFL_DEFSETS

Set of demand profile definitions, for a given scheduler profile

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemandprfldefsets-16039.html#htslabordemandprfldefsets-16039](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemandprfldefsets-16039.html#htslabordemandprfldefsets-16039)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_LABOR_DEMAND_PRFL_SET_PK | LBR_DMD_PRFL_SET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LBR_DMD_PRFL_SET_ID | NUMBER |  | 18 | Yes | LBR_DMD_PRFL_SET_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| SCHED_PROFILE_ID | NUMBER |  | 18 | Yes | SCHED_PROFILE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| START_DATE | DATE |  |  |  | validity date range start for the set of values related to this object |
| END_DATE | DATE |  |  |  | end of validity date range for the set of values related to this object |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_LABOR_DEMAND_PRFL_SETS_PK | Unique | Default | LBR_DMD_PRFL_SET_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
