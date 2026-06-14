# HWM_XFR_GRP

Time record groups transferred by a particular instance, or job, of a transfer process.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrgrp-25903.html#hwmxfrgrp-25903](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrgrp-25903.html#hwmxfrgrp-25903)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_XFR_GRP_PK | XFR_GRP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFR_GRP_ID | NUMBER |  | 18 | Yes | XFR_GRP_ID |
| RESOURCE_ID | NUMBER |  | 18 |  | RESOURCE ID |
| XFR_GRP_STATUS | VARCHAR2 | 30 |  |  | XFR_GRP_STATUS |
| TCSMRS_ID | NUMBER |  | 18 |  | TCSMRS_ID |
| XFR_JOB_ID | NUMBER |  | 18 |  | XFR_JOB_ID |
| TM_REC_GRP_ID | NUMBER |  | 18 |  | TM_REC_GRP_ID |
| TM_REC_GRP_VERSION | NUMBER |  | 9 |  | TM_REC_GRP_VERSION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| GRP_REC_COUNT | NUMBER |  |  |  | GRP_REC_COUNT |
| BATCH_NUMBER | NUMBER |  | 18 |  | The batch In which this group will be transferred. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_XFR_GRP_N1 | Non Unique | Default | TM_REC_GRP_ID, XFR_JOB_ID, ENTERPRISE_ID |
| HWM_XFR_GRP_N2 | Non Unique | Default | XFR_JOB_ID, BATCH_NUMBER, ENTERPRISE_ID |
| HWM_XFR_GRP_N3 | Non Unique | Default | XFR_GRP_STATUS, TCSMRS_ID, TM_REC_GRP_ID |
| HWM_XFR_GRP_PK | Unique | FUSION_TS_TX_DATA | XFR_GRP_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
