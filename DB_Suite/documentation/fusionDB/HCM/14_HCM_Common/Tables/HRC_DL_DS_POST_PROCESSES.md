# HRC_DL_DS_POST_PROCESSES

HRC_DL_DS_POST_PROCESSES table contains the seeded information of the data set level Post Processes that have to be invoked after the data load is complete.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldspostprocesses-3574.html#hrcdldspostprocesses-3574](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdldspostprocesses-3574.html#hrcdldspostprocesses-3574)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_DS_POST_PROCESSES_PK | POST_PROC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POST_PROC_ID | NUMBER |  | 18 | Yes | POST_PROC_ID |
| POST_PROC_NAME | VARCHAR2 | 100 |  | Yes | POST_PROC_NAME |
| POST_PROC_TYPE | VARCHAR2 | 100 |  |  | POST_PROC_TYPE |
| POST_PROC_JOB_FQ_DEFN_NAME | VARCHAR2 | 256 |  | Yes | POST_PROC_JOB_FQ_DEFN_NAME |
| POST_PROC_JOB_FQ_CLASS_NAME | VARCHAR2 | 256 |  | Yes | POST_PROC_JOB_FQ_CLASS_NAME |
| POST_PROC_TASK_NAME | VARCHAR2 | 256 |  |  | POST_PROC_TASK_NAME |
| INTEGRATION_TYPE | VARCHAR2 | 30 |  | Yes | INTEGRATION_TYPE |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| POST_PROC_ENABLED | VARCHAR2 | 1 |  |  | POST_PROC_ENABLED |
| CONFIG_ENABLED | VARCHAR2 | 1 |  |  | CONFIG_ENABLED |
| OVERRIDE_ENABLED | VARCHAR2 | 1 |  |  | OVERRIDE_ENABLED |
| DEFAULT_SUBMIT_VALUE | VARCHAR2 | 1 |  |  | DEFAULT_SUBMIT_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PROCESSING_ORDER | NUMBER |  | 18 |  | PROCESSING_ORDER |
| TERMINAL_ACTION | VARCHAR2 | 256 |  |  | TERMINAL_ACTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_DS_POST_PROCESSES_U1 | Unique | Default | POST_PROC_ID, ORA_SEED_SET1 |
| HRC_DL_DS_POST_PROCESSES_U11 | Unique | Default | POST_PROC_ID, ORA_SEED_SET2 |
| HRC_DL_DS_POST_PROCESSES_U2 | Unique | Default | POST_PROC_NAME, ORA_SEED_SET1 |
| HRC_DL_DS_POST_PROCESSES_U21 | Unique | Default | POST_PROC_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
