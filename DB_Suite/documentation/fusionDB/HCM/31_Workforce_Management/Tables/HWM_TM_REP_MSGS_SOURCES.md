# HWM_TM_REP_MSGS_SOURCES

Table to record the source of messages by recording the rule which creates the messages

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmsgssources-23252.html#hwmtmrepmsgssources-23252](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmsgssources-23252.html#hwmtmrepmsgssources-23252)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REP_MSGS_SOURCES_PK | TM_REP_MSGS_SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REP_MSGS_SOURCE_ID | NUMBER |  | 18 | Yes | TM_REP_MSGS_SOURCE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_REP_MSGS_ID | NUMBER |  | 18 | Yes | Foreign key to HWM_TM_REP_MSGS, tracks the message usages, sources |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| RULE_SET_ID | NUMBER |  | 18 | Yes | Foreign key to HWM_RULE_SETS_F, tracks the rule set which created the message |
| RULE_ID | NUMBER |  | 18 | Yes | Foreign key to HWM_RULES, tracks the rule which created the message |
| RULE_SET_TYPE | VARCHAR2 | 32 |  | Yes | Stores the type of rule set |
| TAG | VARCHAR2 | 120 |  | Yes | TAG |
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

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REP_MSGS_SOURCES_N1 | Non Unique | FUSION_TS_TX_IDX | RULE_SET_ID |
| HWM_TM_REP_MSGS_SOURCES_N2 | Non Unique | Default | TM_REP_MSGS_ID |
| HWM_TM_REP_MSGS_SOURCES_U1 | Unique | FUSION_TS_TX_IDX | TM_REP_MSGS_SOURCE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
