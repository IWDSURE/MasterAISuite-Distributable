# HWM_TCAT_LOGIC_EXPRS

This table will store the logic expression.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatlogicexprs-6176.html#hwmtcatlogicexprs-6176](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatlogicexprs-6176.html#hwmtcatlogicexprs-6176)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCAT_LOGIC_EXPRS_PK | TCAT_LOGIC_EXPR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCAT_LOGIC_EXPR_ID | NUMBER |  | 18 | Yes | TCAT_LOGIC_EXPR_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCAT_ID | NUMBER |  | 18 | Yes | FK to HWM_TCATS_B.TCAT_ID |
| TCAT_EXPRESSION_CMP_1_ID | NUMBER |  | 18 |  | TCAT_EXPRESSION_CMP_ID_1 |
| COMPONENT1 | VARCHAR2 | 5 |  |  | COMPONENT1 |
| OPERATOR | VARCHAR2 | 20 |  |  | OPERATOR |
| TCAT_EXPRESSION_CMP_2_ID | NUMBER |  | 18 |  | TCAT_EXPRESSION_CMP_ID_2 |
| COMPONENT2 | VARCHAR2 | 5 |  |  | COMPONENT2 |
| EXPRESSION_DEPTH | NUMBER |  | 18 |  | EXPRESSION_DEPTH |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCAT_LOGIC_EXPRS_U1 | Unique | Default | TCAT_LOGIC_EXPR_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
