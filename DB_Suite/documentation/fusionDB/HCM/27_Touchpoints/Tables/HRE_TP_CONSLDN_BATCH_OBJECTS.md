# HRE_TP_CONSLDN_BATCH_OBJECTS

Mapping table of Object Id and Batch Id of the consolidation process.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretpconsldnbatchobjects-18784.html#hretpconsldnbatchobjects-18784](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretpconsldnbatchobjects-18784.html#hretpconsldnbatchobjects-18784)

## Primary Key

| Name | Columns |
|------|----------|
| HRE_TP_CONSLDN_BTCH_OBJ_PK | OBJECT_ID, BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_ID | NUMBER |  | 18 | Yes | Primary key. Object Id stores id of object on which consolidation is performed. |
| BATCH_ID | NUMBER |  | 18 | Yes | Foreign key to batch_Id from hre_tp_consldn_batches |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | Identify type of object. In the case of employee and manager,
 store as EMP or MGR or INTERACTIONS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TP_CONSLDN_BTCH_OBJ_FK1 | Non Unique | Default | BATCH_ID |
| HRE_TP_CONSLDN_BTCH_OBJ_PK | Unique | Default | OBJECT_ID, BATCH_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
