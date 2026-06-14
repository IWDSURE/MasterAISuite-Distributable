# HRC_DL_BO_PP_PARAM_OVERRIDES

HRC_DL_BO_PP_PARAM_OVERRIDES is a table that stores BO level Post process parameters as provided by the user.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** hrc_dl_bo_pp_param_overrides

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlboppparamoverrides-9140.html#hrcdlboppparamoverrides-9140](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlboppparamoverrides-9140.html#hrcdlboppparamoverrides-9140)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BO_PP_PARAM_OVERRID_PK | POST_PROC_PARAM_OVERRIDE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POST_PROC_PARAM_OVERRIDE_ID | NUMBER |  | 18 | Yes | POST_PROC_PARAM_OVERRIDE_ID |
| POST_PROC_PARAM_ID | NUMBER |  | 18 | Yes | POST_PROC_PARAM_ID |
| OVERRIDE_VALUE | VARCHAR2 | 500 |  | Yes | OVERRIDE_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BO_PP_PARAM_OVERRID_N1 | Non Unique | HRC_DL_BO_PP_PARAM_OVERRID_N1 | POST_PROC_PARAM_ID |
| HRC_DL_BO_PP_PARAM_OVERRID_PK | Unique | HRC_DL_BO_PP_PARAM_OVERRID_PK | POST_PROC_PARAM_OVERRIDE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
