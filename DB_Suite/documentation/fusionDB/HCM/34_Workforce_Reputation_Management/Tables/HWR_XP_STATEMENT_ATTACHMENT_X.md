# HWR_XP_STATEMENT_ATTACHMENT_X

This is the table for the experience store statement attachment.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpstatementattachmentx-16591.html#hwrxpstatementattachmentx-16591](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpstatementattachmentx-16591.html#hwrxpstatementattachmentx-16591)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_STATE_ATTACH_X_PK | ATTACHMENT_ID, STATEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this attachment. |
| STATEMENT_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this statement. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_STATE_ATTACH_X_N1 | Non Unique | Default | STATEMENT_ID |
| HWR_XP_STATE_ATTACH_X_U1 | Unique | Default | ATTACHMENT_ID, STATEMENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
