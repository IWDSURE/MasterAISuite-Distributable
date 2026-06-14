# PAY_FLOWS

this will be utilized in Payrollflow s

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflows-8725.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflows-8725.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOWS_PK | FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_ID | NUMBER |  | 18 | Yes | This column is the primary key of the table pay_flows. |
| MT_WITHOUT_SOA_FLAG | VARCHAR2 | 2 |  |  | This column contains the SOA flag value of the flow. |
| TASK_VERSIONING_ENABLED | VARCHAR2 | 2 |  |  | This column contains the task versioning enabled value of the flow. |
| BASE_FLOW_ID | NUMBER |  | 18 | Yes | This column contains the base flow id value of the flow. |
| BASE_FLOW_NAME | VARCHAR2 | 100 |  | Yes | This column contains the base flow name value of the flow. |
| DEFAULT_FLOW_FLAG | VARCHAR2 | 1 |  |  | This column contains the default flow flag value of the flow. |
| LDG_RQD_FLAG | VARCHAR2 | 1 |  | Yes | This column contains the ldg required flag value of the flow. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| FORMULA_ID | NUMBER |  | 18 |  | This column contains the formula id value of the flow. |
| START_SCH_TIME_DEF_ID | NUMBER |  | 18 |  | Time definition id which defaults the start schedule of the corresponding flow instance. |
| START_SCH_FORMULA_ID | NUMBER |  | 18 |  | A Formula Id which will be used to default the formulaId present to the user during flow submission |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CONNECTOR_TAG | VARCHAR2 | 250 |  |  | This column contains the connector tag value of the flow. |
| CONNECTOR_STATUS | VARCHAR2 | 10 |  |  | This column contains the connector status value of the flow. |
| FLOW_TYPE | VARCHAR2 | 100 |  |  | This column contains the flow type value of the flow. |
| TASK_TYPES | VARCHAR2 | 100 |  |  | This column contains the task type value of the flow. |
| OUTBOUND_ENABLED_FLAG | VARCHAR2 | 1 |  |  | This column contains the outbound enabled flag value of the flow. |
| TASK_COUNT | NUMBER |  | 18 |  | This column contains the task count value of the flow. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| IMPL_CLASS_CODE | VARCHAR2 | 10 |  |  | This column contains the impl class code value of the flow. |
| SETUP_RULES | VARCHAR2 | 100 |  |  | This column contains the setup rules value of the flow. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_FLOWS_N1 | Non Unique | Default | BASE_FLOW_ID |
| PAY_FLOWS_PK | Unique | Default | FLOW_ID, ORA_SEED_SET1 |
| PAY_FLOWS_PK1 | Unique | Default | FLOW_ID, ORA_SEED_SET2 |
| PAY_FLOWS_U1 | Unique | Default | BASE_FLOW_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_FLOWS_U11 | Unique | Default | BASE_FLOW_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
