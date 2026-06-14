# HWR_RECOGN_GBL_PRFL_X

This cross reference (xref) table stores relationship between global profile and recognition.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecogngblprflx-17306.html#hwrrecogngblprflx-17306](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecogngblprflx-17306.html#hwrrecogngblprflx-17306)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RECOGN_GBL_PRFL_X_PK | RECOGNITION_ID, GBL_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOGNITION_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the recognition table. |
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | The Id of the global profile which has the recognition. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_RECOGN_GBL_PRFL_X_N1 | Non Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID |
| HWR_RECOGN_GBL_PRFL_X_U1 | Unique | FUSION_TS_TX_DATA | RECOGNITION_ID, GBL_PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
