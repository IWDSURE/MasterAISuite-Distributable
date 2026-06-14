# HRC_DL_REM_TMPL_ATTRIBUTES

Attributes which are UPDATE_DELETE,DELETE,UPDATE are allowed for edits by the customer. Rest of the attributes are not available for customer edits in the User Interface.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplattributes-7709.html#hrcdlremtmplattributes-7709](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplattributes-7709.html#hrcdlremtmplattributes-7709)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_TMPL_ATTRIBUTES_PK | TMPL_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TMPL_ATTRIBUTE_ID | NUMBER |  |  | Yes | Primary Key |
| TMPL_ENTITY_ID | NUMBER |  |  | Yes | FK to HRC_DL_REM_TXN_ENTITIES |
| BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | BUSINESS_OBJECT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | ATTRIBUTE_NAME |
| ATTR_LOOKUPTYPE | VARCHAR2 | 30 |  |  | ATTR_LOOKUPTYPE |
| CUSTOM_EDITABLE | VARCHAR2 | 1 |  |  | CUSTOM_EDITABLE |
| ATTR_ACTION | VARCHAR2 | 30 |  | Yes | UPDATE/DELETE |
| ATTR_VALUE | VARCHAR2 | 4000 |  |  | Optional Attribute. Value exists only for UPDATE attributes |
| ATTRIBUTE_ID | NUMBER |  |  |  | FK to HRC_DL_REM_ATTRIBUTES |
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
| HRC_DL_REM_TMPL_ATTRS_N1 | Non Unique | Default | CUSTOM_EDITABLE |
| HRC_DL_REM_TMPL_ATTRS_N2 | Non Unique | Default | TMPL_ENTITY_ID |
| HRC_DL_REM_TMPL_ATTRS_U1 | Unique | Default | TMPL_ATTRIBUTE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
