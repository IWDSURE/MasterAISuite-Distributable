# HWM_TL_TASK_FEATURES_B

This table stores list of all tasks and layouts for one layout set

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtltaskfeaturesb-19228.html#hwmtltaskfeaturesb-19228](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtltaskfeaturesb-19228.html#hwmtltaskfeaturesb-19228)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TL_TASK_FEATURES_B_PK | TL_TASK_FEATURES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TL_TASK_FEATURES_ID | NUMBER |  | 18 | Yes | TL_TASK_FEATURES_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TASK_SHORT_NAME | VARCHAR2 | 256 |  | Yes | TASK_SHORT_NAME |
| LOGIC_EXPRESION | VARCHAR2 | 256 |  |  | LOGIC_EXPRESION |
| TYPE | VARCHAR2 | 256 |  | Yes | TYPE |
| URL_RESOURCE | VARCHAR2 | 256 |  | Yes | URL_RESOURCE |
| SEQUENCE_NUM | NUMBER |  | 18 | Yes | SEQUENCE_NUM |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TL_TASK_FEATURES_B_U1 | Unique | FUSION_TS_TX_IDX | TL_TASK_FEATURES_ID, ORA_SEED_SET1 |
| HWM_TL_TASK_FEATURES_B_U11 | Unique | FUSION_TS_TX_IDX | TL_TASK_FEATURES_ID, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
