# BEN_INTEGRATION_KEY_MAP

BEN_INTEGRATION_KEY_MAP stores 
the alternate Key Map definitions for benefits objects.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_IDX

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benintegrationkeymap-29333.html#benintegrationkeymap-29333](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benintegrationkeymap-29333.html#benintegrationkeymap-29333)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_INTEGRATION_KEY_MAP_F_PK | OBJECT_NAME, BASE_NAME, SURROGATE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_NAME | VARCHAR2 | 256 |  | Yes | Type of the object |
| BASE_NAME | VARCHAR2 | 256 |  | Yes | Name of the object |
| SURROGATE_ID | NUMBER |  | 18 | Yes | surrogate key of the object |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | This column will store the Enterprise ID. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_INTEGRATION_KEY_MAP_N1 | Non Unique | FUSION_TS_TX_IDX | BASE_NAME |
| BEN_INTEGRATION_KEY_MAP_N2 | Non Unique | FUSION_TS_TX_IDX | SURROGATE_ID |
| BEN_INTEGRATION_KEY_MAP_PK | Unique | FUSION_TS_TX_IDX | OBJECT_NAME, BASE_NAME, SURROGATE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
