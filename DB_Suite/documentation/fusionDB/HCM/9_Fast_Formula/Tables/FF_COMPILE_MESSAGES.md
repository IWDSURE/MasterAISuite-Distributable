# FF_COMPILE_MESSAGES

This table contains messages raised when compiling formulas.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffcompilemessages-13144.html#ffcompilemessages-13144](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffcompilemessages-13144.html#ffcompilemessages-13144)

## Primary Key

| Name | Columns |
|------|----------|
| FF_COMPILE_MESSAGES_PK | FORMULA_ID, SEQUENCE, ORA_EDITION_CONTEXT |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_ID | NUMBER |  | 18 | Yes | Identifier for the compiled formula. Foreign key to FF_FORMULAS. |
| SEQUENCE | NUMBER |  | 3 | Yes | Sequence number of the formula compile message. |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the formula compile. |
| EFFECTIVE_DATE | DATE |  |  |  | Effective date used when compiling the formula. |
| MESSAGE_NAME | VARCHAR2 | 30 |  |  | Formula compile error message name. |
| LINE_NUMBER | NUMBER |  | 5 |  | Line number where error occurred. |
| CHAR_POSITION | NUMBER |  | 3 |  | Character position on line where error occurred. |
| TOKEN0 | VARCHAR2 | 30 |  |  | Compile error message token 0 name. |
| TOKEN1 | VARCHAR2 | 30 |  |  | Compile error message token 1 name. |
| TOKEN2 | VARCHAR2 | 30 |  |  | Compile error message token 2 name. |
| TOKEN3 | VARCHAR2 | 30 |  |  | Compile error message token 3 name. |
| TOKEN4 | VARCHAR2 | 30 |  |  | Compile error message token 4 name. |
| TOKEN5 | VARCHAR2 | 30 |  |  | Compile error message token 5 name. |
| TOKEN_VALUE0 | VARCHAR2 | 2000 |  |  | Compile error message token 0 value. |
| TOKEN_VALUE1 | VARCHAR2 | 2000 |  |  | Compile error message token 1 value. |
| TOKEN_VALUE2 | VARCHAR2 | 2000 |  |  | Compile error message token 2 value. |
| TOKEN_VALUE3 | VARCHAR2 | 2000 |  |  | Compile error message token 3 value. |
| TOKEN_VALUE4 | VARCHAR2 | 2000 |  |  | Compile error message token 4 value. |
| TOKEN_VALUE5 | VARCHAR2 | 2000 |  |  | Compile error message token 5 value. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COMPILE_ID | NUMBER |  | 18 | Yes | Identifier for the formula compile. |
| ORA_EDITION_CONTEXT | VARCHAR2 | 30 |  | Yes | Indicates the edition based redefinition (EBR) context to which the row belongs - either 'ALL', ''SET1' or 'SET2'. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| FF_COMPILE_MESSAGES_N1 | Non Unique | Default | FORMULA_ID |  |
| FF_COMPILE_MESSAGES_PK | Unique | Default | FORMULA_ID, SEQUENCE, ORA_EDITION_CONTEXT | Obsolete |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
