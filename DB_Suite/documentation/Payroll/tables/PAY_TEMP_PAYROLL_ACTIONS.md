# PAY_TEMP_PAYROLL_ACTIONS

This table contains general details of the execution of payroll processes, including their type and all parameters supplied to them.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemppayrollactions-16877.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemppayrollactions-16877.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TEMP_PAYROLL_ACTIONS_PK | PAYROLL_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | Primary Key Payroll Action Id |
| ACTION_STATUS | VARCHAR2 | 1 |  | Yes | Status of the Action |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | The Action Type to be processed |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 20 |  |  | Foreign key to FND_TERRITORIES. |
| ACTION_POPULATION_STATUS | VARCHAR2 | 1 |  | Yes | Status of the Population Phase |
| CURRENT_CHUNK_NUMBER | NUMBER |  | 18 |  | Chunk that is currently processing |
| DISPLAY_RUN_NUMBER | NUMBER |  | 10 |  | The Run Number to be used in the display |
| PAY_REQUEST_ID | NUMBER |  | 18 |  | Initial Request Id |
| ACTION_SEQUENCE | NUMBER |  | 18 |  | Internal Sequence Order |
| ACTION_PARAMETER_GROUP_ID | NUMBER |  | 18 |  | Parameter Group to be used on processing |
| START_DATE | DATE |  |  |  | Process Start Date |
| END_DATE | DATE |  |  |  | Process End Date |
| EFFECTIVE_DATE | DATE |  |  |  | Process Effective Date |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign Key to the Payroll |
| CONSOLIDATION_SET_ID | NUMBER |  | 18 |  | Foreign Key to the Consolidation Set |
| LEGISLATIVE_PARAMETERS | VARCHAR2 | 2000 |  |  | Generic Legislation Parameters list |
| TARGET_PAYROLL_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to the Payroll Action |
| CURRENT_TASK | VARCHAR2 | 30 |  |  | Current Task being performed by the process |
| PARAMETER1 | VARCHAR2 | 2300 |  |  | Generic Parameter 1 |
| PARAMETER2 | VARCHAR2 | 30 |  |  | Generic Parameter 2 |
| PARAMETER3 | VARCHAR2 | 30 |  |  | Generic Parameter 3 |
| PARAMETER4 | VARCHAR2 | 30 |  |  | Generic Parameter 4 |
| PARAMETER5 | VARCHAR2 | 30 |  |  | Generic Parameter 5 |
| PROCESS_EVENT_ID | NUMBER |  | 18 |  | Foreign key to Pay Process Events |
| EVENT_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to Event Actions |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TEMP_PAYROLL_ACTIONS_FK1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_TEMP_PAYROLL_ACTIONS_N11 | Non Unique | Default | TARGET_PAYROLL_ACTION_ID |
| PAY_TEMP_PAYROLL_ACTIONS_N2 | Non Unique | Default | CONSOLIDATION_SET_ID, EFFECTIVE_DATE, PAYROLL_ID |
| PAY_TEMP_PAYROLL_ACTIONS_N3 | Non Unique | Default | PAYROLL_ID, ACTION_TYPE, EFFECTIVE_DATE |
| PAY_TEMP_PAYROLL_ACTIONS_N5 | Non Unique | Default | EFFECTIVE_DATE, ACTION_TYPE |
| PAY_TEMP_PAYROLL_ACTIONS_N7 | Non Unique | Default | PAY_REQUEST_ID |
| PAY_TEMP_PAYROLL_ACTIONS_PK | Unique | Default | PAYROLL_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
