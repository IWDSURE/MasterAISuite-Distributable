# PAY_EVENT_TEMP_PROC_ACTIONS

This table is a denomalisation of the Actions and Events that are to be considered in the Event process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventtempprocactions-7546.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventtempprocactions-7546.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_TEMP_PROC_ACTIO_PK | EVENT_TEMP_PROC_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_TEMP_PROC_ACTION_ID | NUMBER |  | 18 | Yes | EVENT_TEMP_PROC_ACTION_ID |
| PROCESS_EVENT_ID | NUMBER |  | 18 | Yes | Foreign Key the Pay Process Events |
| EVENT_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to Pay Event Groups |
| DATETRACKED_EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_DATETRACKED_EVENTS |
| EVENT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_EVENT_ACTIONS_F |
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_EVENT_TEMP_PROC_ACTIONS_PK | Unique | Default | EVENT_TEMP_PROC_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
