# BEN_TYPE_VALUES

This table will hold the Benefits Lookup types details.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bentypevalues-3069.html#bentypevalues-3069](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bentypevalues-3069.html#bentypevalues-3069)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_TYPE_VALUES_PK | TYPE_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TYPE_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| TYPE_ID | NUMBER |  | 18 | Yes | This column is Foreign Key to BEN_TYPES. |
| START_DATE | DATE |  |  |  | This column will store the active from start date. |
| END_DATE | DATE |  |  |  | This column will store the active till end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | This column will store the Enterprise ID. |
| TYPE_NUM | NUMBER |  |  |  | This column will store the Numeric Type Value. |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | Indicates if the type values is active. |
| TYPE_CD | VARCHAR2 | 30 |  |  | This column will store the alphanumeric type value. |
| TYPE_RL | NUMBER |  | 18 |  | Formula ID for the Type Value. |
| MEANING | VARCHAR2 | 240 |  |  | Description of the Type Value to be used in Pre-Determined List of Values. |
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
| BEN_TYPE_VALUES_N1 | Non Unique | Default | TYPE_ID, TYPE_NUM |
| BEN_TYPE_VALUES_PK | Unique | Default | TYPE_VALUE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
