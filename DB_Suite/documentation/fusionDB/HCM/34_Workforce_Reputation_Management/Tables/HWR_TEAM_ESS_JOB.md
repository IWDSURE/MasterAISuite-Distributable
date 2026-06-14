# HWR_TEAM_ESS_JOB

The HWR Team Ess Job run details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamessjob-30804.html#hwrteamessjob-30804](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamessjob-30804.html#hwrteamessjob-30804)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_TEAM_ESS_JOB_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 19 | Yes | This field contains autoincremented JOB_ID from sequence |
| JOB_NAME | VARCHAR2 | 255 |  | Yes | This field contains Ess JOB_NAME |
| LOG | CLOB |  |  |  | This field contains LOG fo job run |
| STATUS | VARCHAR2 | 50 |  |  | This field contains STATUS of job run |
| LAST_RUN_DATE | TIMESTAMP |  |  |  | This field contains  LAST successful RUN_DATE |
| SCHEDULE_INTERVAL | NUMBER |  | 18 |  | This field contains  SCHEDULE_INTERVAL of job |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_ESS_JOB_U1 | Unique | FUSION_TS_TX_DATA | JOB_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
