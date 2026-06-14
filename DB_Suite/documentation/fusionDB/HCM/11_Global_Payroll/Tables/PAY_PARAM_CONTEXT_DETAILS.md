# PAY_PARAM_CONTEXT_DETAILS

this we will be utilizing in storing context value for a parameter

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payparamcontextdetails-16437.html#payparamcontextdetails-16437](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payparamcontextdetails-16437.html#payparamcontextdetails-16437)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PARAM_CONTEXT_DETAILS_PK | CONTEXT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEXT_DETAIL_ID | NUMBER |  | 18 | Yes | primary key for the table pay_param_context_details. |
| PARAM_CONTEXT_ID | NUMBER |  | 18 |  | this column refres to parent table pay_param_context column param_context_id. |
| CONTEXT_KEY | VARCHAR2 | 50 |  |  | this column will store alt key , contxt key for a task parameter. |
| CONTEXT_VALUE | VARCHAR2 | 2400 |  |  | this column will store the value for the context key as security handler. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PARAM_CONTEXT_DETAILS_PK | Unique | Default | CONTEXT_DETAIL_ID, ORA_SEED_SET1 |
| PAY_PARAM_CONTEXT_DETAILS_PK1 | Unique | Default | CONTEXT_DETAIL_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
