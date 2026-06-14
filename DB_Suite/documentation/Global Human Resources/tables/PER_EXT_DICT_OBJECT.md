# PER_EXT_DICT_OBJECT

This Table will be used in Extract for Dictionary Objects.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdictobject-10201.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perextdictobject-10201.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXT_DICT_OBJECT_PK | DICTIONARY_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DICTIONARY_OBJ_ID | NUMBER |  | 18 | Yes | DICTIONARY_OBJ_ID |
| EXT_BUS_OBJECT_ID | NUMBER |  | 18 |  | EXT_BUS_OBJECT_ID |
| USER_ENTITY_ID | NUMBER |  | 18 | Yes | USER_ENTITY_ID |
| BASE_USER_ENTITY_NAME | VARCHAR2 | 240 |  | Yes | BASE_USER_ENTITY_NAME |
| USER_ENTITY_NAME | VARCHAR2 | 240 |  |  | USER_ENTITY_NAME |
| OBJECT_NAME | VARCHAR2 | 4000 |  | Yes | OBJECT_NAME |
| MAIN_BLOCK_FLAG | VARCHAR2 | 1 |  |  | MAIN_BLOCK_FLAG |
| SECURED_FLAG | VARCHAR2 | 1 |  |  | SECURED_FLAG |
| HISTORICAL_FLAG | VARCHAR2 | 1 |  |  | HISTORICAL_FLAG |
| INTERNAL_FLAG | VARCHAR2 | 1 |  |  | INTERNAL_FLAG |
| LARGE_OBJECT_FLAG | VARCHAR2 | 1 |  |  | LARGE_OBJECT_FLAG |
| THREADING_ENTITY_FLAG | VARCHAR2 | 1 |  |  | THREADING_ENTITY_FLAG |
| UE_STATUS | VARCHAR2 | 1 |  |  | UE_STATUS |
| SCORE | NUMBER |  | 9 |  | SCORE |
| ARRAY_DBI_FLAG | VARCHAR2 | 1 |  |  | ARRAY_DBI_FLAG |
| UE_MULTI_ROW_FLAG | VARCHAR2 | 1 |  |  | UE_MULTI_ROW_FLAG |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ACTIVE_STATUS | VARCHAR2 | 1 |  |  | ACTIVE_STATUS |
| EXTRA_INFO_TEXT1 | VARCHAR2 | 30 |  |  | EXTRA_INFO_TEXT1 |
| EXTRA_INFO_TEXT2 | VARCHAR2 | 30 |  |  | EXTRA_INFO_TEXT2 |
| EXTRA_INFO_TEXT3 | VARCHAR2 | 30 |  |  | EXTRA_INFO_TEXT3 |
| EXTRA_INFO_NUMBER1 | NUMBER |  | 18 |  | EXTRA_INFO_NUMBER1 |
| EXTRA_INFO_NUMBER2 | NUMBER |  | 18 |  | EXTRA_INFO_NUMBER2 |
| EXTRA_INFO_DATE1 | DATE |  |  |  | EXTRA_INFO_DATE1 |
| EXTRA_INFO_DATE2 | DATE |  |  |  | EXTRA_INFO_DATE2 |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXT_DICT_OBJECT_FK1 | Non Unique | PER_EXT_DICT_OBJECT_FK1 | USER_ENTITY_ID |
| PER_EXT_DICT_OBJECT_FK3 | Non Unique | PER_EXT_DICT_OBJECT_FK3 | UPPER("OBJECT_NAME") |
| PER_EXT_DICT_OBJECT_FK4 | Non Unique | PER_EXT_DICT_OBJECT_FK4 | EXT_BUS_OBJECT_ID |
| PER_EXT_DICT_OBJECT_PK | Unique | PER_EXT_DICT_OBJECT_PK | DICTIONARY_OBJ_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
