# HRC_DL_OS_BULK_IMPORT

This table is a backup table for storing Oracle Search Backup records.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlosbulkimport-24657.html#hrcdlosbulkimport-24657](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlosbulkimport-24657.html#hrcdlosbulkimport-24657)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_OS_BULK_IMPORT_PK | BULK_IMPORT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BULK_IMPORT_ID | NUMBER |  | 18 | Yes | BULK_IMPORT_ID |
| TABLE_NAME | VARCHAR2 | 240 |  | Yes | TABLE_NAME |
| KEY_ATTR1 | VARCHAR2 | 240 |  | Yes | KEY_ATTR1 |
| KEY_VALUE1 | VARCHAR2 | 240 |  |  | KEY_VALUE1 |
| KEY_ATTR2 | VARCHAR2 | 240 |  |  | KEY_ATTR2 |
| KEY_VALUE2 | VARCHAR2 | 240 |  |  | KEY_VALUE2 |
| KEY_ATTR3 | VARCHAR2 | 240 |  |  | KEY_ATTR3 |
| KEY_VALUE3 | VARCHAR2 | 240 |  |  | KEY_VALUE3 |
| KEY_ATTR4 | VARCHAR2 | 240 |  |  | KEY_ATTR4 |
| KEY_VALUE4 | VARCHAR2 | 240 |  |  | KEY_VALUE4 |
| KEY_ATTR5 | VARCHAR2 | 240 |  |  | KEY_ATTR5 |
| KEY_VALUE5 | VARCHAR2 | 240 |  |  | KEY_VALUE5 |
| OPERATION | VARCHAR2 | 20 |  | Yes | OPERATION |
| SOURCE_LANGUAGE | VARCHAR2 | 10 |  |  | SOURCE_LANGUAGE |
| INDEXES | VARCHAR2 | 4000 |  | Yes | INDEXES |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | PROGRAM_NAME |
| PROGRAM_NAME_FILTERS | CLOB |  |  |  | PROGRAM_NAME_FILTERS |
| STATUS | VARCHAR2 | 20 |  |  | STATUS |
| CUSTOM_STATE | CLOB |  |  |  | CUSTOM_STATE |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| IS_TRANSFERRED | VARCHAR2 | 1 |  |  | IS_TRANSFERRED |
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
| hrc_dl_os_bulk_import_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID, IS_TRANSFERRED |
| hrc_dl_os_bulk_import_U1 | Unique | Default | BULK_IMPORT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
