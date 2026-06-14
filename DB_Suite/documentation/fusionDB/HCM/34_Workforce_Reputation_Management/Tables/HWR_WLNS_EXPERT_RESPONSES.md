# HWR_WLNS_EXPERT_RESPONSES

This table stores the responses for wellness ask an expert.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsexpertresponses-26992.html#hwrwlnsexpertresponses-26992](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsexpertresponses-26992.html#hwrwlnsexpertresponses-26992)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_EXPERT_RESPONSES_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| FUS_PROFILE_ID | NUMBER |  | 18 | Yes | This is the fusion profile ID of the employee who gave the response. |
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the question ID from wellness question table. |
| TOPIC_ID | NUMBER |  | 18 | Yes | The wellness topic id. |
| SPECIFIC_RESPONSES | NUMBER |  | 18 |  | The responses that topics can be detected. |
| GENERAL_RESPONSES | NUMBER |  | 18 |  | The responses which topics cannot be detected. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_EXPERT_RESPONSES_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
