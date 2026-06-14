# HWM_RULE_INPUTS

Stores Rule Templates Input PArameters for Formula/Script

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleinputs-13367.html#hwmruleinputs-13367](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleinputs-13367.html#hwmruleinputs-13367)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_INPUTS_PK | RULE_INPUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_INPUT_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |
| RULE_TMPLT_INPUT_ID | NUMBER |  | 18 | Yes | RULE_TMPLT_INPUT_ID |
| DISPLAY_SEQUENCE | NUMBER |  |  | Yes | DISPLAY_SEQUENCE |
| INPUT_NAME | VARCHAR2 | 30 |  | Yes | PROCESS_INPUT |
| USER_DEFINED_NAME | VARCHAR2 | 80 |  |  | Deprecated/ Obsolete column. 
Column replaced with reference to HWM_RULE_TMPLT_INPUTS_VL .USER_DEFINED_IN_NAME |
| RULE_PARAMETER_TYPE | VARCHAR2 | 30 |  |  | RULE_PARAMETER_TYPE |
| VALUE_SET_ID | NUMBER |  | 18 |  | Forgin key to to FND_VS_VALUE_SETS table |
| TCAT_ID | NUMBER |  | 18 |  | Time category Run Condition, which determines if this member should be applied on TBB. |
| DISPLAY_TYPE | VARCHAR2 | 20 |  |  | DISPLAY_TYPE |
| DISPLAY_VALUE | VARCHAR2 | 250 |  |  | DISPLAY_VALUE |
| VALUE_TEXT | VARCHAR2 | 240 |  |  | VALUE_TEXT |
| VALUE_NUMBER | NUMBER |  |  |  | VALUE_NUMBER |
| VALUE_DATE | DATE |  |  |  | VALUE_DATE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| PARM_VALUE_REQUIRED | VARCHAR2 | 1 |  |  | PARM_VALUE_REQUIRED |
| ROW_SEQUENCE | NUMBER |  |  |  | Row Sequence |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_INPUTS_PK | Unique | FUSION_TS_TX_DATA | RULE_INPUT_ID |
| HWM_RULE_INPUTS_U1 | Unique | FUSION_TS_TX_DATA | RULE_ID, INPUT_NAME |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
