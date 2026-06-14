# WLF_LRN_APPROVAL_TASK_HISTORY

Table to store approval task history.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflrnapprovaltaskhistory-25317.html#wlflrnapprovaltaskhistory-25317](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflrnapprovaltaskhistory-25317.html#wlflrnapprovaltaskhistory-25317)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LRN_APPR_TASK_HISTORY_PK | APPROVAL_TASK_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APPROVAL_TASK_HISTORY_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARN_OBJECT_TYPE | VARCHAR2 | 30 |  |  | Indicates which Learn Object the approval process is related to. |
| LEARN_OBJECT_ID | NUMBER |  | 18 | Yes | Learn Object identifier. |
| APPROVAL_TYPE | VARCHAR2 | 30 |  |  | Indicates which Approval Process the task is referring to. |
| BPM_TASK_ID | VARCHAR2 | 64 |  | Yes | BPM Task Identifier. |
| BPM_TASK_GENERATION_TIME | TIMESTAMP |  |  |  | The time when the BPM task is generated. |
| BPM_TASK_STATUS | VARCHAR2 | 30 |  |  | Indicates if the BPM Task is in In Progress, Approved or Rejected status. |
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
| WLF_LRN_APPR_TASK_HISTORY_U1 | Unique | Default | APPROVAL_TASK_HISTORY_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
