# HWM_XFR_TRANS

A time record transferred to a consuming application

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrtrans-24856.html#hwmxfrtrans-24856](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrtrans-24856.html#hwmxfrtrans-24856)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_XFR_TRANS_PK | XFR_TRANS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFR_TRANS_ID | NUMBER |  | 18 | Yes | The primary key for the object being transferred. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| XFR_JOB_ID | NUMBER |  | 18 | Yes | The Transfer Job which is Transferring to the Time Consumer |
| XFR_TM_UNQ_REC_ID | NUMBER |  | 18 |  | XFR_TM_UNQ_REC_ID |
| XFR_ROW_STATUS | VARCHAR2 | 30 |  |  | XFR_ROW_STATUS |
| XFR_GRP_ID | NUMBER |  | 18 |  | XFR_GRP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TCSMRS_ID | NUMBER |  | 18 |  | Time Consumer ID related with XFR_JOB_ID |
| TM_REC_ID | NUMBER |  | 18 |  | TM_REC_ID |
| TM_REC_VERSION | NUMBER |  | 9 |  | TM_REC_VERSION |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | TM_REC_GRP_ID |
| TM_REC_GRP_VERSION | NUMBER |  | 9 |  | TM_REC_GRP_VERSION |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_XFR_TRANS_N1 | Non Unique | FUSION_TS_TX_DATA | XFR_JOB_ID, TM_REC_GRP_ID, TM_REC_GRP_VERSION |  |
| HWM_XFR_TRANS_N2 | Non Unique | Default | XFR_ROW_STATUS, TCSMRS_ID, TM_REC_ID, ENTERPRISE_ID |  |
| HWM_XFR_TRANS_N3 | Non Unique | Default | XFR_GRP_ID |  |
| HWM_XFR_TRANS_N4 | Non Unique | Default | XFR_TM_UNQ_REC_ID | Obsolete |
| HWM_XFR_TRANS_PK | Unique | FUSION_TS_TX_DATA | XFR_TRANS_ID |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
