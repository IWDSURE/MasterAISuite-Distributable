# IRC_FN_EXPRESSION_REFS

IRC_FN_EXPRESSION_REFS: holds the conditions for an event either predefined or custom conditions by which life cycle phase and states can be moved.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfnexpressionrefs-27384.html#ircfnexpressionrefs-27384](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfnexpressionrefs-27384.html#ircfnexpressionrefs-27384)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_FN_EXPRESSION_REFS_PK | EXPRESSION_REF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXPRESSION_REF_ID | NUMBER |  | 18 | Yes | Primary Key of the table |
| FORMULA_ID | NUMBER |  | 18 |  | References the formula used in the expression |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Relation component |
| OBJECT_ID | NUMBER |  | 18 | Yes | Relation Component |
| REF_TYPE_CODE | VARCHAR2 | 60 |  | Yes | Identifies the condition expression Ex: "ORA_IS_INTERNAL" |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_FN_EXPRESSION_REFS_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_ID |
| IRC_FN_EXPRESSION_REFS_U1 | Unique | Default | EXPRESSION_REF_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
