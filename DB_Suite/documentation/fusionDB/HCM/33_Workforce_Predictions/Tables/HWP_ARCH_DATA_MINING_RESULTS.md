# HWP_ARCH_DATA_MINING_RESULTS

This table stores the archived data mining results.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwparchdataminingresults-22070.html#hwparchdataminingresults-22070](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwparchdataminingresults-22070.html#hwparchdataminingresults-22070)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_ARCH_DATA_MINING_RESU_PK | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Data Mining Process Id. |
| PERSON_ID | NUMBER |  | 18 | Yes | Data Mining Person Id. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Data Mining Assignment Id. |
| PRED_VALUE | VARCHAR2 | 2000 |  |  | Data mining results predicated value. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_ARCH_DATA_MINING_RESU_PK | Unique | FUSION_TS_TX_DATA | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
