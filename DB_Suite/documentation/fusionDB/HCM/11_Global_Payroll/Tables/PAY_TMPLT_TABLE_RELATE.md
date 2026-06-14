# PAY_TMPLT_TABLE_RELATE

This Entity stores the relationship details of tables seeded in Table Information & Table Column Information

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmplttablerelate-10679.html#paytmplttablerelate-10679](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmplttablerelate-10679.html#paytmplttablerelate-10679)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_TABLE_RELATE_PK | TABLE_RELATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TABLE_RELATE_ID | NUMBER |  | 18 | Yes | TABLE_RELATE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PARENT_TABLE_ID | NUMBER |  | 18 | Yes | PARENT_TABLE_ID |
| PARENT_COL_ID | NUMBER |  | 18 | Yes | PARENT_COL_ID |
| CHILD_TABLE_ID | NUMBER |  | 18 | Yes | CHILD_TABLE_ID |
| CHILD_COL_ID | NUMBER |  | 18 | Yes | CHILD_COL_ID |
| RELATION_TYPE | VARCHAR2 | 1 |  |  | RELATION_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_TABLE_RELATE_N20 | Non Unique | Default | SGUID |
| PAY_TMPLT_TABLE_RELATE_PK | Unique | Default | TABLE_RELATE_ID, ORA_SEED_SET1 |
| PAY_TMPLT_TABLE_RELATE_PK1 | Unique | Default | TABLE_RELATE_ID, ORA_SEED_SET2 |
| PAY_TMPLT_TABLE_RELATE_UK1 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, PARENT_TABLE_ID, PARENT_COL_ID, CHILD_TABLE_ID, CHILD_COL_ID, ORA_SEED_SET1 |
| PAY_TMPLT_TABLE_RELATE_UK11 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, PARENT_TABLE_ID, PARENT_COL_ID, CHILD_TABLE_ID, CHILD_COL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
