# PER_TASK_DEPENDENCIES

PER_TASK_DEPENDENCIES : This table holds dependent task details

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertaskdependencies-12284.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertaskdependencies-12284.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_TASK_DEPENDENCIES_PK | TASK_DEPENDENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_DEPENDENCY_ID | NUMBER |  | 18 | Yes | TASK_DEPENDENCY_ID |
| CHECKLIST_ID | NUMBER |  | 18 |  | CHECKLIST_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | OBSOLETE_FLAG |
| TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | TASK_IN_CHECKLIST_ID |
| DEPENDENCY_TYPE | VARCHAR2 | 30 |  | Yes | DEPENDENCY_TYPE |
| DEPENDENT_TASK_IN_CHECKLIST_ID | NUMBER |  | 18 | Yes | DEPENDENT_TASK_IN_CHECKLIST_ID |
| ACTIVATION_ELIGY_PRFL_ID | NUMBER |  | 18 |  | ACTIVATION_ELIGY_PRFL_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_TASK_DEPENDENCIES_N1 | Non Unique | FUSION_TS_TX_DATA | TASK_IN_CHECKLIST_ID |
| PER_TASK_DEPENDENCIES_N2 | Non Unique | FUSION_TS_TX_DATA | DEPENDENT_TASK_IN_CHECKLIST_ID |
| PER_TASK_DEPENDENCIES_N20 | Non Unique | Default | SGUID |
| PER_TASK_DEPENDENCIES_N3 | Non Unique | Default | CHECKLIST_ID |
| PER_TASK_DEPENDENCIES_U1 | Unique | Default | TASK_DEPENDENCY_ID, ORA_SEED_SET1 |
| PER_TASK_DEPENDENCIES_U11 | Unique | Default | TASK_DEPENDENCY_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
