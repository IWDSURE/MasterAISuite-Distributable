# HRC_SDL_INTERFACE_HEADER

Hcm Data Loader Interface Header

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlinterfaceheader-15696.html#hrcsdlinterfaceheader-15696](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsdlinterfaceheader-15696.html#hrcsdlinterfaceheader-15696)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SDL_INTERFACE_HEADER_PK | INTERFACE_HEADER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERFACE_HEADER_ID | NUMBER |  | 18 | Yes | INTERFACE_HEADER_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | SOURCE_TYPE |
| LAYOUT_ID | NUMBER |  | 18 | Yes | LAYOUT_ID |
| DATA_SET_ID | NUMBER |  | 18 |  | DATA_SET_ID |
| DATA_SET_NAME | VARCHAR2 | 200 |  | Yes | DATA_SET_NAME |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| UPLOAD_ID | NUMBER |  | 18 |  | UPLOAD_ID |
| EXECUTION_STATUS | VARCHAR2 | 30 |  |  | EXECUTION_STATUS |
| MSG_TEXT | VARCHAR2 | 500 |  |  | MSG_TEXT |
| HASH_VALUE | VARCHAR2 | 100 |  | Yes | HASH_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ERROR_INFO | VARCHAR2 | 4000 |  |  | Information to translate Error text in user language. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| RUN_MODE | VARCHAR2 | 1000 |  |  | RUN_MODE |
| HEADER_INFO1 | VARCHAR2 | 1000 |  |  | HEADER_INFO1 |
| HEADER_INFO2 | VARCHAR2 | 1000 |  |  | HEADER_INFO2 |
| HEADER_INFO3 | VARCHAR2 | 1000 |  |  | HEADER_INFO3 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SDL_INTERFACE_HEADER_N1 | Non Unique | Default | SOURCE_TYPE, LAYOUT_ID, DATA_SET_NAME |
| HRC_SDL_INTERFACE_HEADER_U1 | Unique | Default | INTERFACE_HEADER_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
