# HWM_TL_TASK_FEATURES

This table stores list of all tasks and layouts for one layout set

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtltaskfeatures-30962.html#hwmtltaskfeatures-30962](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtltaskfeatures-30962.html#hwmtltaskfeatures-30962)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TL_TASK_FEATURES_PK | TL_TASK_FEATURES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TL_TASK_FEATURES_ID | NUMBER |  | 18 | Yes | TL_TASK_FEATURES_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TASK_NAME | VARCHAR2 | 256 |  | Yes | TASK_NAME |
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

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TL_TASK_FEATURES_U1 | Unique | Default | TL_TASK_FEATURES_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
