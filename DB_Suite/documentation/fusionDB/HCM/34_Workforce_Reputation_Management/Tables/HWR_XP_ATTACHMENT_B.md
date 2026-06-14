# HWR_XP_ATTACHMENT_B

This is the table for the experience store attachments.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpattachmentb-7027.html#hwrxpattachmentb-7027](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpattachmentb-7027.html#hwrxpattachmentb-7027)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_ATTACHMENT_B_PK | ATTACHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this attachment. |
| USAGE_TYPE_IRI | VARCHAR2 | 2000 |  | Yes | The usage type iri for this attachment. |
| CONTENT_TYPE | VARCHAR2 | 255 |  | Yes | The content type of the attachment. |
| CONTENT | BLOB |  |  |  | The content of the attachment as binary data. |
| LENGTH | NUMBER |  | 10 | Yes | The lenght in bytes of the attachment. |
| SHA2 | VARCHAR2 | 255 |  | Yes | The computed sha2 of the attachment. |
| FILE_URL | VARCHAR2 | 2000 |  |  | The url of the file for this attachment. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_ATTACHMENT_B_N1 | Non Unique | Default | USAGE_TYPE_IRI |
| HWR_XP_ATTACHMENT_B_N2 | Non Unique | Default | SHA2 |
| HWR_XP_ATTACHMENT_B_U1 | Unique | Default | ATTACHMENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
