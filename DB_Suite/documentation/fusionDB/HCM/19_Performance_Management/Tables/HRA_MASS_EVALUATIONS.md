# HRA_MASS_EVALUATIONS

This table stores the primary data related to Mass Evaluation Documents.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** hra_mass_evaluations

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hramassevaluations-22471.html#hramassevaluations-22471](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hramassevaluations-22471.html#hramassevaluations-22471)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_MASS_EVALUATIONS_PK | MASS_EVALUATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_EVALUATION_ID | NUMBER |  | 18 | Yes | Stores the primary key of the mass evaluation documents. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| MANAGER_ID | NUMBER |  | 18 |  | Stores the manager identifier of the mass evaluation documents. |
| TMPL_PERIOD_ID | NUMBER |  | 18 |  | Stores the template period identifier of the mass evaluation documents. |
| ACTION | VARCHAR2 | 30 |  |  | Stores the action of the mass evaluation documents. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REQUEST_STATUS | VARCHAR2 | 30 |  |  | Stores the ESS request status of the mass evaluation documents. |
| EVALUATION_ID_LIST | CLOB |  |  |  | Stores the list of performance document identifier to be processed for the mass evaluation process. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_MASS_EVALUATIONS_N1 | Non Unique | HRA_MASS_EVALUATIONS_N1 | MANAGER_ID, TMPL_PERIOD_ID |
| HRA_MASS_EVALUATIONS_PK | Unique | HRA_MASS_EVALUATIONS_PK | MASS_EVALUATION_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
