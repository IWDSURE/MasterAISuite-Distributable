# ANC_PAY_INTERFACE_LINES

This table holds information of  the absence pay interface details.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpayinterfacelines-11001.html#ancpayinterfacelines-11001](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpayinterfacelines-11001.html#ancpayinterfacelines-11001)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PAY_INTERFACE_LINES_PK | LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LINE_ID | NUMBER |  | 18 | Yes | LINE_ID |
| HEADER_ID | NUMBER |  | 18 | Yes | HEADER_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ABS_DATE | DATE |  |  | Yes | ABS_DATE |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| UNITS | NUMBER |  |  |  | UNITS |
| OVRD_UNITS | NUMBER |  |  |  | OVRD_UNITS |
| PAY_FACTOR | NUMBER |  |  |  | PAY_FACTOR |
| OVRD_PAY_FACTOR | NUMBER |  |  |  | OVRD_PAY_FACTOR |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PAY_INTERFACE_LINES_U1 | Unique | FUSION_TS_TX_DATA | LINE_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
