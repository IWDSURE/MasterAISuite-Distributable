# PAY_SUBMIT_RELATED_FLOWS

this will be utilized in Payrollflow s

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paysubmitrelatedflows-26660.html#paysubmitrelatedflows-26660](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paysubmitrelatedflows-26660.html#paysubmitrelatedflows-26660)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_SUBMIT_RELATED_FLOW_PK | RELATED_FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RELATED_FLOW_ID | NUMBER |  | 18 | Yes | RELATED_FLOW_ID |
| RELATED_BASE_FLOW_ID | NUMBER |  | 18 | Yes | RELATED_BASE_FLOW_ID |
| SOURCE_BASE_FLOW_ID | NUMBER |  | 18 | Yes | SOURCE_BASE_FLOW_ID |
| SOURCE_BASE_FLOW_TASK_ID | NUMBER |  | 18 | Yes | SOURCE_BASE_FLOW_TASK_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_SUBMIT_RELATED_FLOW_U1 | Unique | Default | RELATED_FLOW_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
