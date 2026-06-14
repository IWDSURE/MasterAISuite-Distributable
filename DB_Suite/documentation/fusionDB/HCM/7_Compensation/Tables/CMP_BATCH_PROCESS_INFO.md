# CMP_BATCH_PROCESS_INFO

Stores CMP Batch process information in the database.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbatchprocessinfo-31431.html#cmpbatchprocessinfo-31431](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpbatchprocessinfo-31431.html#cmpbatchprocessinfo-31431)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| PROCESS_CD | VARCHAR2 | 30 |  | Yes | PROCESS_CD |
| STRT_DT_TM | TIMESTAMP |  |  |  | STRT_DT_TM |
| END_DT_TM | TIMESTAMP |  |  |  | END_DT_TM |
| ELPSD_TM | VARCHAR2 | 90 |  |  | ELPSD_TM |
| GRADE_LADDER_ID | NUMBER |  | 18 | Yes | GRADE_LADDER_ID |
| GRADE_LADDER_GRP_CODE | VARCHAR2 | 30 |  |  | Grade Ladder Group Code |
| TOTAL_SELECTED | NUMBER |  | 18 |  | TOTAL_SELECTED |
| TOTAL_PROCESSED | NUMBER |  | 18 |  | TOTAL_PROCESSED |
| TOTAL_APPROVED | NUMBER |  | 18 |  | TOTAL_APPROVED |
| TOTAL_REJECTED | NUMBER |  | 18 |  | TOTAL_REJECTED |
| TOTAL_ERRORED | NUMBER |  | 18 |  | TOTAL_ERRORED |
| BATCH_INFORMATION1 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION1 |
| BATCH_INFORMATION2 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION2 |
| BATCH_INFORMATION3 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION3 |
| BATCH_INFORMATION4 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION4 |
| BATCH_INFORMATION5 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION5 |
| BATCH_INFORMATION6 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION6 |
| BATCH_INFORMATION7 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION7 |
| BATCH_INFORMATION8 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION8 |
| BATCH_INFORMATION9 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION9 |
| BATCH_INFORMATION10 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION10 |
| BATCH_INFORMATION11 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION11 |
| BATCH_INFORMATION12 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION12 |
| BATCH_INFORMATION13 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION13 |
| BATCH_INFORMATION14 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION14 |
| BATCH_INFORMATION15 | VARCHAR2 | 250 |  |  | BATCH_INFORMATION15 |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_BATCH_PROCESS_INFO_N1 | Non Unique | Default | GRADE_LADDER_ID |
| CMP_BATCH_PROCESS_INFO_N2 | Non Unique | Default | GRADE_LADDER_GRP_CODE |
| CMP_BATCH_PROCESS_INFO_U1 | Unique | Default | REQUEST_ID, GRADE_LADDER_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
