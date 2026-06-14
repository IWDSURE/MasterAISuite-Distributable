# CMP_LOOKUP_USAGES_TL

Stores translation attributes for lookup

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmplookupusagestl-22171.html#cmplookupusagestl-22171](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmplookupusagestl-22171.html#cmplookupusagestl-22171)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_LOOKUP_USAGES_TL_PK | LOOKUP_USAGE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOOKUP_USAGE_ID | NUMBER |  | 18 | Yes | LOOKUP_USAGE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| DISPLAY_NAME | VARCHAR2 | 80 |  |  | DISPLAY_NAME |
| DESCRIPTION | VARCHAR2 | 300 |  |  | DESCRIPTION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_LOOKUP_USAGES_TL_UK1 | Unique | Default | LOOKUP_USAGE_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
