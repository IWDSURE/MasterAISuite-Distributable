# PAY_DAEMON_ACTIONS

Implements the queue of actions to be processed by the Daemon process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydaemonactions-21630.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydaemonactions-21630.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DAEMON_ACTIONS_PK | DAEMON_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DAEMON_ACTION_ID | NUMBER |  | 18 | Yes | Unique identifier of the action. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of the processed object. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of the processed object. |
| PRIORITY | NUMBER |  | 10 | Yes | Processing priority. |
| ACTION_START_DATE | DATE |  |  | Yes | Date and time that the action should be considered for processing. |
| DAEMON_TYPE | VARCHAR2 | 30 |  | Yes | Type of the daemon performing the action. |
| JAVA_ACTION | VARCHAR2 | 256 |  | Yes | Action to be performed. |
| PARENT_DAEMON_ACTION_ID | NUMBER |  | 18 |  | Parent Daemon Action that created this action. |
| ALLOCATED_THREAD | NUMBER |  | 10 |  | Thread Allocated to process Action |
| RETRY_COUNT | NUMBER |  | 2 |  | Retry Count |
| PARAMETER1 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER2 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER3 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER4 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER5 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER6 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER7 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER8 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER9 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| PARAMETER10 | VARCHAR2 | 30 |  |  | Additional parameter for the action. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_STATUS | VARCHAR2 | 30 |  | Yes | Processing status of the action. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_DAEMON_ACTIONS_N1 | Non Unique | Default | PROCESS_STATUS, ACTION_START_DATE, DAEMON_TYPE |
| PAY_DAEMON_ACTIONS_N2 | Non Unique | Default | JAVA_ACTION, PROCESS_STATUS, DAEMON_TYPE |
| PAY_DAEMON_ACTIONS_N3 | Non Unique | Default | PRIORITY, ACTION_START_DATE |
| PAY_DAEMON_ACTIONS_N4 | Non Unique | Default | ALLOCATED_THREAD, PRIORITY, ACTION_START_DATE |
| PAY_DAEMON_ACTIONS_PK | Unique | Default | DAEMON_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
