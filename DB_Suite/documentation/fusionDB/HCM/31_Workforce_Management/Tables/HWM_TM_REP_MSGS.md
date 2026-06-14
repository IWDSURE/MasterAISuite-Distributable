# HWM_TM_REP_MSGS

Information associated with a time record or time record group after validation or rule execution.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmsgs-30313.html#hwmtmrepmsgs-30313](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmsgs-30313.html#hwmtmrepmsgs-30313)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REP_MSGS_PK | TM_REP_MSGS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REP_MSGS_ID | NUMBER |  | 18 | Yes | TM_MSGS_ID |
| TM_EVENT_ID | NUMBER |  | 18 |  | Obsolete |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_REP_ATRB_USAGE_ID | NUMBER |  | 18 |  | Primary key of the Time Attribute Usages |
| TM_BLDG_BLK_ID | NUMBER |  | 18 |  | Foreign key to TM_REC_GRP_ID from HWM_TM_REC_GRP table or to TM_REC_ID from HWM_TM_REC table or to TM_EVENT_ID from HWM_TM_EVENTS table |
| TM_BLDG_BLK_VERSION | NUMBER |  | 9 |  | Foreign key to TM_REC_GRP_VERSION from HWM_TM_REC_GRP table or to TM_REC_VERSION from HWM_TM_REC table, Empty in case of Time Event |
| TM_REC_ID | NUMBER |  | 18 |  | Obsolete |
| TM_REC_VERSION | NUMBER |  | 9 |  | Obsolete |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | Obsolete |
| TM_REC_GRP_VERSION | NUMBER |  | 9 |  | Obsolete |
| TRN_ID | NUMBER |  | 18 |  | TM_MSGS_ID |
| MESSAGE_FIELD | VARCHAR2 | 256 |  |  | Foreign key to HWM_TM_BLDG_BLKS |
| MESSAGE_NAME | VARCHAR2 | 256 |  | Yes | Foreign key to HWM_TM_BLDG_BLKS |
| APPLICATION_ID | NUMBER |  | 16 | Yes | APPLICATION_ID instead of short name, since the name can change |
| APPLICATION_SHORT_NAME | VARCHAR2 | 30 |  |  | APPLICATION_SHORT_NAME |
| MESSAGE_LEVEL | VARCHAR2 | 30 |  | Yes | MESSAGE_LEVEL |
| DATE_FROM | TIMESTAMP |  |  | Yes | DATE_FROM |
| DATE_TO | TIMESTAMP |  |  |  | DATE_TO |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_TM_REP_MSGS_N1 | Non Unique | Default | TM_REC_GRP_ID | Obsolete |
| HWM_TM_REP_MSGS_N2 | Non Unique | Default | TM_REC_ID | Obsolete |
| HWM_TM_REP_MSGS_N3 | Non Unique | Default | TM_BLDG_BLK_ID, TM_BLDG_BLK_VERSION |  |
| HWM_TM_REP_MSGS_N4 | Non Unique | Default | TM_BLDG_BLK_ID, DATE_TO |  |
| HWM_TM_REP_MSGS_U1 | Unique | Default | TM_REP_MSGS_ID |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
