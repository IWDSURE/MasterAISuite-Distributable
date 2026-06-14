# HWM_XFR_JOB

Instance of a transfer of time from workforce management to a time consuming application

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrjob-20594.html#hwmxfrjob-20594](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrjob-20594.html#hwmxfrjob-20594)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_XFR_JOB_PK | XFR_JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| XFR_JOB_ID | NUMBER |  | 18 | Yes | XFR_JOB_ID |
| BU_LDG_ID | NUMBER |  | 18 |  | BU_LDG_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TCSMRS_ID | NUMBER |  | 18 |  | TCSMRS_ID |
| XFR_START_TIME | TIMESTAMP |  |  |  | XFR_START_TIME |
| REC_START_TIME | TIMESTAMP |  |  |  | REC_START_TIME |
| XFR_STATUS | VARCHAR2 | 30 |  |  | XFR_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 |  | person id of whom ran this transfer |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_XFR_JOB_N1 | Non Unique | Default | XFR_STATUS, TRUNC("XFR_START_TIME") |
| HWM_XFR_JOB_PK | Unique | Default | XFR_JOB_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
