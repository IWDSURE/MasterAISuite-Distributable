# PER_INTG_INBOUND_DETAILS

This table stores Details about the each record that was received.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintginbounddetails-22891.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintginbounddetails-22891.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INTG_INBOUND_DETAILS_PK | INBOUND_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INBOUND_DETAIL_ID | NUMBER |  | 18 | Yes | Unique Identifer to identify the row. |
| INBOUND_OBJECT_NAME | VARCHAR2 | 80 |  |  | Data object that wasn transferred and resulted in success in Partner system |
| INBOUND_OBJECT_KEY | NUMBER |  | 18 |  | Primay Key of the object. For example ,Candidate identifier,Requisition Identifier |
| ESS_REQUEST_ID | NUMBER |  | 30 |  | ESS job request Identifier that user submitted |
| INBOUND_DATA_ID | NUMBER |  | 18 |  | Inbound data identifier from the parent table PER_INTG_INBOUND_DATA |
| MESSAGE_TYPE | VARCHAR2 | 80 |  |  | Type of the message recieved from Partner |
| MESSAGE_DESCRIPTION | VARCHAR2 | 500 |  |  | message Description that partner sends back to Fusion |
| STATUS | VARCHAR2 | 30 |  |  | Status of record |
| STATE | VARCHAR2 | 30 |  |  | state of the record |
| BPEL_INSTANCE_ID | NUMBER |  | 18 |  | SOA BPEL instance Identifier |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | enterprise identifier for the mulit tenant purpose |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_INTG_INBOUND_DETAILS_N1 | Non Unique | Default | ESS_REQUEST_ID |
| PER_INTG_INBOUND_DETAILS_N2 | Non Unique | Default | BPEL_INSTANCE_ID |
| PER_INTG_INBOUND_DETAILS_N3 | Non Unique | Default | STATUS |
| PER_INTG_INBOUND_DETAILS_N4 | Non Unique | Default | STATE |
| PER_INTG_INBOUND_DETAILS_U1 | Unique | Default | INBOUND_DETAIL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
