# BEN_ELIG_RSLT_F_

Stores Y/N result of Eligibility Evaluation

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligrsltf-22632.html#beneligrsltf-22632](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligrsltf-22632.html#beneligrsltf-22632)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_RSLT_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ELIG_RSLT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_RSLT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to HR_ORGANIZATION_UNITS. |
| ELIG_OBJ_ID | NUMBER |  | 18 |  | Table that defines the Eligibility Object |
| PERSON_ID | NUMBER |  | 18 |  | Person_id for which results are stored |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment_id for which results are stored |
| ELIG_FLAG | VARCHAR2 | 1 |  |  | This column holds eligible flag. |
| OVERRIDE_THRU_DATE | DATE |  |  |  | This coulmn holds override through date. |
| OVERRIDE_FLAG | VARCHAR2 | 30 |  |  | Flag indicates overriding eligibility. |
| INELG_RSN_CD | VARCHAR2 | 30 |  |  | identifies in-eligiblity reason. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| ELIG_OBJ_TYPE | VARCHAR2 | 30 |  |  | Identifies eligibility object type from the lookup BEN_ELIG_OBJ_TYPE |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_RSLT_PK1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ELIG_RSLT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
