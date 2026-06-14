# HXT_APRV_TASK_ENTRY_DETAIL

This table stores all the entry level details of the time card and approvals

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtaprvtaskentrydetail-28806.html#hxtaprvtaskentrydetail-28806](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtaprvtaskentrydetail-28806.html#hxtaprvtaskentrydetail-28806)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_APRV_TASK_ENTRY_DETAI_PK | APRV_TASK_ENTRY_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APRV_TASK_ENTRY_DETAIL_ID | NUMBER |  | 18 | Yes | APRV_TASK_ENTRY_DETAIL_ID |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ACTION | VARCHAR2 | 60 |  |  | ACTION |
| APRV_TM_REC_GRP_ID | NUMBER |  | 18 |  | APRV_TM_REC_GRP_ID |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMB1 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB1 |
| ATTRIBUTE_NUMB2 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB2 |
| ATTRIBUTE_NUMB3 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB3 |
| ATTRIBUTE_NUMB4 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB4 |
| ATTRIBUTE_NUMB5 | NUMBER |  | 18 |  | ATTRIBUTE_NUMB5 |
| TM_ENTRY_ROW_ID | NUMBER |  | 18 |  | TM_ENTRY_ROW_ID |
| CONSUMER_CODE | VARCHAR2 | 20 |  |  | CONSUMER_CODE |
| HUMAN_TASK_ID | VARCHAR2 | 64 |  |  | HUMAN_TASK_ID |
| TASK_ASSIGNEE | VARCHAR2 | 400 |  |  | TASK_ASSIGNEE |
| TASK_REQUESTOR | VARCHAR2 | 400 |  |  | TASK_REQUESTOR |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 240 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hxt_aprv_entry_detail_N1 | Non Unique | Default | APRV_TM_REC_GRP_ID |
| hxt_aprv_entry_detail_U1 | Unique | Default | APRV_TASK_ENTRY_DETAIL_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
