# HRC_SDL_ATTR_MAPS

Child table of HRC_SDL_MAPS. Contains detailed information on attributes of  a business object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlattrmaps-15268.html#hrcsdlattrmaps-15268](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlattrmaps-15268.html#hrcsdlattrmaps-15268)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_ATTR_MAPS_PK | ATTR_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTR_MAP_ID | NUMBER |  | 18 | Yes | ATTR_MAP_ID |
| BO_MAP_ID | NUMBER |  | 18 | Yes | BO_MAP_ID |
| SEQUENCE_NUMBER | NUMBER |  | 5 | Yes | SEQUENCE_NUMBER |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | ATTRIBUTE_NAME |
| ATTRIBUTE_LABEL | VARCHAR2 | 240 |  | Yes | ATTRIBUTE_LABEL |
| ATTRIBUTE_TYPE | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_TYPE |
| ATTRIBUTE_SUBTYPE | VARCHAR2 | 30 |  |  | ATTRIBUTE_SUBTYPE |
| ATTRIBUTE_SUB_CATEGORY | VARCHAR2 | 30 |  |  | ATTRIBUTE_SUB_CATEGORY |
| ATTRIBUTE_DATATYPE | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_DATATYPE |
| MANDATORY_FLAG | VARCHAR2 | 4 |  | Yes | MANDATORY_FLAG |
| USER_KEY_FLAG | VARCHAR2 | 4 |  | Yes | USER_KEY_FLAG |
| PARENT_USER_KEY_FLAG | VARCHAR2 | 4 |  | Yes | PARENT_USER_KEY_FLAG |
| PARENT_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | PARENT_BUSINESS_OBJECT_ID |
| PARENT_ATTRIBUTE_NAME | VARCHAR2 | 100 |  |  | PARENT_ATTRIBUTE_NAME |
| FLEXFIELD_CODE | VARCHAR2 | 40 |  |  | FLEXFIELD_CODE |
| FLEXFIELD_CONTEXT_CODE | VARCHAR2 | 80 |  |  | FLEXFIELD_CONTEXT_CODE |
| USER_KEY_ATTR_NAMES | VARCHAR2 | 4000 |  |  | USER_KEY_ATTR_NAMES |
| LIST_TYPE | VARCHAR2 | 100 |  |  | LIST_TYPE |
| DISPLAY_TYPE | VARCHAR2 | 240 |  |  | DISPLAY_TYPE |
| LIST_VIEW_DEF_NAME | VARCHAR2 | 240 |  |  | LIST_VIEW_DEF_NAME |
| DISPLAY_ATTR_LIST | VARCHAR2 | 240 |  |  | DISPLAY_ATTR_LIST |
| RETURN_ATTR_NAME | VARCHAR2 | 1000 |  |  | RETURN_ATTR_NAME |
| LIST_VIEW_CRIT_LIST | VARCHAR2 | 4000 |  |  | LIST_VIEW_CRIT_LIST |
| LIST_BIND_MAP | VARCHAR2 | 4000 |  |  | LIST_BIND_MAP |
| LIST_QUERY_CRITERIA | VARCHAR2 | 240 |  |  | LIST_QUERY_CRITERIA |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SECURE_FLAG | VARCHAR2 | 4 |  |  | SECURE_FLAG |
| DATA_LENGTH | NUMBER |  | 4 |  | DATA_LENGTH |
| REFERENCED_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | REFERENCED_BUSINESS_OBJECT_ID |
| INTKEY_HINT_ALLOWED_FLAG | VARCHAR2 | 4 |  |  | INTKEY_HINT_ALLOWED_FLAG |
| DEPENDENT_ATTR_NAMES | VARCHAR2 | 1000 |  |  | DEPENDENT_ATTR_NAMES |
| ATTR_DETAILS | VARCHAR2 | 1000 |  |  | ATTR_DETAILS |
| ATTRIB_INFO1 | VARCHAR2 | 1000 |  |  | ATTRIB_INFO1 |
| ATTRIB_INFO2 | VARCHAR2 | 1000 |  |  | ATTRIB_INFO2 |
| ATTRIB_INFO3 | VARCHAR2 | 1000 |  |  | ATTRIB_INFO3 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_ATTR_MAPS_N1 | Non Unique | Default | BUSINESS_OBJECT_ID, SEQUENCE_NUMBER |
| HRC_SDL_ATTR_MAPS_N2 | Non Unique | Default | BUSINESS_OBJECT_ID, ATTRIBUTE_NAME |
| HRC_SDL_ATTR_MAPS_U1 | Unique | Default | ATTR_MAP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
