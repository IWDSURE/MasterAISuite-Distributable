# WLF_LEARN_PROCESSING_DETAILS

Table to store relation information of learning item to learning organization.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnprocessingdetails-22114.html#wlflearnprocessingdetails-22114](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnprocessingdetails-22114.html#wlflearnprocessingdetails-22114)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_PROCESSING_DTL_PK | PROCESSING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESSING_ID | NUMBER |  |  | Yes | System generated unique identifier. |
| LEARN_OBJECT_ID | NUMBER |  |  | Yes | Reference to the learning object id |
| LEARN_OBJECT_TYPE | VARCHAR2 | 32 |  |  | Reference to learn object type |
| IS_RECONCILE_READY | VARCHAR2 | 1 |  |  | Indicator to provide hint whether learn object is ready to  be reconciled. |
| LATEST_PROCESSED_DATE | TIMESTAMP |  |  |  | The date when learn object is last reconciled. |
| LATEST_PROCESSING_STATUS | VARCHAR2 | 32 |  |  | The status of last reconciliation |
| LATEST_JOB_ID | NUMBER |  |  |  | The latest job id that processed the learn object |
| LAST_SUCC_PROCESSED_DATE | TIMESTAMP |  |  |  | The date when learn object is last reconciled successfully. |
| LAST_SUCC_JOB_ID | NUMBER |  |  |  | The job id of last successful reconcile of learning object |
| JOB_NAME | VARCHAR2 | 32 |  |  | JOB_NAME |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_PROC_DETAILS_N1 | Non Unique | WLF_LEARN_PROC_DETAILS_N1 | LEARN_OBJECT_ID |
| WLF_LEARN_PROC_DETAILS_U1 | Unique | WLF_LEARN_PROC_DETAILS_U1 | PROCESSING_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
