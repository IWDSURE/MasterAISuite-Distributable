# HWR_ENDORSE_GBL_PRFL_X

This cross reference (xref) table stores relationship between global profile and endorsement.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrendorsegblprflx-14869.html#hwrendorsegblprflx-14869](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrendorsegblprflx-14869.html#hwrendorsegblprflx-14869)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ENDORSE_GBL_PRFL_X_PK | ENDORSEMENT_ID, GBL_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENDORSEMENT_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the endorsement table. |
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | The Id of the global profile which has the endorsement. |
| FUS_PRFL_ID | NUMBER |  | 18 |  | The Id of the fusion profile which has the endorsement. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ENDORSE_GBL_PRFL_X_N1 | Non Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID |
| HWR_ENDORSE_GBL_PRFL_X_N2 | Non Unique | FUSION_TS_TX_DATA | FUS_PRFL_ID |
| HWR_ENDORSE_GBL_PRFL_X_U1 | Unique | FUSION_TS_TX_DATA | ENDORSEMENT_ID, GBL_PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
