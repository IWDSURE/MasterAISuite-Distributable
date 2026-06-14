# FF_COMPILE_CODE

This table contains compiler-generated formula code.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffcompilecode-7205.html#ffcompilecode-7205](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffcompilecode-7205.html#ffcompilecode-7205)

## Primary Key

| Name | Columns |
|------|----------|
| FF_COMPILE_CODE_PK | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, COMPILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_ID | NUMBER |  | 18 | Yes | Identifier for the compiled formula. Foreign key to FF_FORMULAS_B_F. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| COMPILE_ID | NUMBER |  | 18 | Yes | Identifier for the compile that created this code. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SELECT_STATEMENT_COUNT | NUMBER |  | 9 | Yes | Number of separate SELECT statements in the executable code. |
| TEXT_LENGTH | NUMBER |  | 9 | Yes | Length (in characters) of the program. |
| COMPILED_TEXT | CLOB |  |  |  | The compiled formula program text. |
| PACKAGE_NAME | VARCHAR2 | 30 |  | Yes | The compiled formula PLSQL package name. |
| PACKAGE_HEADER | CLOB |  |  |  | The compiled formula PLSQL package header text. |
| PACKAGE_BODY | CLOB |  |  |  | The compiled formula PLSQL package body text. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_COMPILE_CODE_PK | Unique | DEFAULT | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, COMPILE_ID |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
