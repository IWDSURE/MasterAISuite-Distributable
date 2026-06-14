# HWR_PER_GBL_PRFL_PRFL_X

This cross reference (xref) table stores relationship between global profile and profile.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpergblprflprflx-16256.html#hwrpergblprflprflx-16256](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpergblprflprflx-16256.html#hwrpergblprflprflx-16256)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_GBL_PRFL_PRFL_X_PK | GBL_PRFL_ID, PRFL_ID, SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GLOBAL_PROFILE_ID | VARCHAR2 | 400 |  | Yes | The Id of the global profile from the HWR_PER_GBL_PRFL_B table. | Obsolete |
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | The Id of the global profile from the HWR_PER_GBL_PRFL_B table. |  |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | The Id for the person profile from the HWR_PER_PROFILE_B table. |  |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id for the source for the person profile from the HWR_PER_PROFILE_B table. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_PER_GBL_PRFL_PRFL_X_N1 | Non Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID |  |
| HWR_PER_GBL_PRFL_PRFL_X_U1 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID, PRFL_ID | Obsolete |
| HWR_PER_GBL_PRFL_PRFL_X_U2 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID, PRFL_ID, SOURCE_ID |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
