# PAY_BAL_BATCH_LINES

This table contains the batch lines of a batch of balance initialisations to be  transferred into the live schema.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalbatchlines-23254.html#paybalbatchlines-23254](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalbatchlines-23254.html#paybalbatchlines-23254)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_BATCH_LINES_PK | BATCH_LINE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_LINE_ID | NUMBER |  | 18 | Yes | BATCH_LINE_ID |
| BATCH_ID | NUMBER |  | 18 | Yes | BATCH_ID |
| BATCH_LINE_STATUS | VARCHAR2 | 30 |  |  | BATCH_LINE_STATUS |
| LINE_SEQUENCE | NUMBER |  | 18 | Yes | LINE_SEQUENCE |
| VALUE | VARCHAR2 | 60 |  |  | VALUE |
| UPLOAD_DATE | DATE |  |  |  | UPLOAD_DATE |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_REL_ACTION_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| PAYROLL_RELATIONSHIP_NUMBER | VARCHAR2 | 30 |  |  | PAYROLL_RELATIONSHIP_NUMBER |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| TERM_NUMBER | VARCHAR2 | 30 |  |  | TERM_NUMBER |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| ASSIGNMENT_NUMBER | VARCHAR2 | 30 |  |  | ASSIGNMENT_NUMBER |
| BALANCE_DIMENSION_ID | NUMBER |  | 18 |  | BALANCE_DIMENSION_ID |
| DIMENSION_NAME | VARCHAR2 | 160 |  |  | DIMENSION_NAME |
| BALANCE_TYPE_ID | NUMBER |  | 18 |  | BALANCE_TYPE_ID |
| BALANCE_NAME | VARCHAR2 | 120 |  |  | BALANCE_NAME |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | LEGAL_EMPLOYER_ID |
| LEGAL_EMPLOYER_NAME | VARCHAR2 | 240 |  |  | LEGAL_EMPLOYER_NAME |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| PAYROLL_NAME | VARCHAR2 | 80 |  |  | PAYROLL_NAME |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 |  | ELEMENT_ENTRY_ID |
| AREA1 | VARCHAR2 | 30 |  |  | AREA1 |
| AREA2 | VARCHAR2 | 30 |  |  | AREA2 |
| AREA3 | VARCHAR2 | 30 |  |  | AREA3 |
| AREA4 | VARCHAR2 | 30 |  |  | AREA4 |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | THIRD_PARTY_PAYEE_ID |
| THIRD_PARTY_PAYEE_NAME | VARCHAR2 | 900 |  |  | TIRD_PARTY_PAYEE_NAME |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |
| TIME_DEFINITION_NAME | VARCHAR2 | 80 |  |  | TIME_DEFINITION_NAME |
| CALC_BREAKDOWN_ID | NUMBER |  | 18 |  | CALC_BREAKDOWN_ID |
| BALANCE_DATE | DATE |  |  |  | BALANCE_DATE |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| TAX_UNIT_NAME | VARCHAR2 | 240 |  |  | TAX_UNIT_NAME |
| RUN_TYPE_ID | NUMBER |  | 10 |  | RUN_TYPE_ID |
| RUN_TYPE_NAME | VARCHAR2 | 80 |  |  | RUN_TYPE_NAME |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | Deduction Type ID. |
| DEDUCTION_TYPE_NAME | VARCHAR2 | 240 |  |  | Deduction Type Name. |
| PROCESSING_SPAN | NUMBER |  | 18 |  | Processing Span. |
| PROCESSING_SPAN_NAME | VARCHAR2 | 80 |  |  | Processing Span Name. |
| CONTEXT1_ID | NUMBER |  | 18 |  | CONTEXT1_ID |
| CONTEXT1_NAME | VARCHAR2 | 80 |  |  | CONTEXT1_NAME |
| CONTEXT1_VALUE | VARCHAR2 | 60 |  |  | CONTEXT1_VALUE |
| CONTEXT2_ID | NUMBER |  | 18 |  | CONTEXT2_ID |
| CONTEXT2_NAME | VARCHAR2 | 80 |  |  | CONTEXT2_NAME |
| CONTEXT2_VALUE | VARCHAR2 | 60 |  |  | CONTEXT2_VALUE |
| CONTEXT3_ID | NUMBER |  | 18 |  | CONTEXT3_ID |
| CONTEXT3_NAME | VARCHAR2 | 80 |  |  | CONTEXT3_NAME |
| CONTEXT3_VALUE | VARCHAR2 | 60 |  |  | CONTEXT3_VALUE |
| CONTEXT4_ID | NUMBER |  | 18 |  | CONTEXT4_ID |
| CONTEXT4_NAME | VARCHAR2 | 80 |  |  | CONTEXT4_NAME |
| CONTEXT4_VALUE | VARCHAR2 | 60 |  |  | CONTEXT4_VALUE |
| CONTEXT5_ID | NUMBER |  | 18 |  | CONTEXT5_ID |
| CONTEXT5_NAME | VARCHAR2 | 80 |  |  | CONTEXT5_NAME |
| CONTEXT5_VALUE | VARCHAR2 | 60 |  |  | CONTEXT5_VALUE |
| CONTEXT6_ID | NUMBER |  | 18 |  | CONTEXT6_ID |
| CONTEXT6_NAME | VARCHAR2 | 80 |  |  | CONTEXT6_NAME |
| CONTEXT6_VALUE | VARCHAR2 | 60 |  |  | CONTEXT6_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_BAL_BATCH_LINES_N1 | Non Unique | Default | BATCH_ID, BATCH_LINE_STATUS |
| PAY_BAL_BATCH_LINES_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, BATCH_ID |
| PAY_BAL_BATCH_LINES_N3 | Non Unique | Default | BATCH_ID, LINE_SEQUENCE |
| PAY_BAL_BATCH_LINES_PK | Unique | Default | BATCH_LINE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
