# HRC_DL_ARC_FILE_LINES

This table holds data for Each line present in the .dat file. Each row will be identified using LINE_ID

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlarcfilelines-23901.html#hrcdlarcfilelines-23901](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlarcfilelines-23901.html#hrcdlarcfilelines-23901)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_ARC_FILE_LINES_PK | LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LINE_ID | NUMBER |  | 18 | Yes | LINE_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| SEQ_NUM | NUMBER |  | 18 | Yes | SEQ_NUM |
| TEXT | VARCHAR2 | 4000 |  |  | TEXT |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| COMPLETE_LINE | VARCHAR2 | 10 |  |  | COMPLETE_LINE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_ARC_FILE_LINES_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_ARC_FILE_LINES_U1 | Unique | Default | LINE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
