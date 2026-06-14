# FF_ROUTE_CONTEXT_USAGES

This table contains a single usage of a context as a bind variable in the ROUTE SQLstatement.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffroutecontextusages-10664.html#ffroutecontextusages-10664](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ffroutecontextusages-10664.html#ffroutecontextusages-10664)

## Primary Key

| Name | Columns |
|------|----------|
| FF_ROUTE_CONTEXT_USAGES_PK | ROUTE_ID, CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROUTE_ID | NUMBER |  | 18 | Yes | Identifier for route the context usage belongs to. Foreign key to FF_ROUTES. |
| CONTEXT_ID | NUMBER |  | 18 | Yes | Identifier for the context. Foreign key to FF_CONTEXTS. |
| SEQUENCE_NO | NUMBER |  | 2 | Yes | Cross reference to the contexts place in the FROM text. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_ROUTE_CONTEXT_USAGES_N20 | Non Unique | Default | SGUID |
| FF_ROUTE_CONTEXT_USAGES_PK | Unique | Default | ROUTE_ID, CONTEXT_ID, ORA_SEED_SET1 |
| FF_ROUTE_CONTEXT_USAGES_PK1 | Unique | Default | ROUTE_ID, CONTEXT_ID, ORA_SEED_SET2 |
| FF_ROUTE_CONTEXT_USAGES_UK1 | Unique | Default | ROUTE_ID, SEQUENCE_NO, ORA_SEED_SET1 |
| FF_ROUTE_CONTEXT_USAGES_UK11 | Unique | Default | ROUTE_ID, SEQUENCE_NO, ORA_SEED_SET2 |
| FF_ROUTE_CONTEXT_USAGE_FK1 | Non Unique | Default | CONTEXT_ID |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
