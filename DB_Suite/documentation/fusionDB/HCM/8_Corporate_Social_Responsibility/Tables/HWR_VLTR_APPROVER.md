# HWR_VLTR_APPROVER

This table stores base Approval process

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrapprover-5658.html#hwrvltrapprover-5658](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrapprover-5658.html#hwrvltrapprover-5658)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_APPROVER_PK | APPROVER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APPROVER_ID | NUMBER |  | 18 | Yes | APPROVER_ID |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | ORGANIZATION_ID |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |
| APPROVAL_TYPE | VARCHAR2 | 100 |  |  | APPROVAL_TYPE |
| EMPLOYEE_ID | NUMBER |  | 18 |  | EMPLOYEE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_APPROVER_U1 | Unique | FUSION_TS_TX_IDX | APPROVER_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
