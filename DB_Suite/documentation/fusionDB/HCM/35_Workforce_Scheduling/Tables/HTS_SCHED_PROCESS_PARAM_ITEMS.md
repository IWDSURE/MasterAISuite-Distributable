# HTS_SCHED_PROCESS_PARAM_ITEMS

Schedule batch processes requests functional parameters: element of a sub-process group

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprocessparamitems-25120.html#htsschedprocessparamitems-25120](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedprocessparamitems-25120.html#htsschedprocessparamitems-25120)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_ROCESS_PARAM_IT_PK | PROCESS_PARAM_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_PARAM_ITEM_ID | NUMBER |  | 18 | Yes | SYSTEM GENERATED UNIQUE IDENTIFIER OF THE ROW |
| GROUP_ID | NUMBER |  | 18 | Yes | Reference to the system generated ID identifying a sub-process functional partition group in hts_sched_process_params table |
| GROUP_ITEM | NUMBER |  | 18 |  | An item of the sub-process functional parameters group |
| GROUP_ITEM2 | NUMBER |  | 18 |  | Discriminating property of an item of the sub-process functional parameters group (such as assignment for person) |
| STATUS | NUMBER |  | 2 |  | Status of the execution of the sub-process for the current item of the sub-process group |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_PRCS_PRM_ITEMS_N1 | Non Unique | FUSION_TS_TX_IDX | GROUP_ID, GROUP_ITEM |
| HTS_SCHED_PRCS_PRM_ITEMS_U1 | Unique | Default | PROCESS_PARAM_ITEM_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
