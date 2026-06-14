# HWM_GRP_CRITERIA

Contains Criteria for Group Defintion

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpcriteria-16462.html#hwmgrpcriteria-16462](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmgrpcriteria-16462.html#hwmgrpcriteria-16462)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_GRP_CRITERIA_PK | GRP_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_CRITERIA_ID | NUMBER |  | 18 | Yes | GRP_CRITERIA_ID |
| ADDL_ATTR_CATEGORY | VARCHAR2 | 30 |  |  | ADDL_ATTR_CATEGORY |
| ADDL_ATTR_CHAR1 | VARCHAR2 | 150 |  |  | ADDL_ATTR_CHAR1 |
| ADDL_ATTR_CHAR2 | VARCHAR2 | 150 |  |  | ADDL_ATTR_CHAR2 |
| ADDL_ATTR_CHAR3 | VARCHAR2 | 150 |  |  | ADDL_ATTR_CHAR3 |
| ADDL_ATTR_CHAR4 | VARCHAR2 | 150 |  |  | ADDL_ATTR_CHAR4 |
| ADDL_ATTR_CHAR5 | VARCHAR2 | 150 |  |  | ADDL_ATTR_CHAR5 |
| ADDL_ATTR_NUMBER1 | NUMBER |  |  |  | ADDL_ATTR_NUMBER1 |
| ADDL_ATTR_NUMBER2 | NUMBER |  |  |  | ADDL_ATTR_NUMBER2 |
| ADDL_ATTR_NUMBER3 | NUMBER |  |  |  | ADDL_ATTR_NUMBER3 |
| ADDL_ATTR_NUMBER4 | NUMBER |  |  |  | ADDL_ATTR_NUMBER4 |
| ADDL_ATTR_NUMBER5 | NUMBER |  |  |  | ADDL_ATTR_NUMBER5 |
| GRP_ID | NUMBER |  | 18 |  | GRP_ID |
| ORDR_NUM | NUMBER |  | 9 |  | ORDR_NUM |
| LEFT_PARAM_NUM | NUMBER |  | 9 |  | LEFT_PARAM_NUM |
| CRITERIA_ID | NUMBER |  | 18 |  | CRITERIA_ID |
| CRITERIA_NAME | VARCHAR2 | 500 |  |  | CRITERIA_NAME |
| CRITERIA_DISPLAY_NAME | VARCHAR2 | 500 |  |  | CRITERIA_DISPLAY_NAME |
| OPERATOR_ID | NUMBER |  | 18 |  | OPERATOR_ID |
| OPERATOR_NAME | VARCHAR2 | 100 |  |  | OPERATOR_NAME |
| RIGHT_PARAM_NUM | NUMBER |  | 9 |  | RIGHT_PARAM_NUM |
| VALUE_CHAR | VARCHAR2 | 30 |  |  | VALUE_CHAR |
| VALUE_NUMBER | NUMBER |  | 18 |  | VALUE_NUMBER |
| VALUE_DATE | DATE |  |  |  | VALUE_DATE |
| VALUE_TS | TIMESTAMP |  |  |  | VALUE_TS |
| BOOL_OPER_CD | VARCHAR2 | 30 |  |  | BOOL_OPER_CD |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_GRP_CRITERIA_N1 | Non Unique | Default | GRP_ID |
| HWM_GRP_CRITERIA_U1 | Unique | FUSION_TS_TX_DATA | GRP_CRITERIA_ID, ORA_SEED_SET1 |
| HWM_GRP_CRITERIA_U11 | Unique | FUSION_TS_TX_DATA | GRP_CRITERIA_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
