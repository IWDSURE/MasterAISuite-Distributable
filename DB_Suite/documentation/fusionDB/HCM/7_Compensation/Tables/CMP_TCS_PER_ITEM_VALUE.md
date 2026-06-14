# CMP_TCS_PER_ITEM_VALUE

Statement Table that stores the item values.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperitemvalue-19055.html#cmptcsperitemvalue-19055](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperitemvalue-19055.html#cmptcsperitemvalue-19055)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_PER_ITEM_VALUE_PK | PER_ITEM_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ITEM_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| STMT_PERD_ID | NUMBER |  | 18 |  | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| PER_PERD_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_PER_PERD |
| PER_PERD_STMT_ID | NUMBER |  | 18 | Yes | Foreign key to CMP_TCS_PER_PERD_STMT |
| ITEM_ID | NUMBER |  | 18 |  | ITEM_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| DISPLAY_DATE | DATE |  |  |  | The Display Date will be set to either the Start Date or the End Date based on Compensation Item Source |
| TEXT_VALUE | VARCHAR2 | 2000 |  |  | If the data type is text then value for the comp item is stored |
| NUM_VALUE | NUMBER |  |  |  | If the data types are currency or number then value for the comp item is stored |
| DATE_VALUE | DATE |  |  |  | If the data type is date then value for the comp item is stored |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| NNMNTRY_UOM | VARCHAR2 | 30 |  |  | NNMNTRY_UOM |
| ROUNDING_CD | VARCHAR2 | 30 |  |  | ROUNDING_CD |
| ESTIMATED_FLAG | VARCHAR2 | 1 |  |  | ESTIMATED_FLAG |
| SOURCE_FROM_DATE | DATE |  |  |  | From date of the value |
| SOURCE_TO_DATE | DATE |  |  |  | To date of the value |
| SOURCE_CD | VARCHAR2 | 30 |  |  | Indicates the type of source for the Compensation item |
| SOURCE_KEY | NUMBER |  | 18 |  | It is the key for the source table which is identified by the Source Code |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_ITEM_VALUE_N1 | Non Unique | Default | ITEM_ID, PER_PERD_ID, LEGAL_ENTITY_ID |
| CMP_TCS_PER_ITEM_VALUE_N2 | Non Unique | Default | PER_PERD_ID, ITEM_ID, PERSON_ID |
| CMP_TCS_PER_ITEM_VALUE_N3 | Non Unique | Default | PER_PERD_STMT_ID, ITEM_ID |
| CMP_TCS_PER_ITEM_VALUE_N4 | Non Unique | Default | PERD_RUN_ID, PERSON_ID, ITEM_ID |
| CMP_TCS_PER_ITEM_VALUE_UK1 | Unique | Default | PER_ITEM_VALUE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
