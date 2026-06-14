# PAY_ANA_PAYROLL_ACTIONS

This table contains payroll actions analytics transactional data.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** pay_ana_payroll_actions

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payanapayrollactions-30462.html#payanapayrollactions-30462](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payanapayrollactions-30462.html#payanapayrollactions-30462)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ANA_PAYROLL_ACTIONS_PK | PAYROLL_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| PROCESS_DATE | DATE |  |  | Yes | PROCESS_DATE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | LEGISLATIVE_DATA_GROUP_ID |
| CATEGORY | VARCHAR2 | 32 |  | Yes | CATEGORY |
| PAYROLL_ID | NUMBER |  | 18 | Yes | PAYROLL_ID |
| TIME_PERIOD_ID | NUMBER |  | 18 | Yes | TIME_PERIOD_ID |
| DEDN_TIME_PERIOD_ID | NUMBER |  | 18 |  | DEDN_TIME_PERIOD_ID |
| FLOW_INSTANCE_ID | NUMBER |  | 18 |  | FLOW_INSTANCE_ID |
| FLOW_INSTANCE_NAME | VARCHAR2 | 200 |  |  | FLOW_INSTANCE_NAME |
| BASE_FLOW_ID | NUMBER |  | 18 |  | BASE_FLOW_ID |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID |
| TASK_ID | NUMBER |  | 18 |  | TASK_ID |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | ACTION_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ANA_PAYROLL_ACTIONS_PK | Unique | Default | PAYROLL_ACTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
