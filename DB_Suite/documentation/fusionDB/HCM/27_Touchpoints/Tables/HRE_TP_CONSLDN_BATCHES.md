# HRE_TP_CONSLDN_BATCHES

Mapping table of Batch Id and Run Id of the consolidation process.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretpconsldnbatches-26720.html#hretpconsldnbatches-26720](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretpconsldnbatches-26720.html#hretpconsldnbatches-26720)

## Primary Key

| Name | Columns |
|------|----------|
| HRE_TP_CONSLDN_BATCHES_PK | BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | System generated primary key for this table. |
| CONSLDN_RUN_ID | NUMBER |  | 18 |  | Foreign key to hre_tp_consldn_run. |
| ERROR_MESSAGE_DETAIL | CLOB |  |  |  | Error Message details of this batch |
| BATCH_STATUS | VARCHAR2 | 64 |  |  | Batch completion status |
| ESS_CHILD_REQUEST_ID | NUMBER |  | 18 |  | Child ESS Request Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | Identify type of object. In the case of employee and manager,
 store as EMP or MGR or INTERACTIONS |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TP_CONSLDN_BATCHES_FK1 | Non Unique | Default | CONSLDN_RUN_ID |
| HRE_TP_CONSLDN_BATCHES_PK | Unique | Default | BATCH_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
