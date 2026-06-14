# PAY_TEMPLATE_CORE_OBJECTS

Template Core Object keeps track of the core schema objects generated from element templates. e.g. Elements, Input Values, Formulas, Formula results, balances, balance feeds etc. created by Template

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemplatecoreobjects-15529.html#paytemplatecoreobjects-15529](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytemplatecoreobjects-15529.html#paytemplatecoreobjects-15529)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TEMPLATE_CORE_OBJECTS_PK | TEMPLATE_CORE_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_CORE_OBJECT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ELEMENT_TEMPLATES. |
| CORE_OBJECT_ID | NUMBER |  | 18 | Yes | Primary key of the generated core object. |
| SHADOW_OBJECT_ID | NUMBER |  | 18 | Yes | Primary key of the shadow schema object used to generate the core schema object. |
| TABLE_ID | NUMBER |  | 18 |  | TABLE_ID |
| ACTION | VARCHAR2 | 30 |  |  | ACTION |
| PROCESS_STATUS | VARCHAR2 | 30 |  |  | PROCESS_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TEMPLATE_CORE_OBJECTS_N1 | Non Unique | Default | CORE_OBJECT_ID |
| PAY_TEMPLATE_CORE_OBJECTS_PK | Unique | Default | TEMPLATE_CORE_OBJECT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
