# HWP_DATA_MINING_REASONS

This table contains data mining reasons for predictives.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingreasons-24591.html#hwpdataminingreasons-24591](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingreasons-24591.html#hwpdataminingreasons-24591)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_DATA_MINING_REASONS_PK | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID, ATTR_CODE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROCESS_ID | NUMBER |  | 18 | Yes | Data Mining process ID. |
| PERSON_ID | NUMBER |  | 18 | Yes | Data mining person ID. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Data Mining assignment ID. |
| ATTR_CODE | VARCHAR2 | 200 |  | Yes | Data Mining attribute code. |
| ATTR_VALUE | VARCHAR2 | 2000 |  |  | Data Mining attribute value. |
| PRED_WEIGHT | NUMBER |  |  |  | Data mining reasons predicted weightage. |
| PRED_WEIGHT_PCT | NUMBER |  |  |  | Data mining reasons predicted weightage percentage. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_DATA_MINING_REASONS_N1 | Non Unique | Default | ASSIGNMENT_ID, ATTR_CODE |
| HWP_DATA_MINING_REASONS_PK | Unique | Default | PROCESS_ID, PERSON_ID, ASSIGNMENT_ID, ATTR_CODE |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
