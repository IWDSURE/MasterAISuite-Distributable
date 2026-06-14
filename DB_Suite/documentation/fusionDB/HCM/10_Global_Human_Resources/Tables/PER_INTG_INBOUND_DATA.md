# PER_INTG_INBOUND_DATA

Table to store  inbound xml data received from partners and track the progress of the data in.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintginbounddata-24915.html#perintginbounddata-24915](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintginbounddata-24915.html#perintginbounddata-24915)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INTG_INBOUND_DATA_PK | INBOUND_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INBOUND_DATA_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PARTNER_ID | NUMBER |  | 18 |  | This stores Partner id and is referenced to Topology manger application id from ASK tables |
| INBOUND_DATA_CACHE | CLOB |  |  |  | Inbound XML coming from partners |
| STATUS | VARCHAR2 | 30 |  |  | status of the xml file to store various stages of the inbound data . |
| STATE | VARCHAR2 | 30 |  |  | This is the stae of the entire composite |
| PARTNER_NAME | VARCHAR2 | 80 |  |  | Name of the application in ASK topology table correspond to PARTNER ID stored in this table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| INTEGRATION_MESSAGE_ID | NUMBER |  | 18 |  | Integration Message Identifier one |
| PAYLOAD_TYPE | VARCHAR2 | 300 |  |  | Payload Type |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Ess Request Id |
| COMPOSITE_INSTANCE_ID | NUMBER |  | 30 |  | BPEL Composite instance id from the Enterprise Manager SOA server. |
| ERROR_CODE | VARCHAR2 | 30 |  |  | System generated error code , this is not the data validation but mostly stores infrastructure errors |
| ERROR_DESCRIPTION | VARCHAR2 | 300 |  |  | Description of the errors |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| INTEGRATION_MESSAGE_ID2 | NUMBER |  | 18 |  | Integration Message Identifier Two |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_INTG_INBOUND_DATA_N1 | Non Unique | FUSION_TS_TX_IDX | COMPOSITE_INSTANCE_ID |
| PER_INTG_INBOUND_DATA_N2 | Non Unique | FUSION_TS_TX_IDX | ESS_REQUEST_ID |
| PER_INTG_INBOUND_DATA_U1 | Unique | FUSION_TS_TX_IDX | INBOUND_DATA_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
