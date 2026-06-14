# HWR_WLNS_QSTN_EXPERT

This table stores the experts found for the question.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstnexpert-21459.html#hwrwlnsqstnexpert-21459](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstnexpert-21459.html#hwrwlnsqstnexpert-21459)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_QSTN_EXPERT_PK | QUESTION_ID, TOPIC_ID, EXPERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | The columns stores the question id. |
| TOPIC_ID | NUMBER |  | 18 | Yes | The corresponding wellness topic id. |
| EXPERT_ID | NUMBER |  | 18 | Yes | The fusion profile id of the expert. |
| NOTIFICATION_SENT | VARCHAR2 | 32 |  |  | Indicates if the notification is sent. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_QSTN_EXPERT_U1 | Unique | Default | QUESTION_ID, TOPIC_ID, EXPERT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
