# HWR_VLTR_NOTIFICATION_RECORD

Table for storing which notifications have been sent

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrnotificationrecord-18077.html#hwrvltrnotificationrecord-18077](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrnotificationrecord-18077.html#hwrvltrnotificationrecord-18077)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_NOTIFICATION_REC_PK | NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTIFICATION_ID | NUMBER |  | 18 | Yes | NOTIFICATIONID |
| OBJECT_TYPE | VARCHAR2 | 40 |  | Yes | OBJECTTYPE |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECTID |
| NOTIFICATION_TYPE | VARCHAR2 | 100 |  | Yes | NOTIFICATIONTYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_NOTIFICATION_RCRD_U1 | Unique | FUSION_TS_TX_IDX | NOTIFICATION_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
