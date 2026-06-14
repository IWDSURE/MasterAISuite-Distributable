# FAI_SAM_RAW_LOAD

This table stores raw data of type payroll flow, ess and hdl

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawload-20275.html#faisamrawload-20275](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamrawload-20275.html#faisamrawload-20275)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SAM_RAW_LOAD_PK | RAW_LOAD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RAW_LOAD_ID | NUMBER |  | 18 | Yes | Primary Key to uniquely identify record in raw load table |
| STATUS | VARCHAR2 | 240 |  |  | Active or Inactive status of the process data |
| NAME | VARCHAR2 | 240 |  |  | Name of the process as specified during process submission |
| TYPE | VARCHAR2 | 240 |  |  | Type of the process like ess payroll hdl |
| PARAMETER | CLOB |  |  |  | Parameter of the load used during process submission |
| SEQUENCE_ID | NUMBER |  | 18 |  | Foreign Key to fai_sam_sequence table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SAM_RAW_LOAD_PK | Unique | Default | RAW_LOAD_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
