# HWM_RULE_TMPLT_INPUTS

Stores Rule Templates Input PArameters for Formula/Script

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruletmpltinputs-22083.html#hwmruletmpltinputs-22083](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruletmpltinputs-22083.html#hwmruletmpltinputs-22083)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_TMPLT_INPUTS_PK | RULE_TMPLT_INPUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_TMPLT_INPUT_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| RULE_TMPLTS_ID | NUMBER |  | 18 | Yes | RULE_TMPLTS_ID |
| DISPLAY_SEQUENCE | NUMBER |  |  | Yes | DISPLAY_SEQUENCE |
| INPUT_NAME | VARCHAR2 | 30 |  | Yes | PROCESS_INPUT |
| USER_DEFINED_NAME | VARCHAR2 | 80 |  |  | Deprecated/ Obsolete column. 
Column replaced with    HWM_RULE_TMPLT_INPUTS_TL .USER_DEFINED_IN_NAME |
| RULE_PARAMETER_TYPE | VARCHAR2 | 30 |  |  | RULE_PARAMETER_TYPE |
| PARM_VALUE_REQUIRED | VARCHAR2 | 1 |  |  | PARM_VALUE_REQUIRED |
| VALUE_SET_ID | NUMBER |  | 18 |  | Foreign key to to FND_VS_VALUE_SETS table |
| LOOKUP_TYPE | VARCHAR2 | 30 |  |  | Foreign key to Lookup Types |
| ROW_SEQUENCE | NUMBER |  |  |  | Row Sequence |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_TMPLT_INPUTS_N20 | Non Unique | Default | SGUID |
| HWM_RULE_TMPLT_INPUTS_PK | Unique | Default | RULE_TMPLT_INPUT_ID, ORA_SEED_SET1 |
| HWM_RULE_TMPLT_INPUTS_PK1 | Unique | Default | RULE_TMPLT_INPUT_ID, ORA_SEED_SET2 |
| HWM_RULE_TMPLT_INPUTS_U1 | Unique | Default | RULE_TMPLTS_ID, DISPLAY_SEQUENCE, ORA_SEED_SET1 |
| HWM_RULE_TMPLT_INPUTS_U11 | Unique | Default | RULE_TMPLTS_ID, DISPLAY_SEQUENCE, ORA_SEED_SET2 |
| HWM_RULE_TMPLT_INPUTS_U2 | Unique | Default | RULE_TMPLTS_ID, INPUT_NAME, ORA_SEED_SET1 |
| HWM_RULE_TMPLT_INPUTS_U21 | Unique | Default | RULE_TMPLTS_ID, INPUT_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
