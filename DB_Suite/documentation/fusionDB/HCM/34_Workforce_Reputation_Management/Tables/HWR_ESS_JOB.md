# HWR_ESS_JOB

This is the table to store the scheduled ESS job info

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressjob-28295.html#hwressjob-28295](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwressjob-28295.html#hwressjob-28295)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ESS_JOB_PK | JOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_ID | NUMBER |  | 18 | Yes | This is the primary key for the ESS job table. |
| JOB_NAME | VARCHAR2 | 255 |  | Yes | This is the name of the ess job. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_ATTR_1 | VARCHAR2 | 100 |  |  | JOB_ATTR_1. This is the extra attribute in case if needed. |
| JOB_ATTR_2 | VARCHAR2 | 100 |  |  | JOB_ATTR_2. This is the extra attribute in case if needed. |
| JOB_ATTR_3 | VARCHAR2 | 100 |  |  | JOB_ATTR_3. This is the extra attribute in case if needed. |
| JOB_ATTR_4 | VARCHAR2 | 100 |  |  | JOB_ATTR_4. This is the extra attribute in case if needed. |
| JOB_ATTR_5 | VARCHAR2 | 100 |  |  | JOB_ATTR_5. This is the extra attribute in case if needed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ESS_JOB_U1 | Unique | Default | JOB_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
