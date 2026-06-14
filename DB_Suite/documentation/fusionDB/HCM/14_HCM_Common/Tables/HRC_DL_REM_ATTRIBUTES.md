# HRC_DL_REM_ATTRIBUTES

Table for storing supported Attributes for each Business Objects. Only UPDATABLE Entities will have data in this table.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremattributes-22620.html#hrcdlremattributes-22620](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremattributes-22620.html#hrcdlremattributes-22620)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_ATTRIBUTES_PK | ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTRIBUTE_ID | NUMBER |  |  | Yes | Primary Key |
| BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | BUSINESS_OBJECT_ID |
| ENTITY_ID | NUMBER |  |  | Yes | FK to HRC_DL_REM_ENTITIES |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | Attribute Name from the HDL supported View Object |
| ATTR_LOOKUPTYPE | VARCHAR2 | 30 |  | Yes | Allowed Attribute Types. 

UPDATE  - Only be UPDATED
UPDATE_DELETE - Can be NULLIFIED (or) Updated with standard values.

Values for few attributes can be UPDATED (or) REMOVED completely. 


However, few can only be UPDATED. For example, SalaryAmount in Salary Business Object. We cannot nullify the field. Hence, default value has to be provided always.



Following can be configured by customer.

UPDATE      - can be updated by the customer. Will have a DEFAULT Value
DELETE       - #NULL

Non-configurable by customer and hidden from the UI.

CONSTANT -  Takes the fixed DEFAULT Value and populates the same in the dat file. Example : ACTION_CODE :  TERMINATION

KEY -  Populates the field based on the value from the DB. Few BO's need some additional KEY Attributes for the object to load.

DERIVED - Combination of string and derived dependent attribute value. For example, "AssignmentNumber" can be updated as  "MASKED-{ AssignmentId}  Example :  MASKED-100, where 100 is AssignmentId |
| CUSTOM_EDITABLE | VARCHAR2 | 1 |  |  | N- Will not be available for customers for modification.
Y- Available |
| DEFAULT_VALUE | VARCHAR2 | 4000 |  |  | For Mandatory Attributes, Default value will be seeded |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_ATTRIBUTES_N1 | Non Unique | Default | ENTITY_ID |
| HRC_DL_REM_ATTRIBUTES_N2 | Non Unique | Default | CUSTOM_EDITABLE |
| HRC_DL_REM_ATTRIBUTES_U1 | Unique | Default | ATTRIBUTE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
