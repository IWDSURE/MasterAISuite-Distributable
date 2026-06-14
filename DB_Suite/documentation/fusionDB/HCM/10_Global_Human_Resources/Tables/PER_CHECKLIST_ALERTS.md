# PER_CHECKLIST_ALERTS

Table to store checklist and task alerts

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistalerts-24739.html#perchecklistalerts-24739](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistalerts-24739.html#perchecklistalerts-24739)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_ALERTS_PK | CHK_ALERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHK_ALERT_ID | NUMBER |  | 18 | Yes | CHK_ALERT_ID |
| ALERT_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | ALERT_OBJECT_TYPE |
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 |  | ALLOCATED_CHECKLIST_ID |
| ALLOCATED_TASK_ID | NUMBER |  | 18 |  | ALLOCATED_TASK_ID |
| ALERT_TYPE | VARCHAR2 | 64 |  | Yes | ALERT_TYPE |
| PROCESSING_STATUS | VARCHAR2 | 30 |  | Yes | PROCESSING_STATUS |
| PROCESSED_DATE | TIMESTAMP |  |  |  | PROCESSED_DATE |
| CHK_ALERT_SET_ID | NUMBER |  | 18 |  | CHK_ALERT_SET_ID |
| CHK_ALERT_CHUNK_ID | NUMBER |  | 18 |  | CHK_ALERT_CHUNK_ID |
| ERROR_DETAILS | VARCHAR2 | 4000 |  |  | ERROR_DETAILS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_ALERTS_PK | Unique | Default | CHK_ALERT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
