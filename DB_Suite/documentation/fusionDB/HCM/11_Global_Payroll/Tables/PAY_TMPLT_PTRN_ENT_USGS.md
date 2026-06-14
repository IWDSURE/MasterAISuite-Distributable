# PAY_TMPLT_PTRN_ENT_USGS

This entity indicates which records are applicable for a given design pattern.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltptrnentusgs-14002.html#paytmpltptrnentusgs-14002](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltptrnentusgs-14002.html#paytmpltptrnentusgs-14002)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_PTRN_ENT_USGS_PK | PTRN_ENT_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PTRN_ENT_USAGE_ID | NUMBER |  | 18 | Yes | PTRN_ENT_USAGE_ID |
| BASE_PTRN_ENT_USAGE_ID | NUMBER |  | 18 | Yes | BASE_PTRN_ENT_USAGE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PATTERN_ID | NUMBER |  | 18 |  | PATTERN_ID |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | ENTITY_TYPE |
| RULE_VALUE | VARCHAR2 | 20 |  |  | RULE_VALUE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_PTRN_ENT_USGS_PK | Unique | Default | PTRN_ENT_USAGE_ID |
| PAY_TMPLT_PTRN_ENT_USGS_U1 | Unique | Default | PATTERN_ID, ENTITY_ID, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
