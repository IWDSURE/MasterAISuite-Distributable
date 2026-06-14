# HTS_LABOR_DEMAND_DEFS

Table containing the types of labor demand , determined by their unit and time step. Labor demand is a criteria for schedules quality objectives.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemanddefs-16159.html#htslabordemanddefs-16159](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemanddefs-16159.html#htslabordemanddefs-16159)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_LABOR_DEMAND_DEFS_PK | DEMAND_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| DEMAND_ID | NUMBER |  | 18 | Yes | DEMAND_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| DEMAND_CD | VARCHAR2 | 80 |  |  | For seed data |  |
| UNIT | VARCHAR2 | 20 |  | Yes | UNIT |  |
| TIME_STEP | VARCHAR2 | 80 |  | Yes | TIME_STEP using the alternate key of seed data in hwm_rp_tm_periods |  |
| ACTIVITY_ID | NUMBER |  | 18 |  | ACTIVITY_ID |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_LABOR_DEMAND_DEFS_U1 | Unique | Default | DEMAND_ID |
| HTS_LABOR_DEMAND_DEFS_U2 | Unique | Default | DEMAND_CD |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
