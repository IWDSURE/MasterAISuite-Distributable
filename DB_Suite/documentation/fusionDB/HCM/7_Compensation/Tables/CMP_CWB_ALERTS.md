# CMP_CWB_ALERTS

Stores the alerts enabled for a person in a compensation plan period. For example, employee terminated or leave of absence.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbalerts-4568.html#cmpcwbalerts-4568](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbalerts-4568.html#cmpcwbalerts-4568)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_ALERTS_PK | PERSON_EVENT_ID, ALERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_EVENT_ID | NUMBER |  | 18 | Yes | PERSON_EVENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| ALERT_ID | NUMBER |  | 18 | Yes | ALERT_ID |
| PLAN_ID | NUMBER |  | 18 | Yes | PLAN_ID |
| PERIOD_ID | NUMBER |  | 18 | Yes | PERIOD_ID |
| DISPLAY_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TRIGGER_SOURCE | VARCHAR2 | 1 |  |  | Will store R for Refresh Process, S for Start Process, H for HR Change and null in case of Manager. |
| HIDE_FROM_MANAGER_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate whether the alert is hidden from managers or not. |
| TRIGGERED_BY | NUMBER |  | 18 |  | Stores person_id of the person who triggered the alert to show. |
| TRIGGERED_DATE | TIMESTAMP |  |  |  | Stores the timestamp when the alert was last triggered. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_ALERTS_N1 | Non Unique | Default | PERIOD_ID, PLAN_ID |
| CMP_CWB_ALERTS_PK | Unique | Default | PERSON_EVENT_ID, ALERT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
