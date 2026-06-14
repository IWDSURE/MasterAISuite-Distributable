# HWR_WLNS_TASKS_B

this table stores wellness tasks

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstasksb-13684.html#hwrwlnstasksb-13684](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstasksb-13684.html#hwrwlnstasksb-13684)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_TASKS_B_PK | TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_ID | NUMBER |  | 18 | Yes | This is the primary key of the table |
| START_DATE | TIMESTAMP |  |  | Yes | This column stores the start date of the corresponding task |
| END_DATE | TIMESTAMP |  |  | Yes | This column stores the end date of the corresponding task |
| AWARD_TYPE | VARCHAR2 | 20 |  | Yes | This column indicates type of award associated with task |
| AWARD | VARCHAR2 | 100 |  |  | This column indicates award associated with task |
| STATUS | VARCHAR2 | 10 |  | Yes | This column indicates status of the task |
| IS_ACTIVE | VARCHAR2 | 1 |  | Yes | This column indicates whether the task is active or not |
| IS_IMAGE | VARCHAR2 | 1 |  | Yes | This column indicates whether the task is associated with a image or not |
| ORDER_RANK | NUMBER |  | 18 | Yes | This column stores the rank of the task |
| PUBLISH_START_DATE | TIMESTAMP |  |  |  | This column indicates wellness  tasks publish start date. |
| PUBLISH_END_DATE | TIMESTAMP |  |  |  | This column indicates wellness  tasks publish end date. |
| TASK_ATTR_1 | VARCHAR2 | 200 |  |  | This column for extra task attribute |
| TASK_ATTR_2 | VARCHAR2 | 200 |  |  | This column for extra task attribute |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ARCHIVE_DATE | TIMESTAMP |  |  |  | This column stores the archival date of the corresponding task |
| IMAGE | BLOB |  |  |  | This column stores the image for the current task |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_TASKS_B_U1 | Unique | FUSION_TS_TX_DATA | TASK_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
