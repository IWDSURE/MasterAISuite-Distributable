# CMP_CUSTOM_REGION_LAYOUTS

Table to store layout customisations for user interface regions

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcustomregionlayouts-27437.html#cmpcustomregionlayouts-27437](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcustomregionlayouts-27437.html#cmpcustomregionlayouts-27437)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CUSTOM_REGION_LAYOUTS_PK | CUSTOM_TYPE, CUSTOM_KEY, REGION_NAME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CUSTOM_TYPE | VARCHAR2 | 30 |  | Yes | Customisation type for user interface region |
| CUSTOM_KEY | NUMBER |  | 18 | Yes | Customisation key |
| REGION_NAME | VARCHAR2 | 60 |  | Yes | Name to identify user interface region |
| REGION_LAYOUT | CLOB |  |  |  | Layout of user interface region |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CUSTOM_REGION_LAYOUTS_PK | Unique | Default | CUSTOM_TYPE, CUSTOM_KEY, REGION_NAME |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
