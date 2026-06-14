# CMP_ATTRIBUTE_ELEMENTS

Stores elements attached to a plan attribute.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattributeelements-30556.html#cmpattributeelements-30556](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpattributeelements-30556.html#cmpattributeelements-30556)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ATTRIBUTE_ELEMENTS_PK | ATTRIBUTE_ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTRIBUTE_ELEMENT_ID | NUMBER |  | 18 | Yes | ATTRIBUTE_ELEMENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| COMP_TYPE | VARCHAR2 | 30 |  |  | COMP_TYPE |
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | PLAN_ATTRIBUTE_ID |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | INPUT_VALUE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ATTRIBUTE_ELEMENTS_N2 | Non Unique | Default | ELEMENT_TYPE_ID |
| CMP_ATTRIBUTE_ELEMENTS_N3 | Non Unique | Default | INPUT_VALUE_ID |
| CMP_ATTRIBUTE_ELEMENTS_N4 | Non Unique | Default | COMP_TYPE |
| CMP_ATTRIBUTE_ELEMENTS_UK2 | Unique | Default | ATTRIBUTE_ELEMENT_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
