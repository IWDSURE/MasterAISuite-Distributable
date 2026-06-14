# PAY_RATE_ELEMENT_INDIRECTS

This table is used by the Rates process to identify the indirect Element Types of an Element Type.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrateelementindirects-8908.html#payrateelementindirects-8908](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrateelementindirects-8908.html#payrateelementindirects-8908)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RATE_ELEMENT_INDIRECT_PK | RATE_ELEMENT_INDIRECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RATE_ELEMENT_INDIRECT_ID | NUMBER |  | 18 | Yes | Primary key |
| BASE_ET_ID | NUMBER |  | 18 | Yes | The Base Element  of the Element Type |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | The Element Type of the Indirect. |
| INDIRECT_ET_ID | NUMBER |  | 18 | Yes | The Indirect ELement Type Id |
| DEP_LEVEL | NUMBER |  | 18 | Yes | Level of the Indirect |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_RATE_ELE_INDIRECTS_N1 | Non Unique | Default | BASE_ET_ID |
| PAY_RATE_ELE_INDIRECTS_PK | Unique | Default | RATE_ELEMENT_INDIRECT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
