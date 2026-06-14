# PAY_OBJECT_GROUP_LEVELS

This table contains the level of the employment hierarchy that the rule applies to.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgrouplevels-6683.html#payobjectgrouplevels-6683](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjectgrouplevels-6683.html#payobjectgrouplevels-6683)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBJECT_GROUP_LEVELS_PK | OBJECT_GROUP_LEVEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_GROUP_LEVEL_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| OBJECT_GROUP_TYPE_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| NAME_CODE | VARCHAR2 | 30 |  |  | NAME_CODE |
| FORMULA_TYPE_ID | NUMBER |  | 18 |  | Forumla_type_id |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |
| PARAMETER_VO | VARCHAR2 | 200 |  |  | PARAMETER_VO |
| DISPLAY_SEQUENCE | NUMBER |  | 1 | Yes | DISPLAY_SEQUENCE |
| EXCLUDE_AMEND_TYPE | VARCHAR2 | 1 |  |  | Used to indicate which Amend types are not allowed-I(Include not allowed),E(Exclude not allowed),B(no amends allowed) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DEFAULT_QUERY | VARCHAR2 | 4000 |  |  | DEFAULT_QUERY |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_OBJECT_GROUP_LEVELS_N1 | Non Unique | Default | OBJECT_GROUP_TYPE_ID |
| PAY_OBJECT_GROUP_LEVELS_N2 | Non Unique | Default | NAME_CODE |
| PAY_OBJECT_GROUP_LEVELS_N20 | Non Unique | Default | SGUID |
| PAY_OBJECT_GROUP_LEVELS_PK | Unique | Default | OBJECT_GROUP_LEVEL_ID, ORA_SEED_SET1 |
| PAY_OBJECT_GROUP_LEVELS_PK1 | Unique | Default | OBJECT_GROUP_LEVEL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
