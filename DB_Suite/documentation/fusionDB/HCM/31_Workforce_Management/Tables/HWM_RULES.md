# HWM_RULES

Contains the rules created for OTL Time Calculation, Time Entry and Time Audit rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrules-9381.html#hwmrules-9381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrules-9381.html#hwmrules-9381)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULES_PK | RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| RULE_NAME | VARCHAR2 | 80 |  | Yes | Name of the Rule |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Optional description of the Rule |
| RULE_TMPLTS_ID | NUMBER |  | 18 | Yes | Foreign Key to the template used to create the rule. |
| PRS_FORMULA_ID | NUMBER |  | 18 |  | PRS_FORMULA_ID |
| PRS_SCRIPT_ID | NUMBER |  | 18 |  | PRS_SCRIPT_ID |
| PROCESS_TYPE | VARCHAR2 | 30 |  |  | PROCESS_TYPE |
| RULE_TYPE | VARCHAR2 | 30 |  | Yes | RULE_TYPE |
| CLASSIFICATION | VARCHAR2 | 30 |  |  | CLASSIFICATION |
| RUN_SUMMATION_LEVEL | VARCHAR2 | 30 |  |  | summation Level |
| RUN_TBB_LEVEL | VARCHAR2 | 30 |  |  | Report Level |
| RULE_EXEC_TYPE | VARCHAR2 | 30 |  |  | RULE_EXEC_TYPE |
| RUN_EVENT_SAVE | VARCHAR2 | 1 |  |  | RUN_EVENT_SAVE |
| RUN_EVENT_SUB | VARCHAR2 | 1 |  |  | RUN_EVENT_SUB |
| RUN_EVENT_RESUB | VARCHAR2 | 1 |  |  | RUN_EVENT_RESUB |
| RUN_EVENT_DELETE | VARCHAR2 | 1 |  |  | RUN_EVENT_DELETE |
| SUPPRESS_DUP_MSGS | VARCHAR2 | 1 |  |  | Suppress duplicate TER messages |
| INCLUDE_EMPTY_TC | VARCHAR2 | 30 |  |  | process NULL timecards |
| RULE_SUB_TYPE | VARCHAR2 | 30 |  |  | RULE_SUB_TYPE |
| USE_INPUT_TIMEZONE | VARCHAR2 | 30 |  |  | Use timeZone or reference time |
| FAST_FORMULA_EXEC_TYPE | VARCHAR2 | 30 |  |  | FAST_FORMULA_EXEC_TYPE |
| DFLT_ALLOCATION_ID | NUMBER |  | 18 |  | DFLT_ALLOCATION_ID |
| RULE_SET_ID | NUMBER |  | 18 |  | Foreign key to Rule Set |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULES_PK | Unique | FUSION_TS_TX_DATA | RULE_ID |
| HWM_RULES_U1 | Unique | FUSION_TS_TX_DATA | RULE_NAME |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
