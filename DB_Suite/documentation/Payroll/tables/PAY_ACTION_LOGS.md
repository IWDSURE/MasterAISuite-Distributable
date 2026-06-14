# PAY_ACTION_LOGS

This table holds the Log File details of the ADF/in-memory processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionlogs-6007.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionlogs-6007.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_LOGS_PK | ACTION_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_LOG_ID | NUMBER |  | 18 | Yes | Primary Key |
| NAME | VARCHAR2 | 30 |  | Yes | Name of the log file |
| STATUS | VARCHAR2 | 5 |  | Yes | Status of the log. |
| LOG_TYPE | VARCHAR2 | 30 |  |  | Type of Log File |
| DAEMON_ACTION_ID | NUMBER |  | 18 |  | Daemon Action that created the log |
| PARENT_DAEMON_ACTION_ID | NUMBER |  | 18 |  | Parent Daemon Action that created this log. |
| CREATOR_ID | NUMBER |  | 18 |  | Creating table Id |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | Identifies the Creator Id |
| SOURCE_ID | NUMBER |  | 18 |  | Source of the Log |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source of the Log. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ACTION_LOGS_N1 | Non Unique | Default | CREATION_DATE |
| PAY_ACTION_LOGS_N2 | Non Unique | Default | CREATOR_ID, CREATOR_TYPE |
| PAY_ACTION_LOGS_N3 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_ACTION_LOGS_N4 | Non Unique | Default | DAEMON_ACTION_ID |
| PAY_ACTION_LOGS_N5 | Non Unique | Default | PARENT_DAEMON_ACTION_ID |
| PAY_ACTION_LOGS_PK | Unique | Default | ACTION_LOG_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
