# PAY_DIMENSION_ROUTES

This table contains additional route information for balance dimensions.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydimensionroutes-6542.html#paydimensionroutes-6542](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydimensionroutes-6542.html#paydimensionroutes-6542)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIMENSION_ROUTES_PK | BALANCE_DIMENSION_ID, PRIORITY |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BALANCE_DIMENSION_ID | NUMBER |  | 18 | Yes | Foreign key to pay_balance_dimensions. |
| ROUTE_ID | NUMBER |  | 18 |  | Foreign key to ff_routes. |
| ROUTE_TYPE | VARCHAR2 | 30 |  | Yes | Either 'RR' for run result route or 'RB' for run balance route. |
| PRIORITY | NUMBER |  | 5 | Yes | Prioritises dimension route relationships. |
| RUN_DIMENSION_ID | NUMBER |  | 18 |  | Run level balance dimension id. Also a foreign key to pay_balance_dimensions. |
| BALANCE_TYPE_COLUMN | VARCHAR2 | 80 |  |  | Denotes the join to balance types that need to be used in the route |
| RETRIEVAL_COLUMN | VARCHAR2 | 2000 |  |  | Used in Non Payroll applications to indicated the name of the column to be summed. |
| OPTIMIZER_HINT | VARCHAR2 | 2000 |  |  | OPTIMIZER_HINT |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_DIMENSION_ROUTES_PK | Unique | Default | BALANCE_DIMENSION_ID, PRIORITY, ORA_SEED_SET1 |
| PAY_DIMENSION_ROUTES_PK1 | Unique | Default | BALANCE_DIMENSION_ID, PRIORITY, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
