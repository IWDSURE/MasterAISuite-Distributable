# HWR_WLNS_QSTN_B

This table stores the wellness questions.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstnb-4159.html#hwrwlnsqstnb-4159](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstnb-4159.html#hwrwlnsqstnb-4159)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_QSTN_B_PK | QUESTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| FUS_PROFILE_ID | NUMBER |  | 18 | Yes | This is the fusion profile ID of the employee who asks the question. |
| SOURCE_ID | NUMBER |  | 18 |  | This is the id of communication source. |
| CONVERSATION_ID | VARCHAR2 | 1000 |  |  | This is the id of the conversation. |
| RESPONSES | NUMBER |  | 18 |  | The number of responses to the question. |
| EXPERTS | NUMBER |  | 18 |  | The number of experts found for the question. |
| IS_VALID | VARCHAR2 | 32 |  |  | Whether the question contains a valid topic. |
| IS_ANALYZED | VARCHAR2 | 32 |  |  | Whether the question is analyzed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_QSTN_B_U1 | Unique | Default | QUESTION_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
