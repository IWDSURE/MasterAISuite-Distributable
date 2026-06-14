# HWR_VLTR_ATTACHMENT

This table stores attachement related information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrattachment-30366.html#hwrvltrattachment-30366](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrattachment-30366.html#hwrvltrattachment-30366)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_ATTACHMENT_PK | ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ID | NUMBER |  | 18 | Yes | ATTACHMENT_ID |
| ATTACHMENT_TYPE | VARCHAR2 | 100 |  |  | ATTACHMENT_TYPE |
| ATTACHMENT_NAME | VARCHAR2 | 100 |  |  | ATTACHMENT_NAME |
| ATTACHMENT_SIZE | NUMBER |  | 18 |  | ATTACHMENT_SIZE |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| VALUE | BLOB |  |  |  | VALUE |
| IS_STAFF_ONLY | NUMBER |  | 1 |  | IS_STAFF_ONLY |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 20 |  |  | ENTITY_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_ATTACHMENT_U1 | Unique | FUSION_TS_TX_IDX | ATTACHMENT_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
