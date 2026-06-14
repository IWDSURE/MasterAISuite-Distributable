# HWR_WLNS_ATTACH_RSP

This table will be used to store the attachment response.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsattachrsp-5141.html#hwrwlnsattachrsp-5141](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsattachrsp-5141.html#hwrwlnsattachrsp-5141)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_ATTACH_RSP_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key of attachment response table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the wellness questionnaire ID which has the attachment. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 | Yes | The wellness questionnaire version which has the attachment. |
| QUESTION_ID | NUMBER |  | 18 | Yes | The question ID associated with the questionnaire which allows the attachment. |
| QUESTION_VERSION | NUMBER |  | 18 | Yes | The question version associated with the question which allows the attachment. |
| PARTICIPANT_ID | VARCHAR2 | 500 |  | Yes | The Fusion Id of the participant of the wellness assessment. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| QSTN_RESPONSE_ID | NUMBER |  | 18 | Yes | The question response ID for this participant response from questionnaire table. |
| ATTACHMENT_DATE | TIMESTAMP |  |  | Yes | Last updated date for the participant who submits the attachment for this question. |
| WLNS_ATTACHMENT_ATTR_1 | VARCHAR2 | 100 |  |  | WLNS_ATTACHMENT_ATTR_1. This is the extra attribute in case if needed. |
| WLNS_ATTACHMENT_ATTR_2 | VARCHAR2 | 100 |  |  | WLNS_ATTACHMENT_ATTR_2. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_ATTACH_RSP_U1 | Unique | Default | ID |
| HWR_WLNS_ATTACH_RSP_U2 | Unique | Default | QUESTIONNAIRE_ID, QUESTION_ID, PARTICIPANT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
