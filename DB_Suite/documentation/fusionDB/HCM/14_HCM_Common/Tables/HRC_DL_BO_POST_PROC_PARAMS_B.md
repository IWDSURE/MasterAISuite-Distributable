# HRC_DL_BO_POST_PROC_PARAMS_B

HRC_DL_BO_POST_PROC_PARAMS_B is a standard base table used to store the Parameters for a Business Object level Post Process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbopostprocparamsb-3142.html#hrcdlbopostprocparamsb-3142](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbopostprocparamsb-3142.html#hrcdlbopostprocparamsb-3142)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BO_POST_PROC_PARAMS_PK | POST_PROC_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POST_PROC_PARAM_ID | NUMBER |  | 18 | Yes | POST_PROC_PARAM_ID |
| POST_PROC_ID | NUMBER |  | 18 | Yes | POST_PROC_ID |
| POST_PROC_PARAM_KEY | VARCHAR2 | 500 |  | Yes | POST_PROC_PARAM_KEY |
| PARAM_DEFAULT_VALUE | VARCHAR2 | 100 |  |  | PARAM_DEFAULT_VALUE |
| PARAM_VALUE_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | PARAM_VALUE_LOOKUP_TYPE |
| OVERRIDE_ENABLED | VARCHAR2 | 10 |  | Yes | OVERRIDE_ENABLED |
| POST_PROC_PARAM_ENABLED | VARCHAR2 | 10 |  | Yes | POST_PROC_PARAM_ENABLED |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BO_POST_PROC_PARAMS_U1 | Unique | HRC_DL_BO_POST_PROC_PARAMS_U1 | POST_PROC_PARAM_ID, ORA_SEED_SET1 |
| HRC_DL_BO_POST_PROC_PARAMS_U2 | Unique | HRC_DL_BO_POST_PROC_PARAMS_U2 | POST_PROC_PARAM_ID, ORA_SEED_SET2 |
| HRC_DL_BO_POST_PROC_PARAMS_U3 | Unique | HRC_DL_BO_POST_PROC_PARAMS_U3 | POST_PROC_ID, POST_PROC_PARAM_KEY, ORA_SEED_SET1 |
| HRC_DL_BO_POST_PROC_PARAMS_U4 | Unique | HRC_DL_BO_POST_PROC_PARAMS_U4 | POST_PROC_ID, POST_PROC_PARAM_KEY, ORA_SEED_SET2 |
| HRC_DL_BO_PP_PARAMS_N20 | Non Unique | HRC_DL_BO_PP_PARAMS_N20 | SGUID, ORA_SEED_SET1 |
| HRC_DL_BO_PP_PARAMS_N201 | Non Unique | HRC_DL_BO_PP_PARAMS_N201 | SGUID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
