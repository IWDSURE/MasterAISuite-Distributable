# HRC_DL_FILE_HEADERS

This table holds data for Each METADATA line present in the .dat file. Each row will be identified using HEADER_ID

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfileheaders-5846.html#hrcdlfileheaders-5846](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfileheaders-5846.html#hrcdlfileheaders-5846)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_FILE_HEADERS_PK | HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HEADER_ID | NUMBER |  | 18 | Yes | HEADER_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| LINE_ID | NUMBER |  | 18 | Yes | LINE_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| VO_LEVEL | NUMBER |  | 18 |  | VO_LEVEL |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO_MAPPING_ID |
| PARENT_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | PARENT_BUS_OBJ_ID |
| TRANSFER_STATUS | VARCHAR2 | 30 |  | Yes | TRANSFER_STATUS |
| KEY_GUID_NAME | VARCHAR2 | 256 |  |  | KEY_GUID_NAME |
| KEY_SURROGATE_ID_NAME | VARCHAR2 | 256 |  |  | KEY_SURROGATE_ID_NAME |
| KEY_SOURCE_OWNER_NAME | VARCHAR2 | 256 |  |  | KEY_SOURCE_OWNER_NAME |
| KEY_SOURCE_ID_NAME | VARCHAR2 | 256 |  |  | KEY_SOURCE_ID_NAME |
| KEY_PARENT_TABLE_NAME | VARCHAR2 | 30 |  |  | KEY_PARENT_TABLE_NAME |
| KEY_PARENT_GUID_NAME | VARCHAR2 | 256 |  |  | KEY_PARENT_GUID_NAME |
| KEY_PARENT_SURROGATE_ID_NAME | VARCHAR2 | 256 |  |  | KEY_PARENT_SURROGATE_ID_NAME |
| KEY_PARENT_SOURCE_OWNER_NAME | VARCHAR2 | 256 |  |  | KEY_PARENT_SOURCE_OWNER_NAME |
| KEY_PARENT_SOURCE_ID_NAME | VARCHAR2 | 256 |  |  | KEY_PARENT_SOURCE_ID_NAME |
| SOURCE_REF_TABLE_NAME | VARCHAR2 | 200 |  |  | SOURCE_REF_TABLE_NAME |
| SOURCE_REF_NAME001 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME001 |
| SOURCE_REF_NAME002 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME002 |
| SOURCE_REF_NAME003 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME003 |
| SOURCE_REF_NAME004 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME004 |
| SOURCE_REF_NAME005 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME005 |
| SOURCE_REF_NAME006 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME006 |
| SOURCE_REF_NAME007 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME007 |
| SOURCE_REF_NAME008 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME008 |
| SOURCE_REF_NAME009 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME009 |
| SOURCE_REF_NAME010 | VARCHAR2 | 200 |  |  | SOURCE_REF_NAME010 |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PARENT_RESOLUTION_TYPE | VARCHAR2 | 30 |  |  | PARENT_RESOLUTION_TYPE |
| REP_ESD_FLAG | VARCHAR2 | 1 |  |  | Flag will be "Y" if current Effective Start Date can be Logical Start Date. |
| REP_EED_FLAG | VARCHAR2 | 1 |  |  | Flag will be "Y" if current Effective End Date can be Logical End Date. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_FILE_HEADERS_N1 | Non Unique | Default | DATA_SET_BUS_OBJ_ID |
| HRC_DL_FILE_HEADERS_N2 | Non Unique | Default | BUSINESS_OBJECT_ID, PARENT_BUSINESS_OBJECT_ID |
| HRC_DL_FILE_HEADERS_U1 | Unique | Default | HEADER_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
