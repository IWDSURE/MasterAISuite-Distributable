# PAY_ACTION_PARAM_VALUES

This table contains parameter values that control certain processes, such as payroll runs.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionparamvalues-29630.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionparamvalues-29630.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ACTION_PARAM_VALUES_PK | PARAMETER_NAME, ACTION_PARAM_GROUP_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAMETER_NAME | VARCHAR2 | 30 |  | Yes | PARAMETER_NAME |
| PARAMETER_VALUE | VARCHAR2 | 80 |  | Yes | PARAMETER_VALUE |
| ACTION_PARAM_GROUP_ID | NUMBER |  | 18 | Yes | ACTION_PARAM_GROUP_ID |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ACTION_PARAM_VALUES_PK | Unique | Default | PARAMETER_NAME, ACTION_PARAM_GROUP_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| PAY_ACTION_PARAM_VALUES_PK1 | Unique | Default | PARAMETER_NAME, ACTION_PARAM_GROUP_ID, ENTERPRISE_ID, ORA_SEED_SET2 |
| PAY_ACTION_PARAM_VALUES_U1 | Unique | Default | PARAMETER_NAME, PARAMETER_VALUE, ACTION_PARAM_GROUP_ID, ENTERPRISE_ID, ORA_SEED_SET1 |
| PAY_ACTION_PARAM_VALUES_U11 | Unique | Default | PARAMETER_NAME, PARAMETER_VALUE, ACTION_PARAM_GROUP_ID, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
