# HWM_TM_REC_GRP_OFFLINE

A new table to manage time cards that have been submitted for offline processing.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrpoffline-26851.html#hwmtmrecgrpoffline-26851](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrpoffline-26851.html#hwmtmrecgrpoffline-26851)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_GRP_OFFLINE_PK | TM_REC_GRP_OFFLINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_GRP_OFFLINE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| STATUS_ID | NUMBER |  | 18 | Yes | STATUS_ID |
| RESOURCE_ID | NUMBER |  | 18 | Yes | The resource for which the time building block applies. |
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | this it the unique id that represents the timecard which need to process |
| TM_REC_GRP_VERSION | NUMBER |  | 9 | Yes | this column containing the current version of the time building block. |
| PROCESS_STATUS | NUMBER |  | 2 | Yes | this column represents the status of the timecard that need to process offline. |
| OFFLINE_SUBMIT_TIME | TIMESTAMP |  |  | Yes | this colun represents the submission time of offline timecard |
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
| HWM_TM_REC_GRP_OFFLINE_N1 | Non Unique | Default | RESOURCE_ID, PROCESS_STATUS |
| HWM_TM_REC_GRP_OFFLINE_N2 | Non Unique | Default | TM_REC_GRP_ID, PROCESS_STATUS |
| HWM_TM_REC_GRP_OFFLINE_U1 | Unique | Default | TM_REC_GRP_OFFLINE_ID, TM_REC_GRP_ID, TM_REC_GRP_VERSION |
| HWM_TM_REC_GRP_OFFLINE_U2 | Unique | Default | TM_REC_GRP_OFFLINE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
