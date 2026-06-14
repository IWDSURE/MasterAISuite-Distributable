# HWR_MENTOR_B

This Table stores the details of the Mentor

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmentorb-16156.html#hwrmentorb-16156](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmentorb-16156.html#hwrmentorb-16156)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_MENTOR_B_PK | MENTOR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MENTOR_ID | NUMBER |  | 18 | Yes | This stores the Unique Identifier of the Mentor |
| MENTOR_GBL_PRFL_ID | NUMBER |  | 18 | Yes | This stores the Mentor's Global Profile Id |
| MENTOR_FUS_PRFL_ID | NUMBER |  | 18 |  | This stores the Mentor's Fusion Profile Id |
| MENTOREE_GBL_PRFL_ID | NUMBER |  | 18 | Yes | This stores the mentoree global profile Id. |
| MENTOREE_FUS_PRFL_ID | NUMBER |  | 18 |  | This stores the mentoree Fusion profile Id. |
| MENTORSHIP_STATUS | VARCHAR2 | 30 |  |  | This is current staus of mentor. |
| METRIC_NAME | VARCHAR2 | 512 |  |  | This store mentor's  metric name. This could be one or multiple. |
| METRIC_TYPE | VARCHAR2 | 30 |  |  | This stores mentor's metric type. |
| MENTOR_MENTOREE_MESSAGES | VARCHAR2 | 4000 |  |  | This will store the communication between the mentor and mentee. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_MENTOR_B_N1 | Non Unique | FUSION_TS_TX_DATA | MENTOR_GBL_PRFL_ID |
| HWR_MENTOR_B_N2 | Non Unique | FUSION_TS_TX_DATA | MENTOREE_GBL_PRFL_ID |
| HWR_MENTOR_B_N3 | Non Unique | FUSION_TS_TX_DATA | MENTOR_FUS_PRFL_ID |
| HWR_MENTOR_B_N4 | Non Unique | FUSION_TS_TX_DATA | MENTOREE_FUS_PRFL_ID |
| HWR_MENTOR_B_U1 | Unique | FUSION_TS_TX_DATA | MENTOR_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
