# HWM_TM_STATUS_CHANGE_REQS

Transfer status changes request table for rest service.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatuschangereqs-14958.html#hwmtmstatuschangereqs-14958](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatuschangereqs-14958.html#hwmtmstatuschangereqs-14958)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_STATUS_CHANGE_REQS_PK | TM_STATUS_CHANGE_REQ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_STATUS_CHANGE_REQ_ID | NUMBER |  | 18 | Yes | TM_STATUS_CHANGE_REQ_ID |
| SOURCE_ID | VARCHAR2 | 40 |  | Yes | SOURCE_ID |
| REQUEST_TIMESTAMP_STRING | VARCHAR2 | 80 |  | Yes | REQUEST_TIMESTAMP_STRING |
| REQ_NUMBER | VARCHAR2 | 80 |  | Yes | REQ_NUMBER |
| REQ_STATUS | NUMBER |  | 2 | Yes | REQ_STATUS |
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
| HWM_TM_STATUS_CHANGE_REQS_U1 | Unique | Default | TM_STATUS_CHANGE_REQ_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
