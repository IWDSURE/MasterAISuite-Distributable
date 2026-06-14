# HRM_PLAN_TALENTPOOLS

The plan pool association table is no longer available for use. The table is obsolete.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplantalentpools-18715.html#hrmplantalentpools-18715](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplantalentpools-18715.html#hrmplantalentpools-18715)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_PLAN_TALENTPOOLS_PK | ENTERPRISE_ID, PLAN_POOL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | enterprise id represents enterprise id for hrm plan talentpools. |
| PLAN_POOL_ID | NUMBER |  | 18 | Yes | Plan pool id represents the id of pool for plan. |
| PLAN_ID | NUMBER |  | 18 |  | Plan id represents the id of the plans. |
| POOL_ID | NUMBER |  | 18 |  | Pool id represents the id of pool to identify it. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRM_PLAN_TALENTPOOLS_FK1 | Non Unique | Default | ENTERPRISE_ID, PLAN_ID | Obsolete |
| HRM_PLAN_TALENTPOOLS_PK | Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, PLAN_POOL_ID |  |
| HRM_PLAN_TALENTPOOLS_UK1 | Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, PLAN_ID, POOL_ID |  |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
