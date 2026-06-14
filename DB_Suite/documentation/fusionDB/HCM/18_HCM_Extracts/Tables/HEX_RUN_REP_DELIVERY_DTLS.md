# HEX_RUN_REP_DELIVERY_DTLS

The table stores the delivery details for all the objects

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunrepdeliverydtls-5537.html#hexrunrepdeliverydtls-5537](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexrunrepdeliverydtls-5537.html#hexrunrepdeliverydtls-5537)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_RUN_REP_DELIVERY_DTLS_PK | HEX_RUN_DEL_OPTION_ID, EXT_RUN_ID, EXT_DELIVERY_OPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HEX_RUN_DEL_OPTION_ID | NUMBER |  | 18 | Yes | The column is a unique sequence generated value |
| FRAGMENT_NO | NUMBER |  |  |  | The column indicates the thread allocated to the fragment |
| DEL_NAME_DE | VARCHAR2 | 4000 |  |  | The column indicates the run time file name generated |
| TIMEZONE | VARCHAR2 | 4000 |  |  | The column indicates the timezone |
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
| KEY | VARCHAR2 | 4000 |  |  | The column is a unique identifier for each row |
| LOCALE | VARCHAR2 | 4000 |  |  | The column indicates the locale of the delivery option |
| OBJECT_ID | NUMBER |  |  |  | The column indicates the object id to be referred |
| OBJECT_TYPE | VARCHAR2 | 4000 |  |  | The column indicates the type of the object used |
| ENTERPRISE_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OUTPUT_NAME | VARCHAR2 | 4000 |  |  | The column indicates the name of the output file generated |
| SAVE_OUTPUT | VARCHAR2 | 4 |  |  | The column indicates if the output generated needs to be saved automatically |
| PARAMETER1 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER2 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER3 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER4 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER5 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER6 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER7 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER8 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER9 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| PARAMETER10 | VARCHAR2 | 4000 |  |  | The column stores the values defined for the delivery option |
| GROUP_TAG_VALUE | VARCHAR2 | 4000 |  |  | The column is a reference for the parent child block link. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_RUN_REP_DELIVERY_DTLS_N1 | Non Unique | FUSION_TS_TX_DATA | EXT_RUN_ID, EXT_DELIVERY_OPTION_ID, GROUP_TAG_VALUE |
| HEX_RUN_REP_DELIVERY_DTLS_PK | Unique | FUSION_TS_TX_DATA | HEX_RUN_DEL_OPTION_ID, EXT_RUN_ID, EXT_DELIVERY_OPTION_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
