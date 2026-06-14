# CMP_TCS_SCHEDULED_STMTS

This table stores the BIP job details submitted by a user to print the Total Compensation Statements for multiple employees.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsscheduledstmts-16138.html#cmptcsscheduledstmts-16138](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsscheduledstmts-16138.html#cmptcsscheduledstmts-16138)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_SCHEDULED_STMTS_PK | SCHEDULED_STMT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULED_STMT_ID | NUMBER |  | 18 | Yes | Primary Key for the table |
| JOB_ID | NUMBER |  | 18 |  | Job Id for the Report Job submitted for print TCS statement process |
| JOB_STATUS_CODE | VARCHAR2 | 30 |  |  | Job Status |
| STMT_ID | NUMBER |  | 18 |  | Statement Id of the Statement for which print process is initiated |
| STMT_PERD_ID | NUMBER |  | 18 |  | Statement Period Id |
| CURRENCY_TYPE | VARCHAR2 | 32 |  |  | Currency code for which PDF statement will be printed |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Business Unit Id |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Department Id |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity Id |
| LEGISLATION_CODE | VARCHAR2 | 32 |  |  | Legislation Code |
| TOTAL_WORKERS | NUMBER |  | 10 |  | Count of employees processed by print job |
| INCLUDE_ALL_EMP_STMT_FLAG | VARCHAR2 | 1 |  |  | Flag to decide whether All Employer Statement for multi-employer employees should be a part of generated PDF |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_SCHEDULED_STMTS_PK | Unique | Default | SCHEDULED_STMT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
