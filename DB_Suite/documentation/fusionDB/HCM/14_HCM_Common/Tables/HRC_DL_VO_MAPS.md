# HRC_DL_VO_MAPS

HRC_DL_VO_MAPS is used to record the View Objects mapped at import time so that they may be referenced at load time to ensure the appropriate VO data is located from the Data Loader stage table columns.
When data is imported for a business object, Metadata manager analyses the ADF View Object to determine the names and types of Data Loader eligible attributes used in the View Object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvomaps-15218.html#hrcdlvomaps-15218](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvomaps-15218.html#hrcdlvomaps-15218)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_VO_MAPS_PK | VO_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO_MAPPING_ID |
| FLEX_AVAILABLE | VARCHAR2 | 3 |  |  | FLEX_AVAILABLE |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| VO_MAPPING_HASH | VARCHAR2 | 100 |  | Yes | VO_MAPPING_HASH |
| IS_TRANSIENT_FLAG | VARCHAR2 | 1 |  | Yes | Provides information about a VO's transient nature. The default value is set to 'N', indicating NO |
| IS_MULTIPLE_UK | VARCHAR2 | 1 |  | Yes | Indicates if the LOCAL Surrogate Key (and if a child object the PARENT Surrogate Key), has multiple User Key Lists mapped within this VO Map. The default value is set to 'N', indicating NO |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| BUS_OBJ_DATE_TYPE | VARCHAR2 | 50 |  | Yes | BUS_OBJ_DATE_TYPE |
| UK_DEO_OVERRIDE | VARCHAR2 | 1 |  |  | UK_DEO_OVERRIDE |
| TRANSLATION_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | Stores the Translation Business Object ID value |
| TRANSLATION_FLAG | VARCHAR2 | 1 |  |  | Value will be "Y" for Translation Entities else will be "N".  For Existing rows value will be NULL |
| LESD_CHANGE_RESTRICTED | VARCHAR2 | 1 |  |  | For a Date Effective object, Y indicates that change to the Least Effective Start Date is restricted. |
| LEED_CHANGE_RESTRICTED | VARCHAR2 | 1 |  |  | For a Date Effective object, Y indicates that change to the Last Effective End Date is restricted. |
| ORA_SEARCH_ENABLED | VARCHAR2 | 1 |  |  | If OS custom property exists on TopLevel VO then Y else blank |
| RESTRICT_FLEX_FIELD_CONTEXTS | VARCHAR2 | 1 |  |  | If flex field contexts are restricted on TopLevel VO then Y else blank |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_VO_MAPS_PK | Unique | Default | VO_MAPPING_ID |
| HRC_DL_VO_MAPS_U1 | Unique | Default | VO_MAPPING_HASH, ENTERPRISE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
