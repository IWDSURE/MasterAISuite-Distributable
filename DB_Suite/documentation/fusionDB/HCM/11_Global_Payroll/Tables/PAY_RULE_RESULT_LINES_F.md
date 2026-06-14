# PAY_RULE_RESULT_LINES_F

This table contains costing accounts assigned to a costing rule.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruleresultlinesf-22149.html#payruleresultlinesf-22149](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruleresultlinesf-22149.html#payruleresultlinesf-22149)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RULE_RESULT_LINES_F_PK | RULE_RESULT_LINE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_RESULT_LINE_ID | NUMBER |  | 18 | Yes | RULE_RESULT_LINE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RULE_RESULT_ID | NUMBER |  | 18 | Yes | RULE_RESULT_ID |
| LINE_NUM | NUMBER |  | 3 | Yes | LINE_NUM |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| USER_NAME | NUMBER |  | 9 | Yes | USER_NAME |
| USER_NAME_VALUE | VARCHAR2 | 100 |  | Yes | USER_NAME_VALUE |
| OPERAND_PARAMETER | NUMBER |  | 18 | Yes | OPERAND_PARAMETER |
| LOGICAL_OPERATOR1 | VARCHAR2 | 20 |  |  | LOGICAL_OPERATOR1 |
| LOGICAL_OPERATOR2 | VARCHAR2 | 20 |  |  | LOGICAL_OPERATOR2 |
| LEFT_PARANTHESIS | VARCHAR2 | 20 |  |  | LEFT_PARANTHESIS |
| RIGHT_PARANTHESIS | VARCHAR2 | 2 |  |  | RIGHT_PARANTHESIS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_RULE_RESULT_LINES_F_PK | Unique | Default | RULE_RESULT_LINE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
