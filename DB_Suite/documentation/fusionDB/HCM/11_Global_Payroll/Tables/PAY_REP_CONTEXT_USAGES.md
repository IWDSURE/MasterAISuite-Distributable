# PAY_REP_CONTEXT_USAGES

Internal table to be used by archive process if context usages are required to be stored.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrepcontextusages-10345.html#payrepcontextusages-10345](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrepcontextusages-10345.html#payrepcontextusages-10345)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REP_CONTEXT_USAGES_PK | REP_CONTEXT_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REP_CONTEXT_USAGE_ID | NUMBER |  | 18 | Yes | REP_CONTEXT_USAGE_ID |  |
| DATABASE_ITEM_ID | NUMBER |  | 18 | Yes | DATABASE_ITEM_ID |  |
| CONTEXT_ID | NUMBER |  | 18 | Yes | Identifier for the context. Foreign key to FF_CONTEXTS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_REP_CONTEXT_USAGES_PK | Unique | Default | REP_CONTEXT_USAGE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
