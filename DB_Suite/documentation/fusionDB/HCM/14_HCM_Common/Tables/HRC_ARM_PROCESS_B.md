# HRC_ARM_PROCESS_B

Approval model Table: This holds the process name mapped to each task available in the active composites and design time flags of whether various features like Rules Simulation, Archive, Bypass, Atomic transactions are supported by respective process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmprocessb-28096.html#hrcarmprocessb-28096](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmprocessb-28096.html#hrcarmprocessb-28096)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ARM_PROCESS_B_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| IS_TASK_CONFIG_SUPPORTED | VARCHAR2 | 20 |  |  | Flag to indicate if task config is supported |
| IS_COMMUNICATION_NTF_SUPPORTED | VARCHAR2 | 20 |  |  | Flag to indicate that communication notification is supported or not |
| USE_COMMUNICATION_APPROVAL | VARCHAR2 | 20 |  |  | Flag indicates whether to use HCM communication for approvals |
| IS_AI_COMMENT_SUPPORTED | VARCHAR2 | 10 |  |  | Design time flag whether the process supports AI comments feature or not |
| RESUBMIT_CALLBACK_CLASS | VARCHAR2 | 200 |  |  | The consumers can update the class in which a call back method will be written which is called at time of resubmit |
| IS_RULE_SIMULATION_SUPPORTED | VARCHAR2 | 10 |  |  | Design time flag whether the process supports simulation feature or not |
| ARCHIVE_PERIOD | VARCHAR2 | 50 |  |  | This column is used to store the Archival Period of the Process. |
| RULE_CONFIGURE_MODE | VARCHAR2 | 20 |  |  | Will contain values null/External/BpmWorklist to identify which is the rule UI to be opened |
| APPROVAL_OVERRIDE_SUPPORTED | VARCHAR2 | 10 |  |  | Design time flag whether the process supports administrator to provide override approval at any stage during the transaction life-cycle. |
| IS_TXN_FRAMEWORK_PROCESS | VARCHAR2 | 10 |  |  | Design time flag whether the process supports approvals by leveraging the transaction framework. |
| IS_COMMUNICATION_PROCESS | VARCHAR2 | 1 |  |  | Flag to indicate that process is specific to communication messages |
| CONTEXT_PARAM_FETCH_CALLBACK | VARCHAR2 | 200 |  |  | Used to fetch parameter context |
| RESOURCE_CONTEXT_SHORT_NAME | VARCHAR2 | 500 |  |  | This is FND Topology Module Short Name to get the context url of the Rest Service |
| REST_RESOURCE_KEY | VARCHAR2 | 60 |  |  | Represent the Column Attribute Name of the HRC_TXN_HEADER Table to pass the value as Primary Key to the Additional Rest Resource |
| ADDITIONAL_REST_RESOURCE | VARCHAR2 | 1000 |  |  | Represents the additional Rest Resource Name |
| CATEGORY_CODE | VARCHAR2 | 100 |  |  | Grouping of approval process based on specified category within the application family |
| SUBCATEGORY_CODE | VARCHAR2 | 100 |  |  | Grouping of approval process based on specified sub category within the application family and category combination. |
| PRODUCT_CODE | VARCHAR2 | 50 |  |  | Grouping of approval process based on specified product code. |
| FAMILY | VARCHAR2 | 100 |  | Yes | The Application family that owns the approval process. |
| COMPOSITE_ID | NUMBER |  | 18 | Yes | Foreign key to HRC_ARM_COMPOSITES |
| TASK_FILE_NAME | VARCHAR2 | 64 |  |  | Task file name associated to the parent process and available at the source |
| RULE_FILE_NAME | VARCHAR2 | 64 |  | Yes | Rule file name associated to the parent process and available at the source |
| ACTIVE | VARCHAR2 | 4 |  | Yes | Flag to identify if the process is active or inactive |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the process belongs.  
Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TXN_MODULE_IDENTIFIER | VARCHAR2 | 60 |  |  | The Module that sets up the transaction business data for the process. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BYPASS_SUPPORTED | VARCHAR2 | 10 |  |  | Design time flag whether the process supports bypassing approvals or not. |
| ASYNC_BYPASS_SUPPORTED | VARCHAR2 | 10 |  |  | Used to identifiy which flow supports Async Bypass |
| TXN_SUB_MODULE_IDENTIFIER | VARCHAR2 | 60 |  |  | The Sub Module that sets up the transaction business data for the process. |
| IS_PARALLEL_TXN_SUPPORTED | VARCHAR2 | 10 |  |  | Design time flag whether the process supports Parallel Transactions. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ARM_PROCESS_B_N1 | Non Unique | Default | UPPER("TXN_MODULE_IDENTIFIER") |
| HRC_ARM_PROCESS_B_PK | Unique | Default | PROCESS_ID, ORA_SEED_SET1 |
| HRC_ARM_PROCESS_B_PK1 | Unique | Default | PROCESS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
