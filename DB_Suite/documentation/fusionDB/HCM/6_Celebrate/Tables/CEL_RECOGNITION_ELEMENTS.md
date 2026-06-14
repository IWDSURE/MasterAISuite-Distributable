# CEL_RECOGNITION_ELEMENTS

Table to hold award amount and element details.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celrecognitionelements-28506.html#celrecognitionelements-28506](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celrecognitionelements-28506.html#celrecognitionelements-28506)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_RECOGNITION_ELEMENTS_PK | RECOGNITION_ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOGNITION_ELEMENT_ID | NUMBER |  | 18 | Yes | Unique identifier of a recognition element |
| RECOGNITION_ID | NUMBER |  | 18 | Yes | Unique identifier of a recognition |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program Identifier |
| PERSON_ID | NUMBER |  | 18 | Yes | Unique identifier of a person |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Unique identifier of an assignment |
| PROGRAM_ELEMENT_ID | NUMBER |  | 18 |  | Program Element Identifier |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element Type Identifier |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Input Value Identifier |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group Identifier |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity Identifier |
| VALUE | NUMBER |  |  |  | Value |
| INPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | Input Currency Code |
| POSTED_FLAG | VARCHAR2 | 1 |  |  | Flag that indictaes if element entry is posted |
| POSTED_DATE | TIMESTAMP |  |  |  | Date of posting |
| RUN_ID | NUMBER |  | 18 |  | Run Identifier |
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
| CEL_RECOGNITION_ELEMENTS_N1 | Non Unique | Default | RECOGNITION_ID |
| CEL_RECOGNITION_ELEMENTS_PK | Unique | Default | RECOGNITION_ELEMENT_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
