# PAY_CHECKLIST_INSTANCES

Table captures the checklist instances created for the flow instance

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychecklistinstances-14466.html#paychecklistinstances-14466](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychecklistinstances-14466.html#paychecklistinstances-14466)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CHECKLIST_INSTANCES_PK | CHECKLIST_INSTANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_INSTANCE_ID | NUMBER |  | 18 | Yes | CHECKLIST_INSTANCE_ID |
| APPROVER | VARCHAR2 | 100 |  |  | APPROVER |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BASE_CHECKLIST_ID | NUMBER |  | 18 | Yes | BASE_CHECKLIST_ID |
| FLOW_INSTANCE_ID | NUMBER |  | 18 | Yes | FLOW_INSTANCE_ID |
| FLOW_TASK_INSTANCE_ID | NUMBER |  | 18 |  | FLOW_TASK_INSTANCE_ID |
| OWNER_TYPE | VARCHAR2 | 18 |  |  | OWNER_TYPE |
| OWNER_ID | VARCHAR2 | 4000 |  |  | OWNER_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| PROGRESS | NUMBER |  | 9 |  | PROGRESS |
| DUE_DATE | DATE |  |  |  | DUE_DATE |
| COMPLETION_DATE | DATE |  |  |  | COMPLETION_DATE |
| START_DATE | DATE |  |  |  | START_DATE |
| PRNT_CHKLST_INST_ID | NUMBER |  | 18 |  | PRNT_CHKLST_INST_ID |
| FREEZE_FLAG | VARCHAR2 | 1 |  |  | FREEZE_FLAG |
| WORKLIST_ID | VARCHAR2 | 80 |  |  | WORKLIST_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_CHECKLIST_INSTANCES_N1 | Non Unique | Default | FLOW_INSTANCE_ID |
| PAY_CHECKLIST_INSTANCES_N2 | Non Unique | Default | BASE_CHECKLIST_ID |
| PAY_CHECKLIST_INSTANCES_N3 | Non Unique | Default | FLOW_TASK_INSTANCE_ID |
| PAY_CHECKLIST_INSTANCES_N4 | Non Unique | Default | STATUS |
| PAY_CHECKLIST_INSTANCES_N5 | Non Unique | Default | PRNT_CHKLST_INST_ID |
| PAY_CHECKLIST_INSTANCES_PK | Unique | Default | CHECKLIST_INSTANCE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
