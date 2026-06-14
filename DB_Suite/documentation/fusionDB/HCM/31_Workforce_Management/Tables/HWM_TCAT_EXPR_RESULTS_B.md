# HWM_TCAT_EXPR_RESULTS_B

This is the base table for storing the expression results.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatexprresultsb-21371.html#hwmtcatexprresultsb-21371](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatexprresultsb-21371.html#hwmtcatexprresultsb-21371)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCAT_EXPR_RESULTS_B_PK | TCAT_EXPR_RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCAT_EXPR_RESULT_ID | NUMBER |  | 18 | Yes | TCAT_EXPR_RESULTS_ID |
| TCAT_ID | NUMBER |  | 18 | Yes | FK to HWM_TCATS_B.TCAT_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DISPLAY_SEQUENCE | NUMBER |  | 18 |  | ORDER_NUMBER |
| EXPRESSION_GROUP_ID | NUMBER |  | 18 |  | EXPRESSION_GROUP_ID |
| LEFT_PARENTHESIS_NUM | NUMBER |  | 18 |  | LEFT_PARENTHESIS |
| TIME_ATRB_FLD_ID | NUMBER |  | 18 |  | TIME_ATRB_FLD_ID |
| VALUE_TYPE | VARCHAR2 | 50 |  |  | VALUE_TYPE |
| VALUE_ID | NUMBER |  | 18 |  | VALUE_ID |
| DATA_SOURCE_USAGE_ID | NUMBER |  | 18 |  | Foreign Key to Data Sources |
| OPERATOR | VARCHAR2 | 20 |  |  | GROUP_OPERATOR |
| RIGHT_PARENTHESIS_NUM | NUMBER |  | 18 |  | RIGHT_PARENTHESIS |
| EXPR_ROW_IDENTIFIER | VARCHAR2 | 2 |  |  | EXPR_ROW_IDENTIFIER |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id |
| IMP_TCAT_ID | NUMBER |  | 18 |  | This column stores the TimeCategory Id of the imported TimeCategory |
| DISPLAY_VALUE | VARCHAR2 | 255 |  |  | Stores the selected description  for ValueSet/SpecificValue type of expressions |
| VALUE_CHAR | VARCHAR2 | 255 |  |  | Stores the selected Code  for SpecificValue type of expressions |
| VALUE_DATE | DATE |  |  |  | Stores the selected Code  for SpecificValue type of expressions |
| VALUE_TIMESTAMP | TIMESTAMP |  |  |  | Stores the selected Code  for SpecificValue type of expressions |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCAT_EXPR_RESULTS_B_N1 | Non Unique | Default | TCAT_ID |
| HWM_TCAT_EXPR_RESULTS_B_N20 | Non Unique | Default | SGUID |
| HWM_TCAT_EXPR_RESULTS_B_U1 | Unique | Default | TCAT_EXPR_RESULT_ID, ORA_SEED_SET1 |
| HWM_TCAT_EXPR_RESULTS_B_U11 | Unique | Default | TCAT_EXPR_RESULT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
