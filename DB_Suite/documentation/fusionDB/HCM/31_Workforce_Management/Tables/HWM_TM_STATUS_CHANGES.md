# HWM_TM_STATUS_CHANGES

Transfer status changes event table for rest service.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatuschanges-8911.html#hwmtmstatuschanges-8911](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatuschanges-8911.html#hwmtmstatuschanges-8911)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_STATUS_CHANGES_PK | TM_STATUS_CHANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_STATUS_CHANGE_ID | NUMBER |  | 18 | Yes | TM_STATUS_CHANGE_ID |
| TM_STATUS_CHANGE_REQ_ID | NUMBER |  | 18 | Yes | TM_STATUS_CHANGE_REQ_ID |
| TM_BLDG_BLK_ID | NUMBER |  | 18 | Yes | TM_BLDG_BLK_ID |
| TM_BLDG_BLK_VERSION | NUMBER |  | 9 | Yes | TM_BLDG_BLK_VERSION |
| CONSUMER_CODE | VARCHAR2 | 30 |  | Yes | CONSUMER_CODE |
| STATUS_CODE | VARCHAR2 | 40 |  | Yes | STATUS_CODE |
| STATUS_VALUE | VARCHAR2 | 30 |  | Yes | STATUS_VALUE |
| PROCESS_STATUS | NUMBER |  | 2 | Yes | PROCESS_STATUS |
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
| HWM_TM_STATUS_CHANGES_U1 | Unique | Default | TM_STATUS_CHANGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
