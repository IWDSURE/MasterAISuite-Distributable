# HWM_TCD_EXP_DATA_ESS_PROCESS

TCD EXPORT DATA ESS PROCESS TABLE

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataessprocess-17793.html#hwmtcdexpdataessprocess-17793](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataessprocess-17793.html#hwmtcdexpdataessprocess-17793)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_ESS_PROC_PK | TCD_EXP_DATA_ESS_PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCD_EXP_DATA_ESS_PROCESS_ID | NUMBER |  | 18 | Yes | The time device export data process id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| ESS_REQUEST_ID | NUMBER |  | 18 | Yes | Process request Id from the ESS |
| PROCESS_BEGIN_TIME | TIMESTAMP |  |  | Yes | The process begin date and time |
| PROCESS_END_TIME | TIMESTAMP |  |  |  | The process end date and time |
| STATUS | VARCHAR2 | 20 |  |  | Status of the time device export data process |
| SUB_STATUS | VARCHAR2 | 20 |  |  | Status of the phases in the time device export data process |
| ERROR_TEXT | VARCHAR2 | 4000 |  |  | The error message to indicate what went wrong while running the process |
| SETUP_PROFILE_ID | NUMBER |  | 18 |  | The setup profile id driving the export data collection. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCD_EXP_DATA_ESS_PRO_U1 | Unique | Default | TCD_EXP_DATA_ESS_PROCESS_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
