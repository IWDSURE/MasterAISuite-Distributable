# HWM_RULE_OUTPUTS

An output from a rule used in further processing

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleoutputs-26519.html#hwmruleoutputs-26519](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruleoutputs-26519.html#hwmruleoutputs-26519)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_OUTPUTS_PK | RULE_OUTPUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_OUTPUT_ID | NUMBER |  | 18 | Yes | RULE_OUTPUT_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |
| RULE_TMPLT_USAGES_ID | NUMBER |  | 18 | Yes | RULE_TMPLT_USAGES_ID |
| OUTPUT_NAME | VARCHAR2 | 30 |  | Yes | PROCESS_INPUT |
| OUTPUT_SOURCE | VARCHAR2 | 30 |  | Yes | OUTPUT_SOURCE |
| DISPLAY_SEQUENCE | NUMBER |  |  | Yes | DISPLAY_SEQUENCE |
| TBB_GROUP_NUMBER | NUMBER |  |  | Yes | TBB_GROUP_NUMBER |
| HIDE_FLAG | VARCHAR2 | 1 |  |  | HIDE_FLAG |
| RECURSIVE | VARCHAR2 | 1 |  |  | RECURSIVE |
| ATRB_FLD_SET_ID | NUMBER |  | 18 |  | DISPLAY_SEQUENCE |
| TM_ATRB_FLD_ID | NUMBER |  | 18 |  | TM_ATRB_FLD_ID |
| ATRB_FLD_NAME | VARCHAR2 | 240 |  |  | ATRB_FLD_NAME |
| RELATED_INPUT_NAME | VARCHAR2 | 30 |  |  | RELATED_INPUT_NAME |
| MSG_SEVERITY | VARCHAR2 | 30 |  |  | MSG_SEVERITY |
| OUTPUT_VALUE_TYPE | VARCHAR2 | 30 |  |  | OUTPUT_VALUE_TYPE |
| VALUE_SET_ID | NUMBER |  | 18 |  | Forgin key to to FND_VS_VALUE_SETS table |
| DISPLAY_TYPE | VARCHAR2 | 20 |  |  | DISPLAY_TYPE |
| DISPLAY_VALUE | VARCHAR2 | 250 |  |  | DISPLAY_VALUE |
| VALUE_TEXT | VARCHAR2 | 240 |  |  | VALUE_TEXT |
| VALUE_NUMBER | NUMBER |  |  |  | VALUE_NUMBER |
| VALUE_DATE | DATE |  |  |  | VALUE_DATE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_OUTPUTS_PK | Unique | FUSION_TS_TX_DATA | RULE_OUTPUT_ID |
| HWM_RULE_OUTPUTS_U1 | Unique | FUSION_TS_TX_DATA | RULE_ID, OUTPUT_NAME |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
