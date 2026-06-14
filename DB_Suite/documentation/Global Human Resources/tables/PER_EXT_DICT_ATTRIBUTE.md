# PER_EXT_DICT_ATTRIBUTE

This Table will be used in Extract for Dictionary Attributes.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdictattribute-16325.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdictattribute-16325.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_DICT_ATTRIBUTE_PK | DICTIONARY_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DICTIONARY_ATTR_ID | NUMBER |  | 18 | Yes | DICTIONARY_ATTR_ID |
| DBI_ID | NUMBER |  | 18 |  | DBI_ID |
| DBI_GROUP_ID | NUMBER |  | 18 |  | DBI_GROUP_ID |
| USER_ENTITY_ID | NUMBER |  | 18 | Yes | USER_ENTITY_ID |
| BASE_USER_ENTITY_NAME | VARCHAR2 | 240 |  | Yes | BASE_USER_ENTITY_NAME |
| ATTRIBUTE_NAME | VARCHAR2 | 240 |  | Yes | ATTRIBUTE_NAME |
| MAIN_BLOCK_FLAG | VARCHAR2 | 1 |  |  | MAIN_BLOCK_FLAG |
| SECURED_FLAG | VARCHAR2 | 1 |  |  | SECURED_FLAG |
| HISTORICAL_FLAG | VARCHAR2 | 1 |  |  | HISTORICAL_FLAG |
| INTERNAL_FLAG | VARCHAR2 | 1 |  |  | INTERNAL_FLAG |
| LARGE_OBJECT_FLAG | VARCHAR2 | 1 |  |  | LARGE_OBJECT_FLAG |
| UE_THREADING_ENTITY_FLAG | VARCHAR2 | 1 |  |  | UE_THREADING_ENTITY_FLAG |
| UE_STATUS | VARCHAR2 | 1 |  |  | UE_STATUS |
| UE_MULTI_ROW_FLAG | VARCHAR2 | 1 |  |  | UE_MULTI_ROW_FLAG |
| ARRAY_DBI_FLAG | VARCHAR2 | 1 |  |  | ARRAY_DBI_FLAG |
| DERIVED_UE_NAME | VARCHAR2 | 240 |  |  | DERIVED_UE_NAME |
| BASE_USER_NAME | VARCHAR2 | 255 |  | Yes | BASE_USER_NAME |
| DBI_STATUS | VARCHAR2 | 1 |  |  | DBI_STATUS |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ACTIVE_STATUS | VARCHAR2 | 1 |  |  | ACTIVE_STATUS |
| EXTRA_INFO_TEXT1 | VARCHAR2 | 30 |  |  | EXTRA_INFO_TEXT1 |
| EXTRA_INFO_TEXT2 | VARCHAR2 | 30 |  |  | EXTRA_INFO_TEXT2 |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_DICT_ATTRIBUTE_FK1 | Non Unique | PER_EXT_DICT_ATTRIBUTE_FK1 | USER_ENTITY_ID |
| PER_EXT_DICT_ATTRIBUTE_FK3 | Non Unique | PER_EXT_DICT_ATTRIBUTE_FK3 | UPPER("ATTRIBUTE_NAME") |
| PER_EXT_DICT_ATTRIBUTE_FK4 | Non Unique | PER_EXT_DICT_ATTRIBUTE_FK4 | DBI_ID |
| PER_EXT_DICT_ATTRIBUTE_FK5 | Non Unique | PER_EXT_DICT_ATTRIBUTE_FK5 | DBI_GROUP_ID |
| PER_EXT_DICT_ATTRIBUTE_PK | Unique | PER_EXT_DICT_ATTRIBUTE_PK | DICTIONARY_ATTR_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
