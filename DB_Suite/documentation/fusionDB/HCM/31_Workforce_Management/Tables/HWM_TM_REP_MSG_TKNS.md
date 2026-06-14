# HWM_TM_REP_MSG_TKNS

Specific detail to use within a message associated with validation or rule execution on a time record or time record group.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmsgtkns-19698.html#hwmtmrepmsgtkns-19698](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmsgtkns-19698.html#hwmtmrepmsgtkns-19698)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REP_MSG_TKNS_PK | TM_REP_MSG_TKNS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REP_MSG_TKNS_ID | NUMBER |  | 18 | Yes | TM_MSG_TKNS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_REP_MSGS_ID | NUMBER |  | 18 | Yes | HWM_CALCD_TM_MSGS_ID |
| APPLICATION_ID | NUMBER |  | 18 |  | APPLICATION_ID |
| APPLICATION_SHORT_NAME | VARCHAR2 | 30 |  |  | APPLICATION_SHORT_NAME |
| TOKEN_NAME | VARCHAR2 | 256 |  |  | TOKEN_NAME |
| DATA_TYPE | VARCHAR2 | 256 |  |  | DATATYPE |
| TOKEN_VAL_NUMBER | NUMBER |  |  |  | TOKEN_VAL_NUMBER |
| TOKEN_VAL_VARCHAR | VARCHAR2 | 256 |  |  | TOKEN_VAL_VARCHAR |
| TOKEN_VAL_TIMESTAMP | TIMESTAMP |  |  |  | TOKEN_VAL_TIMESTAMP |
| TOKEN_VAL_DATE | DATE |  |  |  | TOKEN_VAL_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REP_MSG_TKNS_N1 | Non Unique | Default | TM_REP_MSGS_ID |
| HWM_TM_REP_MSG_TKNS_U1 | Unique | Default | TM_REP_MSG_TKNS_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
