# HWR_WLNS_FIN_SUM

The wellness financial data table stores wellness quarterly financial data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsfinsum-30350.html#hwrwlnsfinsum-30350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsfinsum-30350.html#hwrwlnsfinsum-30350)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_FIN_SUM_PK | YEAR, QUARTER |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| YEAR | NUMBER |  | 18 | Yes | This is the year of the wellness financial data. |
| QUARTER | NUMBER |  | 18 | Yes | This is the quarter of the wellness financial data. |
| REVENUE_PER_HOUR | NUMBER |  |  |  | This is the revenue per hour of the wellness financial data. |
| HEALTH_CARE_COST | NUMBER |  |  |  | This is the health care cost of the wellness financial data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_FIN_SUM_U1 | Unique | FUSION_TS_TX_DATA | YEAR, QUARTER |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
