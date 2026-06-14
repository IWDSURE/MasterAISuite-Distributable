# HWM_XFRS_UNQ_RECS

Contains Unique Records for Transfer

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrsunqrecs-13917.html#hwmxfrsunqrecs-13917](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrsunqrecs-13917.html#hwmxfrsunqrecs-13917)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_XFRS_UNQ_RECS_PK | XFR_TM_UNQ_REC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFR_TM_UNQ_REC_ID | NUMBER |  | 18 | Yes | XFR_TM_UNQ_REC_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_REC_ID | NUMBER |  | 18 |  | The Time Record Being Transferred to the Time Consumer |
| TM_REC_VERSION | NUMBER |  | 9 |  | The version of the Time Record being Transferred to the Time Consumer |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | TM_REC_GRP_ID |
| TM_REC_GRP_VERSION | NUMBER |  | 9 |  | TM_REC_GRP_VERSION |
| IN_USE_FLAG | VARCHAR2 | 20 |  |  | IN_USE_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_XFRS_UNQ_RECS_N1 | Non Unique | Default | TM_REC_GRP_ID, ENTERPRISE_ID |
| HWM_XFRS_UNQ_RECS_PK | Unique | FUSION_TS_TX_DATA | XFR_TM_UNQ_REC_ID |
| HWM_XFRS_UNQ_RECS_U1 | Unique | FUSION_TS_TX_DATA | TM_REC_ID, TM_REC_VERSION, ENTERPRISE_ID, TM_REC_GRP_ID, XFR_TM_UNQ_REC_ID |
| HWM_XFRS_UNQ_RECS_U2 | Unique | Default | TM_REC_ID, TM_REC_VERSION |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
