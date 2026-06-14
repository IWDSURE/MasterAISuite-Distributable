# HRC_TXN_TAC_ALERT_RECIPIENT_

The user stores the combination of username vs alert templates with respect to a process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxntacalertrecipient-12942.html#hrctxntacalertrecipient-12942](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxntacalertrecipient-12942.html#hrctxntacalertrecipient-12942)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_TAC_ALERT_RECIPIE_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ALERT_RECIPIENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALERT_RECIPIENT_ID | NUMBER |  | 18 | Yes | This column stores the primary key of the table and it cannot be null. |
| USERNAME | VARCHAR2 | 64 |  |  | This column stores the username to which the Alert has to be sent. |
| PROCESS_ID | NUMBER |  | 18 |  | Foreign key to HRC_ARM_APPROVAL_OPTIONS table. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ALERT_TEMPLATE_OBJECT_GUID | VARCHAR2 | 32 |  |  | This is used for maintaining consistency of seed data framework. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_TAC_ALRT_RCPT_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ALERT_RECIPIENT_ID |
| TAC_ALERT_RECIPIENT_N1_ | Non Unique | Default | ALERT_RECIPIENT_ID, LAST_UPDATE_DATE, LAST_UPDATED_BY |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
