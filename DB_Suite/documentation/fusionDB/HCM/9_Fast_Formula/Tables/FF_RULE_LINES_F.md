# FF_RULE_LINES_F

This table contains values for rule lines that help to create formulas.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffrulelinesf-29944.html#ffrulelinesf-29944](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffrulelinesf-29944.html#ffrulelinesf-29944)

## Primary Key

| Name | Columns |
|------|----------|
| FF_RULE_LINES_F_PK | RULE_LINE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_LINE_ID | NUMBER |  | 18 | Yes | Unique identifier for rule line. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| FORMULA_ID | NUMBER |  | 18 | Yes | Identifier for the formula. Foreign key to FF_FORMULAS. |
| CONJUNCTION | VARCHAR2 | 30 |  |  | Conjunction used with this rule line. |
| STARTING_BRACE | VARCHAR2 | 30 |  |  | Starting braces for the formula text for this rule line. |
| ENDING_BRACE | VARCHAR2 | 30 |  |  | Ending braces for the formula text for this rule line. |
| DATABASE_ITEM_ID | NUMBER |  |  |  | Identifier for database item used as operand in rule line. Foreign key to FF_DATABASE_ITEMS. |
| VALUE | VARCHAR2 | 80 |  |  | Value used as operand in rule line. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEQUENCE_NUMBER | NUMBER |  |  |  | Position of rule line within rule. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OPERATOR | VARCHAR2 | 20 |  |  | Operator for this rule. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_RULE_LINES_F_U1 | Unique | Default | RULE_LINE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
