# PAY_PARAM_CONTEXTS_B

this we will be utilizing in storing context name of parameter for security

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payparamcontextsb-23744.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payparamcontextsb-23744.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PARAM_CONTEXTS_B_PK | PARAM_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAM_CONTEXT_ID | NUMBER |  | 18 | Yes | primary key for the table pay_param_contexts_b. |
| BASE_CONTEXT_NAME | VARCHAR2 | 200 |  | Yes | Used to store context name of a parameter. |
| PERSIST_FLAG | VARCHAR2 | 2 |  |  | Y,Y implies the value will be denormalized as a context value. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PARAM_CONTEXTS_B_PK | Unique | Default | PARAM_CONTEXT_ID, ORA_SEED_SET1 |
| PAY_PARAM_CONTEXTS_B_PK1 | Unique | Default | PARAM_CONTEXT_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
