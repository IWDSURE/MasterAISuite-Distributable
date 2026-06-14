# CMP_ESS_TASK_INFO

This object for defining ess process statistic information

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpesstaskinfo-22756.html#cmpesstaskinfo-22756](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpesstaskinfo-22756.html#cmpesstaskinfo-22756)

## Primary Key

| Name | Columns |
|------|----------|
| cmp_ess_task_info_PK | ESS_TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ESS_TASK_ID | NUMBER |  | 18 | Yes | BATCH_PROC_ID |
| TASK_ID | NUMBER |  | 18 |  | TASK_ID |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| MODE_CODE | VARCHAR2 | 30 |  |  | MODE_CODE |
| AUDIT_LOG_FLAG | VARCHAR2 | 1 |  |  | AUDIT_LOG_FLAG |
| VALIDATE_FLAG | VARCHAR2 | 1 |  |  | VALIDATE_FLAG |
| INFORMATION1 | NUMBER |  | 18 |  | INFORMATION1 |
| INFORMATION2 | NUMBER |  | 18 |  | INFORMATION2 |
| INFORMATION3 | NUMBER |  | 18 |  | INFORMATION3 |
| INFORMATION4 | NUMBER |  | 18 |  | INFORMATION4 |
| INFORMATION5 | NUMBER |  | 18 |  | INFORMATION5 |
| INFORMATION6 | NUMBER |  | 18 |  | INFORMATION6 |
| INFORMATION7 | NUMBER |  | 18 |  | INFORMATION7 |
| INFORMATION8 | NUMBER |  | 18 |  | INFORMATION8 |
| INFORMATION9 | NUMBER |  | 18 |  | INFORMATION9 |
| INFORMATION10 | NUMBER |  | 18 |  | INFORMATION10 |
| INFORMATION11 | VARCHAR2 | 255 |  |  | INFORMATION11 |
| INFORMATION12 | VARCHAR2 | 255 |  |  | INFORMATION12 |
| INFORMATION13 | VARCHAR2 | 255 |  |  | INFORMATION13 |
| INFORMATION14 | VARCHAR2 | 255 |  |  | INFORMATION14 |
| INFORMATION15 | VARCHAR2 | 255 |  |  | INFORMATION15 |
| INFORMATION16 | VARCHAR2 | 255 |  |  | INFORMATION16 |
| INFORMATION17 | VARCHAR2 | 255 |  |  | INFORMATION17 |
| INFORMATION18 | VARCHAR2 | 255 |  |  | INFORMATION18 |
| INFORMATION19 | VARCHAR2 | 255 |  |  | INFORMATION19 |
| INFORMATION20 | VARCHAR2 | 255 |  |  | INFORMATION20 |
| INFORMATION21 | DATE |  |  |  | INFORMATION21 |
| INFORMATION22 | DATE |  |  |  | INFORMATION22 |
| INFORMATION23 | DATE |  |  |  | INFORMATION23 |
| INFORMATION24 | DATE |  |  |  | INFORMATION24 |
| INFORMATION25 | DATE |  |  |  | INFORMATION25 |
| START_DATE_TIME | TIMESTAMP |  |  |  | START_DATE_TIME |
| END_DATE_TIME | TIMESTAMP |  |  |  | END_DATE_TIME |
| TOT_COUNT | NUMBER |  | 18 |  | TOT_COUNT |
| SUCC_COUNT | NUMBER |  | 18 |  | SUCC_COUNT |
| ERR_COUNT | NUMBER |  | 18 |  | ERR_COUNT |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ESS_TASK_INFO_N1 | Non Unique | Default | REQUEST_ID, MODE_CODE |
| CMP_ESS_TASK_INFO_N2 | Non Unique | Default | TASK_ID |
| cmp_ess_task_info_U1 | Unique | Default | ESS_TASK_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
