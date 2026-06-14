# HWM_TL_TASK_RESULTS

Task results determined by answers

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtltaskresults-26086.html#hwmtltaskresults-26086](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtltaskresults-26086.html#hwmtltaskresults-26086)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TL_TASK_RESULTS_PK | TL_TASK_RESULTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TL_TASK_RESULTS_ID | NUMBER |  | 18 | Yes | TL_TASK_RESULTS_ID |
| TL_TASK_FEATURES_ID | NUMBER |  | 18 | Yes | TL_TASK_FEATURES_ID |
| TL_ANSWER_SET_ID | NUMBER |  | 18 | Yes | TL_ANSWER_SET_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | 'Y' if task is enabled for this layout set based on questionnaire input. |
| COMPLETED_FLAG | VARCHAR2 | 1 |  |  | 'Y' if user marks the task as completed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| TL_TASK_RESULTS_CD | VARCHAR2 | 160 |  |  | used for seed data |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TL_TASK_RESULTS_N20 | Non Unique | Default | SGUID |
| HWM_TL_TASK_RESULTS_U1 | Unique | Default | TL_TASK_RESULTS_ID, ORA_SEED_SET1 |
| HWM_TL_TASK_RESULTS_U11 | Unique | Default | TL_TASK_RESULTS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
