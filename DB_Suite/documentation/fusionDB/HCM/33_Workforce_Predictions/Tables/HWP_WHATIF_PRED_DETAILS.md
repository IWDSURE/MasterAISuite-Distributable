# HWP_WHATIF_PRED_DETAILS

This table stores the current and new predicted values for an assignment.

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpwhatifpreddetails-7246.html#hwpwhatifpreddetails-7246](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpwhatifpreddetails-7246.html#hwpwhatifpreddetails-7246)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_WHATIF_PRED_DETAILS_PK | SEQ_NO |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQ_NO | NUMBER |  | 18 | Yes | Seq No generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment Id of a person. |
| CURRENT_PREDICTED_ATTRITION | VARCHAR2 | 2000 |  |  | Current Predicted Attrition of the person. |
| CURRENT_PREDICTED_PERF | VARCHAR2 | 2000 |  |  | Current Predicted Performance of the person. |
| NEW_PREDICTED_ATTRITION | VARCHAR2 | 2000 |  |  | New Predicted Attrition of the person. |
| NEW_PREDICTED_PERF | VARCHAR2 | 2000 |  |  | New Predicted Performance of the person. |
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 |  | Allocated CheckList Id. |
| LOGGEDIN_MANAGER_ID | NUMBER |  | 18 | Yes | Logged in Manager Id. |
| ANALYSIS_NAME | VARCHAR2 | 200 |  | Yes | Saved Analysis Name for the modified attribute values. |
| ANALYSIS_DESC | VARCHAR2 | 2000 |  |  | Description of the saved Analysis Name. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_WHATIF_PRED_DETAILS_N1 | Non Unique | Default | ASSIGNMENT_ID, ANALYSIS_NAME |
| HWP_WHATIF_PRED_DETAILS_U1 | Unique | Default | SEQ_NO |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
