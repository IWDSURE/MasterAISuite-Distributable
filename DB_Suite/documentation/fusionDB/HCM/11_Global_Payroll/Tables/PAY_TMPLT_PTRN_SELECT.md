# PAY_TMPLT_PTRN_SELECT

This holds the pattern selection based on the available list of patterns for a given Functional Area. E.g. For back dated changes there can be two patterns, one being the full recalculation and other being the partial recalculation. In here US legislation might prefer the full recalculation.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltptrnselect-9116.html#paytmpltptrnselect-9116](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltptrnselect-9116.html#paytmpltptrnselect-9116)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_PTRN_SELECT_PK | PTRN_SELECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PTRN_SELECT_ID | NUMBER |  | 18 | Yes | PTRN_SELECT_ID |
| BASE_PTRN_SELECT_ID | NUMBER |  | 18 | Yes | BASE_PTRN_SELECT_ID |
| PATTERN_ID | NUMBER |  | 18 | Yes | PATTERN_ID |
| FUN_AREA_ID | NUMBER |  | 18 | Yes | FUN_AREA_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | NUMBER |  | 18 |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_PTRN_SELECT_PK | Unique | Default | PTRN_SELECT_ID |
| PAY_TMPLT_PTRN_SELECT_U1 | Unique | Default | PATTERN_ID, FUN_AREA_ID, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
