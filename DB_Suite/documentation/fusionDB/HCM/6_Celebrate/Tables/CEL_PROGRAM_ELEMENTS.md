# CEL_PROGRAM_ELEMENTS

Table for element mapping of award programs

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramelements-17590.html#celprogramelements-17590](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramelements-17590.html#celprogramelements-17590)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_PROGRAM_ELEMENTS_PK | PROGRAM_ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROGRAM_ELEMENT_ID | NUMBER |  | 18 | Yes | Program Element Identifier |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program Identifier |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group Identifier |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code |
| INPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | Input Currency Code |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element Type Identifier |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Input Value Identifier |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity Identifier |
| FIXED_VALUE | NUMBER |  |  |  | Fixed value for the element entry |
| MINIMUM_VALUE | NUMBER |  |  |  | Minimum allowed value for the element entry |
| MAXIMUM_VALUE | NUMBER |  |  |  | Maximum allowed value for the element entry |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_PROGRAM_ELEMENTS_N1 | Non Unique | Default | PROGRAM_ID |
| CEL_PROGRAM_ELEMENTS_PK | Unique | Default | PROGRAM_ELEMENT_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
