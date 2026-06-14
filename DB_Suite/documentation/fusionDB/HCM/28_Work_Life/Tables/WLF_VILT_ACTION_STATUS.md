# WLF_VILT_ACTION_STATUS

Table to store status and errors of virtual ILT actions such as create meeting, update meeting, etc

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfviltactionstatus-17613.html#wlfviltactionstatus-17613](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfviltactionstatus-17613.html#wlfviltactionstatus-17613)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_VILT_ACTION_STATUS_PK | VILT_ACTION_STATUS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VILT_ACTION_STATUS_ID | NUMBER |  | 18 | Yes | Vilt action status PK |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | Learning Item Id in which the VILT action was performed on |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source type of the source id column |
| SOURCE_ID | NUMBER |  | 18 |  | Source id |
| ACTION_TYPE | VARCHAR2 | 30 |  |  | The type of vilt action (create, update, delete etc.) |
| STATUS | VARCHAR2 | 30 |  |  | Status of the vilt action, error, success, etc. |
| LOG | VARCHAR2 | 4000 |  |  | Log for the vilt action |
| ACTION_TIMESTAMP | TIMESTAMP |  |  |  | Timestamp of the vilt action |
| ERROR_CODE | VARCHAR2 | 100 |  |  | Error code of vilt action |
| INSTR_VILT_REL_ID | NUMBER |  | 18 |  | The instructor account used for VILT api call |
| RESOLUTION_STATUS | VARCHAR2 | 30 |  |  | Column to indicate what action the user has taken for this log entry |
| MAX_RETRIES | NUMBER |  | 18 |  | Max number of retries |
| NOTES | VARCHAR2 | 1000 |  |  | Notes |
| ERROR_LOG | CLOB |  |  |  | Contains error information about the failed call to VILT provider |
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
| WLF_VILT_ACTION_STATUS_N1 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| WLF_VILT_ACTION_STATUS_N2 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_VILT_ACTION_STATUS_N3 | Non Unique | Default | STATUS |
| WLF_VILT_ACTION_STATUS_U1 | Unique | Default | VILT_ACTION_STATUS_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
