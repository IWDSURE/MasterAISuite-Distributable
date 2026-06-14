# PER_INTG_OUTBOUND_ERROR

This table stores a row for each unsuccessful transfer of a row to the partner.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintgoutbounderror-14019.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perintgoutbounderror-14019.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INTG_OUTBOUND_ERROR_PK | OUTBOUND_DATA_ERROR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OUTBOUND_DATA_ERROR_ID | NUMBER |  | 18 | Yes | Unique Identifer to identify the row. |
| OUTBOUND_OBJECT_NAME | VARCHAR2 | 80 |  |  | Data object that wasn transferred and resulted in error in Partner system |
| OUTBOUND_OBJECT_KEY | NUMBER |  | 18 |  | Primay Key of the object. For example , postion identifier for postions |
| ESS_REQUEST_ID | NUMBER |  | 30 |  | ESS job request Id that user submitted |
| OUTBOUND_DATA_ID | NUMBER |  | 18 |  | Outbound data identifier |
| ERROR_TYPE | VARCHAR2 | 80 |  |  | Type of the error recieved from Partner |
| ERROR_DESCRIPTION | VARCHAR2 | 500 |  |  | Eror Description that partner sends back to Fusion |
| PARTNER_RESPONSE_DOCUMENT | CLOB |  |  |  | this is the output document sent by partner |
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
| PER_INTG_OUTBOUND_ERROR_N1 | Non Unique | Default | ESS_REQUEST_ID |
| PER_INTG_OUTBOUND_ERROR_N2 | Non Unique | Default | OUTBOUND_OBJECT_NAME, OUTBOUND_OBJECT_KEY, ESS_REQUEST_ID |
| PER_INTG_OUTBOUND_ERROR_U1 | Unique | Default | OUTBOUND_DATA_ERROR_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
