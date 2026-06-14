# HWM_RULE_TMPLTS

Specifies formula and input and output variables for use with rule instances.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruletmplts-22252.html#hwmruletmplts-22252](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruletmplts-22252.html#hwmruletmplts-22252)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_TMPLTS_PK | RULE_TMPLTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_TMPLTS_ID | NUMBER |  | 18 | Yes | RULE_TMPLTS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| PROCESS_TYPE | VARCHAR2 | 30 |  | Yes | PROCESS_TYPE |
| PRS_FORMULA_ID | NUMBER |  | 18 |  | PRS_FORMULA_ID |
| PRS_SCRIPT_ID | NUMBER |  | 18 |  | PRS_SCRIPT_ID |
| PROCESS_NAME | VARCHAR2 | 80 |  |  | PROCESS_NAME |
| TEMPLATE_TYPE | VARCHAR2 | 30 |  | Yes | TEMPLATE_TYPE |
| TEMPLATE_NAME | VARCHAR2 | 80 |  | Yes | NAME |
| CLASSIFICATION | VARCHAR2 | 30 |  |  | CLASSIFICATION |
| RUN_SUMMATION_LEVEL | VARCHAR2 | 30 |  | Yes | Summation Level |
| RUN_TBB_LEVEL | VARCHAR2 | 30 |  | Yes | Report Level |
| RULE_EXEC_TYPE | VARCHAR2 | 30 |  |  | RULE_EXEC_TYPE |
| RUN_EVENT_SAVE | VARCHAR2 | 1 |  |  | RUN_EVENT_SAVE |
| RUN_EVENT_SUB | VARCHAR2 | 1 |  |  | RUN_EVENT_SUB |
| RUN_EVENT_RESUB | VARCHAR2 | 1 |  |  | RUN_EVENT_RESUB |
| RUN_EVENT_DELETE | VARCHAR2 | 1 |  |  | RUN_EVENT_DELETE |
| SUPPRESS_DUP_MSGS | VARCHAR2 | 1 |  |  | Suppress  Duplicate TER messages |
| INCLUDE_EMPTY_TC | VARCHAR2 | 30 |  |  | Process  NULL timecards |
| SEEDED_FLAG | VARCHAR2 | 1 |  |  | Is seeded data |
| RULE_SUB_TYPE | VARCHAR2 | 30 |  |  | RULE_SUB_TYPE |
| FAST_FORMULA_EXEC_TYPE | VARCHAR2 | 30 |  |  | FAST_FORMULA_EXEC_TYPE |
| DFLT_ALLOCATION_ID | NUMBER |  | 18 |  | DFLT_ALLOCATION_ID |
| JAVA_CLASS | VARCHAR2 | 500 |  |  | Class used in Java reflection |
| JAVA_METHOD | VARCHAR2 | 100 |  |  | Method used to process the rule |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_RULE_TMPLTS_PK | Unique | Default | RULE_TMPLTS_ID, ORA_SEED_SET1 |
| HWM_RULE_TMPLTS_PK1 | Unique | Default | RULE_TMPLTS_ID, ORA_SEED_SET2 |
| HWM_RULE_TMPLTS_U1 | Unique | Default | TEMPLATE_NAME, ORA_SEED_SET1 |
| HWM_RULE_TMPLTS_U11 | Unique | Default | TEMPLATE_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
