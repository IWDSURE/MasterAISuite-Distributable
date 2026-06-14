# FAI_TMPL_MDL_PARAMS

This table contains LLM parameters and values for prompt designs.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitmplmdlparams-13189.html#faitmplmdlparams-13189](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitmplmdlparams-13189.html#faitmplmdlparams-13189)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_TMPL_MDL_PARAMS_PK | TMPL_MDL_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TMPL_MDL_PARAM_ID | VARCHAR2 | 32 |  | Yes | The system generated surrogate key. |
| TMPL_MDL_PARAM_CODE | VARCHAR2 | 80 |  | Yes | This column indicates the LLM parameter code. |
| TMPL_MDL_PARAM_TYPE | VARCHAR2 | 40 |  | Yes | This column indicates the LLM parameter type. |
| PROMPT_TMPL_ID | VARCHAR2 | 32 |  | Yes | Foreign key referencing to FAI_PROMPT_TMPLS table. |
| CLOB_VALUE | CLOB |  |  |  | This column indicates the parameter value for CLOB type. |
| NUMBER_VALUE | NUMBER |  |  |  | This column indicates the parameter value for NUMBER type. |
| VARCHAR2_VALUE | VARCHAR2 | 4000 |  |  | This column indicates the parameter value for VARCHAR2 type. |
| TIMESTAMP_VALUE | TIMESTAMP |  |  |  | This column indicates the parameter value for TIMESTAMP type. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_TMPL_MDL_PARAMS_U1 | Unique | Default | TMPL_MDL_PARAM_ID, ORA_SEED_SET1 |
| FAI_TMPL_MDL_PARAMS_U11 | Unique | Default | TMPL_MDL_PARAM_ID, ORA_SEED_SET2 |
| FAI_TMPL_MDL_PARAMS_U2 | Unique | Default | PROMPT_TMPL_ID, TMPL_MDL_PARAM_CODE, ORA_SEED_SET1 |
| FAI_TMPL_MDL_PARAMS_U21 | Unique | Default | PROMPT_TMPL_ID, TMPL_MDL_PARAM_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
