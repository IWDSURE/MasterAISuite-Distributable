# HWR_PER_ORG_LEAD_XREF

This cross reference (xref) table stores relationship between organization and its lead.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorgleadxref-10328.html#hwrperorgleadxref-10328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorgleadxref-10328.html#hwrperorgleadxref-10328)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_ORG_LEAD_XREF_PK | HWR_ORG_ID, LEAD_SOURCE_ID, LEAD_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HWR_ORG_ID | VARCHAR2 | 500 |  | Yes | The Id of the first organization. |
| LEAD_PRFL_ID | VARCHAR2 | 500 |  | Yes | The profile Id of the organization lead. |
| LEAD_SOURCE_ID | NUMBER |  | 18 | Yes | The source Id of the organization lead. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PER_ORG_LEAD_XREF_N1 | Non Unique | FUSION_TS_TX_DATA | LEAD_SOURCE_ID, LEAD_PRFL_ID |
| HWR_PER_ORG_LEAD_XREF_U1 | Unique | FUSION_TS_TX_DATA | HWR_ORG_ID, LEAD_SOURCE_ID, LEAD_PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
