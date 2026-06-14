# HWR_WLNS_POINTS_REPORT

This table stores the wellness report data

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnspointsreport-6771.html#hwrwlnspointsreport-6771](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnspointsreport-6771.html#hwrwlnspointsreport-6771)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_POINTS_REPORT_PK | RPT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RPT_ID | NUMBER |  | 18 | Yes | This is the primary key for the Wellness points report table |
| RPT_DATE | TIMESTAMP |  |  | Yes | This column contains the wellness points report date |
| POINTS | NUMBER |  | 18 | Yes | This column contains the wellness points for the user |
| USER_ID | VARCHAR2 | 64 |  | Yes | This column contains the wellness points for the User |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_POINTS_REPORT_N1 | Non Unique | FUSION_TS_TX_DATA | RPT_DATE |
| HWR_WLNS_POINTS_REPORT_U1 | Unique | FUSION_TS_TX_DATA | RPT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
