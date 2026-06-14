# PAY_PAYROLL_ACTIONS

This table contains general details of the execution of payroll processes, including their type and all parameters supplied to them.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollactions-6144.html#paypayrollactions-6144](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollactions-6144.html#paypayrollactions-6144)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAYROLL_ACTIONS_PK | PAYROLL_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_ACTION_ID | NUMBER |  | 18 | Yes | PAYROLL_ACTION_ID |
| ACTION_STATUS | VARCHAR2 | 1 |  | Yes | ACTION_STATUS |
| ACTION_TYPE | VARCHAR2 | 30 |  | Yes | ACTION_TYPE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 20 |  |  | Foreign key to FND_TERRITORIES. |
| ACTION_POPULATION_STATUS | VARCHAR2 | 1 |  | Yes | ACTION_POPULATION_STATUS |
| CURRENT_CHUNK_NUMBER | NUMBER |  | 18 |  | CURRENT_CHUNK_NUMBER |
| DISPLAY_RUN_NUMBER | NUMBER |  | 10 |  | DISPLAY_RUN_NUMBER |
| PAY_REQUEST_ID | NUMBER |  | 18 |  | PAY_REQUEST_ID |
| ACTION_SEQUENCE | NUMBER |  | 18 |  | ACTION_SEQUENCE |
| ACTION_PARAMETER_GROUP_ID | NUMBER |  | 18 |  | ACTION_PARAMETER_GROUP_ID |
| START_DATE | DATE |  |  |  | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| EFFECTIVE_DATE | DATE |  |  |  | EFFECTIVE_DATE |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| CONSOLIDATION_SET_ID | NUMBER |  | 18 |  | CONSOLIDATION_SET_ID |
| ELEMENT_SET_ID | NUMBER |  | 18 |  | ELEMENT_SET_ID |
| DATE_EARNED | DATE |  |  |  | DATE_EARNED |
| RUN_TYPE_ID | NUMBER |  | 18 |  | RUN_TYPE_ID |
| ASSIGNMENT_SET_ID | NUMBER |  | 18 |  | ASSIGNMENT_SET_ID |
| PAYMENT_TYPE_ID | NUMBER |  | 18 |  | PAYMENT_TYPE_ID |
| EARN_TIME_PERIOD_ID | NUMBER |  | 18 |  | EARN_TIME_PERIOD_ID |
| DEDN_TIME_PERIOD_ID | NUMBER |  | 18 |  | DEDN_TIME_PERIOD_ID |
| BATCH_PROCESS_MODE | VARCHAR2 | 30 |  |  | BATCH_PROCESS_MODE |
| LEGISLATIVE_PARAMETERS | VARCHAR2 | 2000 |  |  | LEGISLATIVE_PARAMETERS |
| RETRO_DEFINITION_ID | NUMBER |  | 18 |  | RETRO_DEFINITION_ID |
| FUTURE_PROCESS_MODE | VARCHAR2 | 30 |  |  | Payments future process mode |
| COSTING_PROCESS_MODE | VARCHAR2 | 30 |  |  | Costing future process mode |
| TARGET_PAYROLL_ACTION_ID | NUMBER |  | 18 |  | TARGET_PAYROLL_ACTION_ID |
| CREATOR_ID | NUMBER |  | 18 |  | Key of the Creating entity |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | The Creating Enitity |
| CURRENT_TASK | VARCHAR2 | 30 |  |  | CURRENT_TASK |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 |  | ORG_PAYMENT_METHOD_ID |
| PARENT_ORG_PAY_METHOD_ID | NUMBER |  | 18 |  | PARENT_ORG_PAY_METHOD_ID |
| START_CHEQUE_NUMBER | NUMBER |  | 18 |  | START_CHEQUE_NUMBER |
| END_CHEQUE_NUMBER | NUMBER |  | 18 |  | END_CHEQUE_NUMBER |
| OVERRIDING_DD_DATE | DATE |  |  |  | OVERRIDING_DD_DATE |
| REPORT_CATEGORY_ID | NUMBER |  | 18 |  | REPORT_CATEGORY_ID |
| CHEQUE_PROCEDURE | VARCHAR2 | 30 |  |  | CHEQUE_PROCEDURE |
| REPORT_FORMAT_MAPPING_ID | NUMBER |  | 18 |  | REPORT_FORMAT_MAPPING_ID |
| EFT_FILE_REFERENCE | VARCHAR2 | 30 |  |  | EFT_FILE_REFERENCE |
| EFT_EXPIRY_DATE | DATE |  |  |  | EFT_EXPIRY_DATE |
| BIP_JOB_ID | NUMBER |  | 18 |  | BIP_JOB_ID |
| INTERFACE_TYPE_ID | NUMBER |  | 18 |  | INTERFACE_TYPE_ID |
| PAYMENT_REASON | VARCHAR2 | 30 |  |  | PAYMENT_REASON |
| FILE_NAME | VARCHAR2 | 256 |  |  | The name of a file the process will use |
| PARAMETER1 | VARCHAR2 | 2300 |  |  | PARAMETER1 |
| PARAMETER2 | VARCHAR2 | 30 |  |  | PARAMETER2 |
| PARAMETER3 | VARCHAR2 | 30 |  |  | PARAMETER3 |
| PARAMETER4 | VARCHAR2 | 30 |  |  | PARAMETER4 |
| PARAMETER5 | VARCHAR2 | 30 |  |  | PARAMETER5 |
| PROCESS_EVENT_ID | NUMBER |  | 18 |  | Foreign key to Pay Process Events |
| EVENT_ACTION_ID | NUMBER |  | 18 |  | EVENT_ACTION_ID |
| PAY_PAYEE_TYPE | VARCHAR2 | 30 |  |  | Payee Type - Employee Or Third-Party |
| EXPEDITE_FLAG | VARCHAR2 | 30 |  |  | This indicates whether the Payroll Run is expedited. |
| EXPIRE_ID | NUMBER |  | 8 |  | EXPIRE_ID |
| PROCESS_PHASE | VARCHAR2 | 20 |  |  | PROCESS_PHASE |
| OVERRIDE_DATE | DATE |  |  |  | OVERRIDE_DATE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PAYROLL_ACTIONS_FK1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_PAYROLL_ACTIONS_FK5 | Non Unique | Default | PAYMENT_TYPE_ID |
| PAY_PAYROLL_ACTIONS_N10 | Non Unique | Default | REPORT_CATEGORY_ID, EFFECTIVE_DATE |
| PAY_PAYROLL_ACTIONS_N11 | Non Unique | Default | TARGET_PAYROLL_ACTION_ID |
| PAY_PAYROLL_ACTIONS_N12 | Non Unique | Default | EXPIRE_ID |
| PAY_PAYROLL_ACTIONS_N2 | Non Unique | Default | CONSOLIDATION_SET_ID, EFFECTIVE_DATE, PAYROLL_ID |
| PAY_PAYROLL_ACTIONS_N3 | Non Unique | Default | PAYROLL_ID, ACTION_TYPE, EFFECTIVE_DATE |
| PAY_PAYROLL_ACTIONS_N4 | Non Unique | Default | ORG_PAYMENT_METHOD_ID |
| PAY_PAYROLL_ACTIONS_N5 | Non Unique | Default | EFFECTIVE_DATE, ACTION_TYPE |
| PAY_PAYROLL_ACTIONS_N6 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_PAYROLL_ACTIONS_N7 | Non Unique | Default | PAY_REQUEST_ID |
| PAY_PAYROLL_ACTIONS_N8 | Non Unique | Default | EARN_TIME_PERIOD_ID |
| PAY_PAYROLL_ACTIONS_N9 | Non Unique | Default | DEDN_TIME_PERIOD_ID |
| PAY_PAYROLL_ACTIONS_PK | Unique | Default | PAYROLL_ACTION_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
