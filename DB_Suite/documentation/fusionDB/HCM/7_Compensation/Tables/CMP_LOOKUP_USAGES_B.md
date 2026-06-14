# CMP_LOOKUP_USAGES_B

Stores lookup information based on a plan and type. This table allows users to define lookup values at plan level.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmplookupusagesb-20216.html#cmplookupusagesb-20216](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmplookupusagesb-20216.html#cmplookupusagesb-20216)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_LOOKUP_USAGES_B_PK | LOOKUP_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOOKUP_USAGE_ID | NUMBER |  | 18 | Yes | LOOKUP_USAGE_ID |
| TEXT_VALUE4 | VARCHAR2 | 250 |  |  | TEXT_VALUE4 |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| KEY_TYPE | VARCHAR2 | 30 |  | Yes | KEY_TYPE |
| KEY_VALUE | NUMBER |  | 18 | Yes | KEY_VALUE |
| ATTRIBUTE_NAME | VARCHAR2 | 30 |  | Yes | ATTRIBUTE_NAME |
| ATTRIBUTE_VALUE | VARCHAR2 | 30 |  |  | ATTRIBUTE_VALUE |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | ENABLED_FLAG |
| ORDER_NUM | NUMBER |  |  |  | ORDER_NUM |
| NUMBER_VALUE1 | NUMBER |  |  |  | NUMBER_VALUE1 |
| NUMBER_VALUE2 | NUMBER |  |  |  | NUMBER_VALUE2 |
| NUMBER_VALUE3 | NUMBER |  |  |  | NUMBER_VALUE3 |
| TEXT_VALUE1 | VARCHAR2 | 30 |  |  | TEXT_VALUE1 |
| TEXT_VALUE2 | VARCHAR2 | 2000 |  |  | Stores Report Path |
| TEXT_VALUE3 | VARCHAR2 | 250 |  |  | Stores Report name |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| NUMBER_VALUE4 | NUMBER |  |  |  | NUMBER_VALUE4 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_LOOKUP_USAGES_B_U1 | Unique | Default | KEY_TYPE, KEY_VALUE, ATTRIBUTE_NAME, ATTRIBUTE_VALUE |
| CMP_LOOKUP_USAGES_B_UK1 | Unique | Default | LOOKUP_USAGE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
