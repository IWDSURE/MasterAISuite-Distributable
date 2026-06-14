# HWR_TEAM_OSN_JOBS

The HWR Team osn jobs run details are stored in this table

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamosnjobs-30302.html#hwrteamosnjobs-30302](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrteamosnjobs-30302.html#hwrteamosnjobs-30302)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_TEAM_OSN_JOBS_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | Indicates the identifier associated to the row |
| JOB_NAME | VARCHAR2 | 4000 |  |  | job name |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | error message |
| STATUS | VARCHAR2 | 50 |  |  | stores the status of the job |
| JOB_TYPE | VARCHAR2 | 50 |  |  | job type |
| SOURCE_OBJECT_ID | VARCHAR2 | 4000 |  |  | stores the external id that is sent to osn |
| LAST_RUN_DATE | TIMESTAMP |  |  |  | last run date |
| SCHEDULE_INTERVAL | NUMBER |  | 18 |  | schedule interval |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RESULT | VARCHAR2 | 4000 |  |  | stores result of the job |
| OSN_ATTR1 | VARCHAR2 | 4000 |  |  | additional column to store varchar datatype |
| OSN_ATTR2 | VARCHAR2 | 4000 |  |  | additional column to store varchar datatype |
| OSN_ATTR3 | TIMESTAMP |  |  |  | additional column to store timestamp datatype |
| OSN_ATTR4 | TIMESTAMP |  |  |  | additional column to store timestamp datatype |
| OSN_ATTR5 | NUMBER |  | 18 |  | additional column to store number datatype |
| OSN_ATTR6 | NUMBER |  | 18 |  | additional column to store number datatype |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_TEAM_OSN_JOBS_U1 | Unique | FUSION_TS_TX_DATA | JOB_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
