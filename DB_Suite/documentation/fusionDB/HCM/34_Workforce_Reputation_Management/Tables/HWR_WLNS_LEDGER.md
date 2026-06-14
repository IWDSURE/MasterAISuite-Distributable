# HWR_WLNS_LEDGER

The wellness ledger table stores wellness ledger summary information.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsledger-24446.html#hwrwlnsledger-24446](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsledger-24446.html#hwrwlnsledger-24446)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_LEDGER_PK | USER_ID, SUMMARY_DATE |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| USER_ID | VARCHAR2 | 500 | Yes | This is the user Id of the user that has the summary. |
| SUMMARY_DATE | DATE |  | Yes | This is the date of the summary information. |
| REVENUE_PER_HOUR | NUMBER |  |  | This is the revenue per hour of the summary. |
| HEALTH_CARE_COST | NUMBER |  |  | This is the health care cost of the summary. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_LEDGER_U1 | Unique | FUSION_TS_TX_DATA | USER_ID, SUMMARY_DATE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
