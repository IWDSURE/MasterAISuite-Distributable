# PAY_ACTION_MATRIX

Action Matrix controls what action is available in which context

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionmatrix-4186.html#payactionmatrix-4186](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionmatrix-4186.html#payactionmatrix-4186)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_MATRIX_PK | ACTION_MATRIX_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_MATRIX_ID | NUMBER |  | 18 | Yes | ACTION_MATRIX_ID |
| CURRENT_NODE_STATUS | VARCHAR2 | 50 |  | Yes | CURRENT_NODE_STATUS |
| SUCCEEDING_NODE_STATUS | VARCHAR2 | 50 |  |  | SUCCEEDING_NODE_STATUS |
| TASK_TYPE | VARCHAR2 | 20 |  |  | TASK_TYPE |
| AVAILABLE_ACTION | VARCHAR2 | 50 |  |  | AVAILABLE_ACTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | ACTIVE_FLAG |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ACTION_MATRIX_PK | Unique | Default | ACTION_MATRIX_ID, ORA_SEED_SET1 |
| PAY_ACTION_MATRIX_PK1 | Unique | Default | ACTION_MATRIX_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
