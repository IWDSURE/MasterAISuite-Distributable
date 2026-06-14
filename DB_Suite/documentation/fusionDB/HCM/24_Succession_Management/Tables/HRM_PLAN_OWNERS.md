# HRM_PLAN_OWNERS

The owners table provides information about the plan owners.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanowners-8323.html#hrmplanowners-8323](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanowners-8323.html#hrmplanowners-8323)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_PLAN_OWNERS_PK | ENTERPRISE_ID, PLAN_OWNER_ID, DATE_FROM |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| ENABLE_ALERT | VARCHAR2 | 30 |  |  | Enable Alert determines whether alert/notification has to be sent to the particular owner or not. |
| PLAN_OWNER_ID | NUMBER |  | 18 | Yes | Plan owner id uniquely identifies the owner in the plan. |
| PLAN_ID | NUMBER |  | 18 | Yes | Plan id indicated the plan in which current owner belongs to. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person id represents the person id of the plan owner. |
| OWNER_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Owner Type Code determines whether user has Administrator or Viewer or Candidate Manager access. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LATEST_RECORD_FLAG | VARCHAR2 | 1 |  | Yes | Latest record flag indicates the latest-active snapshot. |
| OPERATION_TYPE | VARCHAR2 | 210 |  |  | Operation type represents the type of operation committed. |
| SOURCE_CODE | VARCHAR2 | 30 |  |  | Source code represents the source from were row is created or updated. |
| DATE_FROM | DATE |  |  | Yes | Date from represent the date from which current snapshot has created. |
| DATE_TO | DATE |  |  |  | Date to represents end date for the current snapshot. |
| SOURCE_KEY | VARCHAR2 | 200 |  |  | Source Key represents the object_id of source from where row is created or updated. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_PLAN_OWNERS_FK1 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, PLAN_ID |
| HRM_PLAN_OWNERS_PK | Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, PLAN_OWNER_ID, DATE_FROM |
| HRM_PLAN_OWNERS_UK1 | Unique | Default | PERSON_ID, PLAN_ID, ENTERPRISE_ID, DATE_FROM |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
