# HRC_DL_REM_DISPOSED_COUNT

This table will store objects information disposed as part of data disposal process

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremdisposedcount-21920.html#hrcdlremdisposedcount-21920](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremdisposedcount-21920.html#hrcdlremdisposedcount-21920)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_DISP_COUNT_PK | DISPOSED_OBJ_COUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DISPOSED_OBJ_COUNT_ID | NUMBER |  |  | Yes | DISPOSED_OBJ_COUNT_ID |
| DISPOSAL_PROCESS_ID | NUMBER |  |  | Yes | DISPOSAL_PROCESS_ID |
| PERSON_ID | NUMBER |  |  | Yes | PERSON_ID |
| BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | BUSINESS_OBJECT_ID |
| RECORD_COUNT | NUMBER |  |  | Yes | RECORD_COUNT |
| DATA_SET_BUS_OBJ_ID | NUMBER |  |  | Yes | DATA_SET_BUS_OBJ_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_DISP_COUNT_N1 | Non Unique | Default | DISPOSAL_PROCESS_ID, PERSON_ID |
| HRC_DL_REM_DISP_COUNT_N2 | Non Unique | Default | DISPOSAL_PROCESS_ID, BUSINESS_OBJECT_ID |
| HRC_DL_REM_DISP_COUNT_U1 | Unique | Default | DISPOSED_OBJ_COUNT_ID |
| HRC_DL_REM_DISP_COUNT_U2 | Unique | Default | DISPOSAL_PROCESS_ID, DATA_SET_BUS_OBJ_ID, PERSON_ID, BUSINESS_OBJECT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
