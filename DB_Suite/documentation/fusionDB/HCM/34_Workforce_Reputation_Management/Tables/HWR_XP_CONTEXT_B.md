# HWR_XP_CONTEXT_B

This is the table for the experience store contexts.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpcontextb-27135.html#hwrxpcontextb-27135](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpcontextb-27135.html#hwrxpcontextb-27135)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_CONTEXT_B_PK | CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEXT_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this context. |
| STATEMENT_REF_ID | NUMBER |  | 18 |  | The Unique database identifier for the statement. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_CONTEXT_B_N1 | Non Unique | Default | STATEMENT_REF_ID |
| HWR_XP_CONTEXT_B_U1 | Unique | Default | CONTEXT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
