# BEN_EXTRA_INPUT_VALUES

BEN_EXTRA_INPUT_VALUES indentifies which extra input values are used by a standard rate.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextrainputvalues-31730.html#benextrainputvalues-31730](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benextrainputvalues-31730.html#benextrainputvalues-31730)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_EXTRA_INPUT_VALUES_PK | EXTRA_INPUT_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTRA_INPUT_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ACTY_BASE_RT_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ACTY_BASE_RT_F. |
| INPUT_VALUE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_INPUT_VALUES_F. |
| INPUT_TEXT | VARCHAR2 | 240 |  |  | Input value text in rates setup. |
| UPD_WHEN_ELE_ENDED_CD | VARCHAR2 | 30 |  |  | Update when element entry ended. |
| RETURN_VAR_NAME | VARCHAR2 | 240 |  | Yes | Return variable name in rates setup. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| VALUE_DEFINITION_BASE_NAME | VARCHAR2 | 128 |  |  | Base name of the Value Definition |
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
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_EXTRA_INPUT_VALUES_FK1 | Non Unique | Default | ACTY_BASE_RT_ID |
| BEN_EXTRA_INPUT_VALUES_FK2 | Non Unique | Default | INPUT_VALUE_ID |
| BEN_EXTRA_INPUT_VALUES_PK | Unique | Default | EXTRA_INPUT_VALUE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
