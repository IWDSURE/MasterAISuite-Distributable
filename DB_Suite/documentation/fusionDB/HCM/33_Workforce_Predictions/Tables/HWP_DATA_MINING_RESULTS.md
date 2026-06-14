# HWP_DATA_MINING_RESULTS

The table contains data mining results for predictives.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingresults-17451.html#hwpdataminingresults-17451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingresults-17451.html#hwpdataminingresults-17451)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_DATA_MINING_RESULTS_PK | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Data mining results process ID. |
| PERSON_ID | NUMBER |  | 18 | Yes | Data mining results Person ID. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Data mining results Assignment ID. |
| PRED_VALUE | VARCHAR2 | 2000 |  |  | Data mining results predicated value. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_DATA_MINING_RESULTS_N1 | Non Unique | Default | PERSON_ID, ASSIGNMENT_ID |
| HWP_DATA_MINING_RESULTS_PK | Unique | Default | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
