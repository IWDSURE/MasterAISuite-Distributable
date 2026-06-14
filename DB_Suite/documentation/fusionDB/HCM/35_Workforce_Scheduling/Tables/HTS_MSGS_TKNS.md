# HTS_MSGS_TKNS

Specific detail to use within a message associated with validation or execution on intenalization of shifts imported.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsmsgstkns-6518.html#htsmsgstkns-6518](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsmsgstkns-6518.html#htsmsgstkns-6518)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_MSGS_TKNS_PK | HTS_MSG_TKNS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HTS_MSG_TKNS_ID | NUMBER |  | 18 | Yes | HTS_MSG_TKNS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| HTS_MSGS_ID | NUMBER |  | 18 | Yes | HTS_MSGS_ID |
| TOKEN_NAME | VARCHAR2 | 256 |  |  | TOKEN_NAME |
| DATA_TYPE | VARCHAR2 | 256 |  |  | DATATYPE |
| TOKEN_VALUE | VARCHAR2 | 256 |  |  | TOKEN_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_MSGS_TKNS_N1 | Non Unique | FUSION_TS_TX_IDX | HTS_MSGS_ID |
| HTS_MSGS_TKNS_U1 | Unique | FUSION_TS_TX_IDX | HTS_MSG_TKNS_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
