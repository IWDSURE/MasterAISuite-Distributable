# HWM_TE_ALT_NAME_VALS_B

This table keeps information about the actual values that are used in the repository when a user selects an alternate name.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtealtnamevalsb-21965.html#hwmtealtnamevalsb-21965](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtealtnamevalsb-21965.html#hwmtealtnamevalsb-21965)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TE_ALT_NAME_VALS_B_PK | TE_ALT_NAME_VAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TE_ALT_NAME_ID | NUMBER |  | 18 |  | foreign key to hxt_te_alt_names |
| TE_ALT_NAME_VAL_ID | NUMBER |  | 18 | Yes | primary key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| NAME | VARCHAR2 | 64 |  |  | NAME |
| WFM_EVENT_IN_OUT | VARCHAR2 | 32 |  |  | WFM_EVENT_IN_OUT |
| DATE_FROM | DATE |  |  |  | DATE_FROM |
| DATE_TO | DATE |  |  |  | DATE_TO |
| ENABLED_FLAG | VARCHAR2 | 20 |  |  | ENABLED_FLAG |
| EXISTING_FLAG | VARCHAR2 | 20 |  |  | EXISTING_FLAG |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDL_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Added as part of webclock new functionality. |
| DISPLAY_SEQUENCE | NUMBER |  | 9 |  | DISPLAY_SEQUENCE |
| WORKER_ACTION_CD | VARCHAR2 | 30 |  |  | WORKER_ACTION_CD |
| MANAGER_ACTION_CD | VARCHAR2 | 30 |  |  | MANAGER_ACTION_CD |
| TL_MGR_ACTION_CD | VARCHAR2 | 30 |  |  | Indicates time and labor manager actions allowed for reported time entries. |
| ENABLE_CO_FLAG | VARCHAR2 | 30 |  |  | ENABLE_CO_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| LINE_MGR_ACTION_CD | VARCHAR2 | 30 |  |  | Indicates Line manager actions allowed for reported time entries. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TE_ALT_NAME_VALS_B_N1 | Non Unique | Default | TE_ALT_NAME_ID |
| HWM_TE_ALT_NAME_VALS_B_U1 | Unique | Default | TE_ALT_NAME_VAL_ID, ORA_SEED_SET1 |
| HWM_TE_ALT_NAME_VALS_B_U11 | Unique | Default | TE_ALT_NAME_VAL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
