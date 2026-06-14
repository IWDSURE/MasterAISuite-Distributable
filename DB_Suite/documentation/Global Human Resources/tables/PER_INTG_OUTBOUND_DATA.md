# PER_INTG_OUTBOUND_DATA

This table is to track the Outbound data sent to Recruitment partner

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintgoutbounddata-17832.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintgoutbounddata-17832.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INTG_OUTBOUND_DATA_PK | OUTBOUND_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OUTBOUND_DATA_ID | NUMBER |  | 18 | Yes | This column is unique identtifier for the row |
| OUTBOUND_OBJECT_NAME | VARCHAR2 | 80 |  |  | This column is to indicate the object being exported to thrid party applications. This columns stores lookup codes for lookup type PER_INTG_EXPORT_JOB . |
| OUTBOUND_DATA_CACHE | CLOB |  |  |  | paylaoad that is being sent to third party application |
| PARENT_BPEL_INSTANCE_ID | NUMBER |  | 30 |  | BPEL composite identifier of the Parent Instance that sends data out |
| CHILD_BPEL_INSTANCE_ID | NUMBER |  | 30 |  | BPEL compoiste Identifier that sends data and spawned by Parent Instance Identifier |
| ESS_REQUEST_ID | NUMBER |  | 30 |  | ESS request Identifier that submitted the outbound data transfer |
| OUTBOUND_DATA_SENT_TIME | TIMESTAMP |  |  |  | Date and Time of the outbound data sent |
| RESULT_RECEIVED_TIME | TIMESTAMP |  |  |  | date and time of the result receieved from partner. |
| STATUS | VARCHAR2 | 30 |  |  | Status of the data sent to partners. |
| STATE | VARCHAR2 | 30 |  |  | State of the transfer of data to partners |
| PARTNER_NAME | VARCHAR2 | 80 |  |  | name of the partner that data was sent to |
| PARTNER_MESSAGE_KEY1 | NUMBER |  | 18 |  | Partner sent message key. |
| PARTNER_MESSAGE_KEY2 | NUMBER |  | 18 |  | Partner Sent message key 2 |
| PARTNER_RESPONSE_DOCUMENT | CLOB |  |  |  | payload response sent by partner. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Enterprise identifier. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BATCH_FETCH_START | NUMBER |  | 18 |  | This column stores the fetch start of the records being sent to partners |
| BATCH_FETCH_SIZE | NUMBER |  | 18 |  | This column stores size of the batch that was sent to partners |
| RECORDS_PROCESSED | NUMBER |  | 18 |  | This column holds the number of records processed by partner |
| RECORDS_ERRORED | NUMBER |  | 18 |  | This column holds the number of Records Errored |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_INTG_OUTBOUND_DATA_N1 | Non Unique | Default | ESS_REQUEST_ID |
| PER_INTG_OUTBOUND_DATA_N2 | Non Unique | Default | PARENT_BPEL_INSTANCE_ID, ESS_REQUEST_ID |
| PER_INTG_OUTBOUND_DATA_U1 | Unique | Default | OUTBOUND_DATA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
