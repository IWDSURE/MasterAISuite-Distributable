# FF_FDI_USAGES

This table contains compiler-generated descriptions of database items used in a formula.

## Details

**Schema:** FUSION

**Object owner:** FF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fffdiusages-28778.html#fffdiusages-28778](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/fffdiusages-28778.html#fffdiusages-28778)

## Primary Key

| Name | Columns |
|------|----------|
| FF_FDI_USAGES_PK | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ITEM_NAME, ORA_EDITION_CONTEXT |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FORMULA_ID | NUMBER |  | 18 | Yes | Identifier for the formula the data item usage belongs to. Foreign key to FF_FORMULAS. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ITEM_NAME | VARCHAR2 | 255 |  | Yes | Name of the item the usage is for. |
| DATA_TYPE | VARCHAR2 | 2 |  | Yes | Data type of the formula data item. |
| USAGE | VARCHAR2 | 1 |  | Yes | Subtype field (D, L, I, O, B, U). |
| ITEM_GENERATED_NAME | VARCHAR2 | 30 |  | Yes | System generated bind variable for the item. |
| INDICATOR_VAR_NAME | VARCHAR2 | 30 |  |  | Generated bind variable that indicates whether or not a returned value is not null. |
| LOAD_WHEN_RUNNING | VARCHAR2 | 1 |  | Yes | Y or N flag that indicates whether item gets loaded at runtime. |
| ITEM_ID | NUMBER |  | 18 |  | Usage-specific surrogate key for item. |
| ROUTE_ID | NUMBER |  | 18 |  | Identifier for database item route. Foreign key to FF_ROUTES. |
| USER_ENTITY_ID | NUMBER |  | 18 |  | Identifier for database item user entity. Foreign key to FF_USER_ENTITIES. |
| STATUS | VARCHAR2 | 1 |  |  | Validity status. A status other than V means that the formula needs to be recompiled. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COMPILE_ID | NUMBER |  | 18 | Yes | Identifier for the formula compile. |
| ORA_EDITION_CONTEXT | VARCHAR2 | 30 |  | Yes | Indicates the edition based redefinition (EBR) context to which the row belongs - either 'ALL', ''SET1' or 'SET2'. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FF_FDI_USAGES_FK1 | Non Unique | Default | ROUTE_ID |
| FF_FDI_USAGES_FK2 | Non Unique | Default | USER_ENTITY_ID |
| FF_FDI_USAGES_N1 | Non Unique | Default | UPPER("ITEM_NAME") |
| FF_FDI_USAGES_N2 | Non Unique | Default | ITEM_ID |
| FF_FDI_USAGES_PK | Unique | Default | FORMULA_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ITEM_NAME, ORA_EDITION_CONTEXT |

---

[← Back to Index](../9_Fast_Formula_Tables_Index.md)
