# HEX_RUN_DOR_DELIVERY_DTLS

The table stores the delivery details for all the objects for DOR and UCM

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrundordeliverydtls-20597.html#hexrundordeliverydtls-20597](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrundordeliverydtls-20597.html#hexrundordeliverydtls-20597)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUN_DOR_DELIVERY_DTLS_PK | HEX_RUN_DOR_DEL_OPTION_ID, EXT_RUN_ID, EXT_DELIVERY_OPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HEX_RUN_DOR_DEL_OPTION_ID | NUMBER |  | 18 | Yes | The column is a unique sequence generated value |
| FRAGMENT_NO | NUMBER |  |  |  | The column indicates the thread allocated to the fragment |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | The column indicates the document type id |
| DEL_NAME_DE | VARCHAR2 | 4000 |  |  | The column indicates the run time file name generated |
| ISSUED_DATE | DATE |  |  |  | The column indicates the date of issue |
| TIMEZONE | VARCHAR2 | 4000 |  |  | The column indicates the timezone |
| RELATED_OBJECT_ID | NUMBER |  |  |  | The column indicates the related object id |
| VERIFIED_BY | NUMBER |  | 18 |  | The column indicates the DOR verification user |
| VERIFIED_DATE | DATE |  |  |  | The column indicates the DOR verification date |
| EXT_DELIVERY_OPTION_ID | NUMBER |  | 18 | Yes | The column indicates the foreign key reference to the delivery option id from PER_EXT_DELIVERY_OPTIONS_B |
| EXT_RUN_ID | NUMBER |  | 18 | Yes | The column indicates the EXT_RUN_ID from HEX_RUNS table |
| DEL_PREF | VARCHAR2 | 4000 |  |  | The column indicates the delivery preference |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| RELATED_OBJECT_ID_COL | VARCHAR2 | 4000 |  |  | The column indicates the related object id col |
| RELATED_OBJECT_NAME | VARCHAR2 | 4000 |  |  | The column indicates the related object name |
| STATUS | VARCHAR2 | 4000 |  |  | The column indicates the status of DOR |
| SYSTEM_DOCUMENT_TYPE | VARCHAR2 | 4000 |  |  | The column indicates the type of the document |
| ISSUING_AUTHORITY | VARCHAR2 | 4000 |  |  | The column indicates the issuing authority |
| ISSUING_COUNTRY | VARCHAR2 | 4000 |  |  | The column indicates the issuing country |
| ISSUING_LOCATION | VARCHAR2 | 4000 |  |  | The column indicates the issuing location |
| KEY | VARCHAR2 | 4000 |  |  | The column is a unique identifier for each row |
| LOCALE | VARCHAR2 | 4000 |  |  | The column indicates the locale of the delivery option |
| OBJECT_ID | NUMBER |  |  |  | The column indicates the object id to be referred |
| OBJECT_TYPE | VARCHAR2 | 4000 |  |  | The column indicates the type of the object used |
| PERSON_ID | NUMBER |  |  |  | The column indicates the unique identifier for the person |
| DEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | The column indicates the information number |
| PUBLISH | VARCHAR2 | 4000 |  |  | The column indicates the option for publishing the data |
| DEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | The column indicates the information number |
| PUBLISH_DATE | DATE |  |  |  | The column indicates the publishing date |
| DEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | The column indicates the information number |
| DEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | The column indicates the information number |
| DEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | The column indicates the information number |
| DEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | The column indicates the information number |
| DEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | The column indicates the information number |
| COMMENTS | VARCHAR2 | 4000 |  |  | The column indicates the comments to be added for DOR |
| DATE_FROM | DATE |  |  |  | The column indicates the start date of the report |
| DATE_TO | DATE |  |  |  | The column indicates the end date of the report |
| DEI_INFORMATION1 | VARCHAR2 | 4000 |  |  | The column indicates the information text |
| DEI_INFORMATION2 | VARCHAR2 | 4000 |  |  | The column indicates the information text |
| DEI_INFORMATION3 | VARCHAR2 | 4000 |  |  | The column indicates the information text |
| DEI_INFORMATION4 | VARCHAR2 | 4000 |  |  | The column indicates the information text |
| DEI_INFORMATION5 | VARCHAR2 | 4000 |  |  | The column indicates the information text |
| DEI_INFORMATION_CATEGORY | VARCHAR2 | 4000 |  |  | The column indicates the information text |
| DEI_INFORMATION_DATE1 | DATE |  |  |  | The column indicates the information date |
| DEI_INFORMATION_DATE2 | DATE |  |  |  | The column indicates the information date |
| DEI_INFORMATION_DATE3 | DATE |  |  |  | The column indicates the information date |
| DEI_INFORMATION_DATE4 | DATE |  |  |  | The column indicates the information date |
| DEI_INFORMATION_DATE5 | DATE |  |  |  | The column indicates the information date |
| DEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | The column indicates the information number |
| DEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | The column indicates the information number |
| DEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | The column indicates the information number |
| DOCUMENT_NAME | VARCHAR2 | 4000 |  |  | The column indicates the document name |
| DOCUMENT_NUMBER | NUMBER |  |  |  | The column indicates the document number |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| GROUP_TAG_VALUE | VARCHAR2 | 4000 |  |  | The column is a reference for the parent child block link. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_RUN_DOR_DELIVERY_DTLS_N1 | Non Unique | FUSION_TS_TX_DATA | EXT_RUN_ID, EXT_DELIVERY_OPTION_ID, GROUP_TAG_VALUE |
| HEX_RUN_DOR_DELIVERY_DTLS_PK | Unique | FUSION_TS_TX_DATA | HEX_RUN_DOR_DEL_OPTION_ID, EXT_RUN_ID, EXT_DELIVERY_OPTION_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
