# HHR_VLTR_EVENT_NOTIF

This table stores notification event info

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltreventnotif-24526.html#hhrvltreventnotif-24526](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltreventnotif-24526.html#hhrvltreventnotif-24526)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_EVENT_NOTIFICATION_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| ALERT_NAME | VARCHAR2 | 64 |  | Yes | ALERT_NAME |
| PARAMETER_MAP | CLOB |  |  | Yes | PARAMETER_MAP |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| STATUS | VARCHAR2 | 50 |  |  | STATUS |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | ERROR_MESSAGE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_EVENT_NOTIFICATION_U1 | Unique | FUSION_TS_TX_IDX | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
