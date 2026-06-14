# ANC_PAY_INTERFACE_HEADER

This table holds information of  the absence pay interface header.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpayinterfaceheader-30071.html#ancpayinterfaceheader-30071](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpayinterfaceheader-30071.html#ancpayinterfaceheader-30071)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PAY_INTERFACE_HEADER_PK | HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HEADER_ID | NUMBER |  | 18 | Yes | HEADER_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| MAPPING_ID | NUMBER |  |  |  | MAPPING_ID |
| RATE_DEFINITION_ID | NUMBER |  |  |  | RATE_DEFINITION_ID |
| RATE_START | DATE |  |  | Yes | RATE_START |
| RATE_END | DATE |  |  |  | RATE_END |
| OVRIDING_RATE_DEF_ID | NUMBER |  |  |  | OVRIDING_RATE_DEF_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PAY_INTERFACE_HEADER_U1 | Unique | FUSION_TS_TX_DATA | HEADER_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
