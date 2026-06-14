# HRA_PROCESS_STEP_ALERTS

This table stores the alerts that need to be raised for each step in the Performance Review process

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraprocessstepalerts-22463.html#hraprocessstepalerts-22463](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraprocessstepalerts-22463.html#hraprocessstepalerts-22463)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_PROCESS_STEP_ALERTS_PK | PROCESS_STEP_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PROCESS_STEP_ID | NUMBER |  | 18 | Yes | Indicates the id of the process flow step |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| TEMPLATE_DEFN_ID | NUMBER |  | 18 | Yes | Foreign key of Template Definition |  |
| STEP_CODE | VARCHAR2 | 30 |  | Yes | Stores the code for the step. This indicates the step. |  |
| STANDARD_ALERT_DAYS | NUMBER |  | 18 | Yes | Indicates the number of days before the due date for the step to alert the user that the task is due for that step. The nature of this alert is a standard alert. |  |
| CRITICAL_ALERT_DAYS | NUMBER |  | 18 | Yes | Indicates the number of days before the due date for the step to alert the user that the task is due for that step. The nature of this alert is a critical alert. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| STANDARD_ALERT_DAILY_FLAG | VARCHAR2 | 30 |  |  | Flag indicating whether worker and/or manager receives standard alerts daily. |  |
| CRITICAL_ALERT_DAILY_FLAG | VARCHAR2 | 30 |  |  | Flag indicating whether worker and/or manager receives critical alerts daily. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_PROCESS_STEP_ALERTS_N1 | Non Unique | Default | TEMPLATE_DEFN_ID |
| HRA_PROCESS_STEP_ALERTS_PK | Unique | Default | PROCESS_STEP_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
