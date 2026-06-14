# CMP_TCS_PER_ITEM_CRITERIA

This table stores the criteria or conditional text values for the rich text.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperitemcriteria-5661.html#cmptcsperitemcriteria-5661](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperitemcriteria-5661.html#cmptcsperitemcriteria-5661)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ITEM_CRITERIA_ID | NUMBER |  | 18 | Yes | PER_ITEM_CRITERIA_ID |
| PER_PERD_ID | NUMBER |  | 18 | Yes | PER_PERD_ID |
| PER_PERD_STMT_ID | NUMBER |  | 18 | Yes | PER_PERD_STMT_ID |
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| STMT_PERD_ID | NUMBER |  | 18 | Yes | STMT_PERD_ID |
| PERD_RUN_ID | NUMBER |  | 18 | Yes | PERD_RUN_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| CAT_ID | NUMBER |  | 18 |  | CAT_ID |
| ITEM_TAG_ID | NUMBER |  | 18 |  | ITEM_TAG_ID |
| CRITERIA_ID | NUMBER |  | 18 |  | CRITERIA_ID |
| TEXT_VALUE | VARCHAR2 | 2000 |  |  | TEXT_VALUE |
| NUM_VALUE | NUMBER |  |  |  | NUM_VALUE |
| DATE_VALUE | DATE |  |  |  | DATE_VALUE |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| CONTRIBUTIONS_TYPE | VARCHAR2 | 15 |  |  | CONTRIBUTIONS_TYPE |
| CRITERIA_VALUE | VARCHAR2 | 1 |  |  | CRITERIA_VALUE |
| CRITERIA | VARCHAR2 | 2000 |  |  | CRITERIA |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_ITEM_CRITERIA_N1 | Non Unique | Default | PER_PERD_ID, PER_PERD_STMT_ID, PERSON_ID, CAT_ID, CONTRIBUTIONS_TYPE |
| CMP_TCS_PER_ITEM_CRITERIA_UK1 | Unique | Default | PER_ITEM_CRITERIA_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
