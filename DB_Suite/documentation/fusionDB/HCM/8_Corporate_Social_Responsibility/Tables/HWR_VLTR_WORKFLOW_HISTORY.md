# HWR_VLTR_WORKFLOW_HISTORY

This table stores the workflow history information for project and organization entity

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrworkflowhistory-30525.html#hwrvltrworkflowhistory-30525](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrworkflowhistory-30525.html#hwrvltrworkflowhistory-30525)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_WORKFLOW_HISTORY_PK | ID |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| ID | NUMBER |  | Yes | ID |
| SUBMITTED_BY | VARCHAR2 | 64 |  | SUBMITTED_BY |
| PREVIOUS_STATE | VARCHAR2 | 100 |  | PREVIOUS_STATE |
| ENTITY_ID | NUMBER |  | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 100 | Yes | ENTITY_TYPE |
| ACTION | VARCHAR2 | 100 | Yes | ACTION |
| NEXT_STATE | VARCHAR2 | 100 | Yes | NEXT_STATE |
| COMMENTS | VARCHAR2 | 2000 |  | COMMENTS |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_WORKFLOW_HISTORY_U1 | Unique | FUSION_TS_TX_IDX | ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
