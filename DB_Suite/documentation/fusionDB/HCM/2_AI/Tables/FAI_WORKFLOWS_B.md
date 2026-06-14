# FAI_WORKFLOWS_B

This table stores the workflow information.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowsb-22001.html#faiworkflowsb-22001](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiworkflowsb-22001.html#faiworkflowsb-22001)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_WORKFLOWS_B_PK | WORKFLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORKFLOW_ID | NUMBER |  | 18 | Yes | Uniquely identifies the workflow |
| VERSION | NUMBER |  | 9 | Yes | This column specifies the workflow version. |
| SEEDED_FLAG | VARCHAR2 | 1 |  | Yes | This column differentiates seeded data from customer created. |
| SOURCE_WORKFLOW_ID | NUMBER |  | 18 |  | Identifies parent workflow, if any |
| USE_CASE_ID | VARCHAR2 | 100 |  | Yes | Identify usecase of the workflow |
| WORKFLOW_CODE | VARCHAR2 | 200 |  | Yes | Text identifier of the workflow |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Workflow. |
| OWNER_NAME | VARCHAR2 | 200 |  |  | This column identifies the owner of the workflow. |
| STATUS | VARCHAR2 | 32 |  | Yes | This column provides status of the workflow. |
| ARCHITECTURE | VARCHAR2 | 200 |  | Yes | Architecture can be hierarchical, group, sequential, etc. |
| ACCESS_MODIFIER | VARCHAR2 | 200 |  | Yes | Access modifier of the workflow |
| SPECIFICATION | CLOB |  |  |  | JSON specification for the workflow |
| FAMILY | VARCHAR2 | 80 |  |  | Product family of the supported business object. |
| PRODUCT | VARCHAR2 | 100 |  |  | Product of the supported business object. |
| HIDDEN_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the workflow is visible or not. |
| START_QUESTION_1 | VARCHAR2 | 120 |  |  | Slot number one for start question. |
| START_QUESTION_2 | VARCHAR2 | 120 |  |  | Slot number two for start question. |
| START_QUESTION_3 | VARCHAR2 | 120 |  |  | Slot number three for start question. |
| START_QUESTION_4 | VARCHAR2 | 120 |  |  | Slot number four for start question. |
| START_QUESTION_5 | VARCHAR2 | 120 |  |  | Slot number five for start question. |
| FOLLOW_UP_PROMPT_ENABLED | VARCHAR2 | 1 |  | Yes | Whether follow up prompt is enabled. |
| FOLLOW_UP_PROMPT | CLOB |  |  |  | This column stores the follow up prompt. |
| MODEL_CONFIG_ID | NUMBER |  | 18 |  | Reference to a LLM model configuration. Foreign key to FAI_MODEL_CONFIGS table. |
| MAX_INTERACTIONS | NUMBER |  | 4 |  | Maximum number of interactions with LLM engine. |
| START_AGENT_ID | NUMBER |  | 18 |  | Start Agent in the associated Agent grapgh. |
| INTERNAL_NAME | VARCHAR2 | 200 |  |  | This column represents the system name of the Workflow. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the Workflow. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CUSTOM_FLAG | VARCHAR2 | 1 |  |  | Identifies if customizations have been made to the workflow or not |
| SOURCE_WORKFLOW_CODE | VARCHAR2 | 200 |  |  | Identifies parent workflow code, if any |
| IS_TEMPLATE | VARCHAR2 | 1 |  |  | Identifies if the workflow is a template or not |
| EMAIL_CONFIG_CODE | VARCHAR2 | 100 |  |  | Stores the email account associated with the workflow |
| JOB_REQUEST_ID | NUMBER |  | 18 |  | Stores the batch job request identifier |
| IS_AI_APPS_COMPATIBLE | VARCHAR2 | 1 |  |  | Identifies whether the workflow is compatible with AI applications |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_WORKFLOWS_B_N1 | Non Unique | Default | MODEL_CONFIG_ID |
| FAI_WORKFLOWS_B_N2 | Non Unique | Default | START_AGENT_ID |
| FAI_WORKFLOWS_B_U1 | Unique | Default | WORKFLOW_ID, ORA_SEED_SET1 |
| FAI_WORKFLOWS_B_U11 | Unique | Default | WORKFLOW_ID, ORA_SEED_SET2 |
| FAI_WORKFLOWS_B_U2 | Unique | Default | WORKFLOW_CODE, VERSION, STATUS, ORA_SEED_SET1 |
| FAI_WORKFLOWS_B_U21 | Unique | Default | WORKFLOW_CODE, VERSION, STATUS, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
