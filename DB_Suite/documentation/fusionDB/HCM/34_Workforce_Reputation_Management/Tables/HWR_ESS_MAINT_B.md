# HWR_ESS_MAINT_B

This table will be used to store maintain information about Alerts to be deleted which is being used by HWR ESS job

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressmaintb-23053.html#hwressmaintb-23053](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressmaintb-23053.html#hwressmaintb-23053)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ESS_MAINT_B_PK | RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ID | NUMBER |  | 18 | Yes | RUN_ID -This is the alert run id which needs to be deleted by ESS job |
| ALERT_NAME | VARCHAR2 | 100 |  | Yes | ALERT_NAME |
| RECIPIENT_USERNAME | VARCHAR2 | 100 |  |  | RECIPIENT_USERNAME |
| IS_DEL | VARCHAR2 | 20 |  | Yes | IS_DEL |
| HWR_ALERT_ATTR1 | VARCHAR2 | 2000 |  |  | HWR_ALERT_ATTR1 |
| HWR_ALERT_ATTR2 | VARCHAR2 | 1000 |  |  | HWR_ALERT_ATTR2 |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ESS_MAINT_B_U1 | Unique | Default | RUN_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
