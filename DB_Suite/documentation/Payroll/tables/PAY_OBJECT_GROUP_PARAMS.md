# PAY_OBJECT_GROUP_PARAMS

This table contains the parameters that define an object group, such as the payroll name for an assignment group.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroupparams-10393.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgroupparams-10393.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBJECT_GROUP_PARAMS_PK | OBJECT_GROUP_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_GROUP_PARAM_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_PARAM_ID |
| OBJECT_GROUP_TYPE_PARAM_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_TYPE_PARAM_ID |
| OBJECT_GROUP_ID | NUMBER |  | 18 | Yes | OBJECT_GROUP_ID |
| PARAM_VALUE | VARCHAR2 | 30 |  | Yes | PARAM_VALUE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_OBJECT_GROUP_PARAMS_PK | Unique | Default | OBJECT_GROUP_PARAM_ID, ORA_SEED_SET1 |
| PAY_OBJECT_GROUP_PARAMS_PK1 | Unique | Default | OBJECT_GROUP_PARAM_ID, ORA_SEED_SET2 |
| PAY_OBJECT_GROUP_PARAMS_U1 | Unique | Default | OBJECT_GROUP_ID, OBJECT_GROUP_TYPE_PARAM_ID, ORA_SEED_SET1 |
| PAY_OBJECT_GROUP_PARAMS_U11 | Unique | Default | OBJECT_GROUP_ID, OBJECT_GROUP_TYPE_PARAM_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
