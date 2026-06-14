# PAY_GENERIC_ANA_DATA

This table contains pay generic analytics transaction data.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericanadata-22056.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericanadata-22056.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GENERIC_ANA_DATA_PK | PAY_GEN_ANA_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_GEN_ANA_DATA_ID | NUMBER |  | 18 | Yes | System-generated primary key column. Payroll Generic Analytics Data Id. |
| PRIMARY_ID | NUMBER |  | 18 |  | Primary Id, identify partent Payroll Generic Analytics Data Id. |
| BASE_GEN_ANA_TYPE | VARCHAR2 | 128 |  | Yes | Base Generic Analytics Type, Identify payroll, prepayment, payment, payslip and costing. |
| PAYROLL_ACTION_ID | NUMBER |  | 18 |  | Payroll Action Id, Foreign key to pay_payroll_actions table. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group Id. Foreign key to PER_LEGISLATIVE_DATA_GROUPS_vl table. |
| LEGISLATION_CODE | VARCHAR2 | 20 |  |  | Legislation Code. Identify legislation code. |
| PAYROLL_ID | NUMBER |  | 18 |  | Payroll Id, Foreign key to PAY_ALL_PAYROLLS_F table. |
| ACTION_TYPE | VARCHAR2 | 64 |  |  | Action Type, Identify payroll run, prepayment, payment.. |
| FLOW_INSTANCE_ID | NUMBER |  | 18 |  | Flow Instance Id, Foreign key to pay_flow_instances table. |
| BASE_FLOW_ID | NUMBER |  | 18 |  | Base Flow Id. Foreign key to pay_flows table. |
| PERIOD_ID | NUMBER |  | 18 |  | Period Id, Foreign key to HR person table. |
| PERIOD_START_DATE | DATE |  |  |  | PERIOD_START_DATE. Period Start Date in pay_period table |
| PERIOD_END_DATE | DATE |  |  |  | PERIOD_END_DATE. Period End Date in pay_period table |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE, Effective Date in pay_payroll_actions table |
| CONSOLIDATION_SET_ID | NUMBER |  | 18 |  | CONSOLIDATION_SET_ID, Consolidation Set Id in pay_payroll_actions table |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID, Run Type Id in pay_payroll_actions table |
| PARENT_ACTION_ID | NUMBER |  | 18 |  | Parent Payroll Action Id, identify parent payroll_action_id |
| NUMBER1 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER2 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER3 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER4 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER5 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER6 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER7 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER8 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER9 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER10 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER11 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER12 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER13 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER14 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER15 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER16 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER17 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER18 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER19 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| NUMBER20 | NUMBER |  | 24 |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA1 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA2 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA3 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA4 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA5 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA6 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA7 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA8 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA9 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA10 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA11 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA12 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA13 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA14 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA15 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA16 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA17 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA18 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA19 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATA20 | VARCHAR2 | 512 |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATE1 | DATE |  |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATE2 | DATE |  |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATE3 | DATE |  |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATE4 | DATE |  |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| DATE5 | DATE |  |  |  | Oracle internal use only, Flex field used by payroll generic analytics. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_GENERIC_ANA_DATA_N1 | Non Unique | Default | BASE_GEN_ANA_TYPE, PAYROLL_ACTION_ID |
| PAY_GENERIC_ANA_DATA_N2 | Non Unique | Default | PRIMARY_ID |
| PAY_GENERIC_ANA_DATA_N3 | Non Unique | Default | PAYROLL_ID, PERIOD_ID |
| PAY_GENERIC_ANA_DATA_N4 | Non Unique | Default | PARENT_ACTION_ID |
| PAY_GENERIC_ANA_DATA_PK | Unique | Default | PAY_GEN_ANA_DATA_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
