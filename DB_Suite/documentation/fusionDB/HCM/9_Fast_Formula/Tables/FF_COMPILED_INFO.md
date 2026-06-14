# FF_COMPILED_INFO

This table contains compiled versions of user-defined formulas.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffcompiledinfo-11593.html#ffcompiledinfo-11593](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffcompiledinfo-11593.html#ffcompiledinfo-11593)

## Primary Key

| Name | Columns |
|------|----------|
| FF_COMPILED_INFO_PK | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_EDITION_CONTEXT |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_ID | NUMBER |  | 18 | Yes | Identifier for the compiled formula. Foreign key to FF_FORMULAS. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| FDIU_ENTRY_COUNT | NUMBER |  | 9 | Yes | Number of formula data item usage entries for the formula in FF_FDI_USAGES. |
| SELECT_STATEMENT_COUNT | NUMBER |  | 9 | Yes | Number of separate SELECT statements in the executable code. |
| TEXT_LENGTH | NUMBER |  | 9 | Yes | Length (in characters) of the program. |
| COMPILED_TEXT | CLOB |  |  |  | The program that represents the user formula. |
| STATUS | VARCHAR2 | 1 |  |  | Validity status. A status other than V means that the formula needs to be recompiled. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| PLSQL_CREATED | VARCHAR2 | 1 |  | Yes | Flag whether or not  formula PLSQL has been created. |
| PACKAGE_NAME | VARCHAR2 | 30 |  |  | The compiled formula PLSQL package name. |
| PACKAGE_HEADER | CLOB |  |  |  | Formula PLSQL package header text. |
| PACKAGE_BODY | CLOB |  |  |  | Formula PLSQL package body text. |
| PLSQL_ERRORS | CLOB |  |  |  | Errors in creating formula PLSQL. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COMPILE_ID | NUMBER |  | 18 | Yes | Identifier for the formula compile. |
| ORA_EDITION_CONTEXT | VARCHAR2 | 30 |  | Yes | Indicates the edition based redefinition (EBR) context to which the row belongs - either 'ALL', ''SET1' or 'SET2'. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_COMPILED_INFO_PK | Unique | Default | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_EDITION_CONTEXT |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
