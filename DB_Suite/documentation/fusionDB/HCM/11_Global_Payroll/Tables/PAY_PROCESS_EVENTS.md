# PAY_PROCESS_EVENTS

This table contains general details of the execution of payroll processes, including their type and all parameters supplied to them. It is also used to synchronize the parallelization of the payroll processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocessevents-30079.html#payprocessevents-30079](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocessevents-30079.html#payprocessevents-30079)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PROCESS_EVENTS_PK | PROCESS_EVENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_EVENT_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| BATCH_ID | NUMBER |  | 18 |  | BATCH_ID |
| BATCH_TYPE | VARCHAR2 | 32 |  |  | BATCH_TYPE |
| DATED_TABLE_ID | NUMBER |  | 18 | Yes | DATED_TABLE_ID |
| SURROGATE_KEY_ID | NUMBER |  |  | Yes | SURROGATE_KEY_ID |
| CHANGE_TYPE | VARCHAR2 | 20 |  | Yes | Type of change detected. |
| EFFECTIVE_DATE | DATE |  |  | Yes | Effective date of event. |
| CALCULATION_DATE | DATE |  |  | Yes | Date event was processed |
| OLD_VALUE | VARCHAR2 | 150 |  |  | OLD_VALUE |
| NEW_VALUE | VARCHAR2 | 150 |  |  | NEW_VALUE |
| ADDL_VALUE | VARCHAR2 | 150 |  |  | ADDL_VALUE |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| LEGISLATIVE_DATA_GROUP_ID | VARCHAR2 | 20 |  |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| DESCRIPTION | VARCHAR2 | 30 |  |  | Brief description of the event change |
| COLUMN_NAME | VARCHAR2 | 30 |  |  | COLUMN_NAME |
| EVENT_STATUS | VARCHAR2 | 30 |  |  | Is the Event Valid or Invalid. |
| TRANSACTION_ID | NUMBER |  | 18 |  | Foreign Key to HCM Events table. |
| QUALIFIER_VALUE | VARCHAR2 | 2000 |  |  | QUALIFIER_VALUE |
| SEC_QUALIFIER_VALUE | VARCHAR2 | 2000 |  |  | SEC_QUALIFIER_VALUE |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PROCESS_EVENTS_N1 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, EFFECTIVE_DATE, CHANGE_TYPE |
| PAY_PROCESS_EVENTS_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, CREATION_DATE, CHANGE_TYPE |
| PAY_PROCESS_EVENTS_N3 | Non Unique | Default | DATED_TABLE_ID, SURROGATE_KEY_ID |
| PAY_PROCESS_EVENTS_N4 | Non Unique | Default | TRANSACTION_ID |
| PAY_PROCESS_EVENTS_N5 | Non Unique | Default | BATCH_ID, BATCH_TYPE |
| PAY_PROCESS_EVENTS_PK | Unique | Default | PROCESS_EVENT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
