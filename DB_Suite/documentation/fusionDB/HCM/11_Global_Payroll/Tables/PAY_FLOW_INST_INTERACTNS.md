# PAY_FLOW_INST_INTERACTNS

When the user selects and submits a Payroll Flow Pattern a Payroll Flow instance will be created.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowinstinteractns-30247.html#payflowinstinteractns-30247](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowinstinteractns-30247.html#payflowinstinteractns-30247)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_INST_INTERACTNS_PK | INST_INTERACT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INST_INTERACT_ID | NUMBER |  | 18 | Yes | INST_INTERACT_ID |
| INTERACTION_SOURCE | VARCHAR2 | 10 |  |  | INTERACTION_SOURCE |
| IGNORE_PREREQ_FLAG | VARCHAR2 | 1 |  |  | IGNORE_PREREQ_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FROM_FLOW_ID | NUMBER |  | 18 |  | FROM_FLOW_ID |
| FROM_FLOW_INSTANCE_ID | NUMBER |  | 18 |  | FROM_FLOW_INSTANCE_ID |
| FROM_FLOW_TASK_ID | NUMBER |  | 18 |  | FROM_FLOW_TASK_ID |
| TO_FLOW_ID | NUMBER |  | 18 |  | TO_FLOW_ID |
| TO_FLOW_INSTANCE_ID | NUMBER |  | 18 |  | TO_FLOW_INSTANCE_ID |
| TO_FLOW_TASK_ID | NUMBER |  | 18 |  | TO_FLOW_TASK_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| IMPACT_CALCULATION | VARCHAR2 | 1 |  | Yes | IMPACT_CALCULATION |
| TAG_VALUE | VARCHAR2 | 250 |  |  | TAG_VALUE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_INST_INTERACTNS_N1 | Non Unique | Default | FROM_FLOW_INSTANCE_ID |
| PAY_FLOW_INST_INTERACTNS_N2 | Non Unique | Default | TO_FLOW_INSTANCE_ID |
| PAY_FLOW_INST_INTERACTNS_N3 | Non Unique | Default | FROM_FLOW_TASK_ID |
| PAY_FLOW_INST_INTERACTNS_N4 | Non Unique | Default | TO_FLOW_TASK_ID |
| PAY_FLOW_INST_INTERACTNS_PK | Unique | Default | INST_INTERACT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
