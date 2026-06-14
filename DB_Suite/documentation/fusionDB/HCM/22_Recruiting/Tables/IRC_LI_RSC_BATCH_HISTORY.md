# IRC_LI_RSC_BATCH_HISTORY

Stores the history of batch calls that were made as part of LinkedIn RSC integration

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscbatchhistory-11615.html#irclirscbatchhistory-11615](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscbatchhistory-11615.html#irclirscbatchhistory-11615)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_RSC_BATCH_HISTORY_PK | BATCH_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| ENTITY_TYPE_CODE | VARCHAR2 | 20 |  | Yes | Indicates the type of ORC entity. The corresponding lookup type is ORA_IRC_LI_RSC_ENTITY_TYPE |
| ACTION_CODE | VARCHAR2 | 20 |  | Yes | Action to be excuted by the sync. The corresponding lookup type is ORA_IRC_LI_RSC_ACTION |
| BATCH_COUNT | NUMBER |  | 4 |  | Stores the number of records sent in the batch |
| PAYLOAD | CLOB |  |  |  | The payload sent to LinkedIn RSC. |
| RESPONSE_PAYLOAD | CLOB |  |  |  | The payload received from LinkedIn RSC. |
| URL | CLOB |  |  |  | The url used when sending to LinkedIn RSC. |
| STATUS_CODE | VARCHAR2 | 20 |  |  | The status of this sync action. The corresponding lookup type is ORA_IRC_LI_RSC_SYNC_STATUS |
| METHOD | VARCHAR2 | 20 |  |  | Http method that used in the request. |
| REQUEST_HEADERS | CLOB |  |  |  | Http request headers that is used here. |
| RESPONSE_STATUS_CODE | NUMBER |  | 18 |  | Http status code of http response. |
| STATUS_MESSAGE | CLOB |  |  |  | Http status message that is returned in response. |
| RESPONSE_HEADERS | CLOB |  |  |  | Http response headers returned from the response. |
| REQUEST_START_TIME | TIMESTAMP |  |  |  | The time that the http request started. |
| REQUEST_END_TIME | TIMESTAMP |  |  |  | The time that the http request ended. |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Ess Job ID, the ess request ID of the job. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Indicates the date and time when the batch call was made to LinkedIn. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_RSC_BATCH_HISTORY_N1 | Non Unique | Default | ACTION_CODE, ENTITY_TYPE_CODE |
| IRC_LI_RSC_BATCH_HISTORY_N2 | Non Unique | Default | CREATION_DATE |
| IRC_LI_RSC_BATCH_HISTORY_N3 | Non Unique | Default | ENTITY_TYPE_CODE, PROCESSED_DATE |
| IRC_LI_RSC_BATCH_HISTORY_PK | Unique | Default | BATCH_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
