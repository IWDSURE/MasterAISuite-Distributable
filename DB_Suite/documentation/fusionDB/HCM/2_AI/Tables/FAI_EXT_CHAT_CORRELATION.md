# FAI_EXT_CHAT_CORRELATION

This table stores chat correlation data for external channel integrations.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiextchatcorrelation-19718.html#faiextchatcorrelation-19718](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiextchatcorrelation-19718.html#faiextchatcorrelation-19718)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_EXT_CHAT_CORRELATION_PK | ID |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| ID | NUMBER |  | Yes | Primary Key |
| CONVERSATION_ID | VARCHAR2 | 500 |  | Conversation identifier from Fusion Agents. |
| EXTERNAL_CONVERSATION_ID | VARCHAR2 | 500 |  | Conversation identifier from external integration. |
| EXTERNAL_USER_ID | VARCHAR2 | 200 |  | User identifier from external integration. |
| WORKFLOW_CODE | VARCHAR2 | 200 |  | Text identifier of the workflow. |
| WORKFLOW_VERSION | VARCHAR2 | 20 |  | Version of the workflow. |
| WORKFLOW_STATUS | VARCHAR2 | 40 |  | Status of the workflow. |
| ADDN_CONV_PARAMS | CLOB |  |  | Any additional conversation related details that have to be stored. |
| USER_ID | VARCHAR2 | 100 | Yes | User identifier from external integration. |
| LAST_JOB_ID | VARCHAR2 | 100 |  | Identifier of the last performed job. |
| EXT_CHANNEL_TYPE | VARCHAR2 | 100 | Yes | Identifier of external channel. |
| ADDN_CHANNEL_INFO | CLOB |  |  | Any additional channel specific inforamtion that has to be stored. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_EXT_CHAT_CORRELATION_N1 | Non Unique | Default | USER_ID, EXT_CHANNEL_TYPE |
| FAI_EXT_CHAT_CORRELATION_U1 | Unique | Default | ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
