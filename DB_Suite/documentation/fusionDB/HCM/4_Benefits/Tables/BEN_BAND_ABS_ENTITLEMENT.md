# BEN_BAND_ABS_ENTITLEMENT

BEN_BAND_ABS_ENTITLEMENT identifies band entitlements information.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbandabsentitlement-24625.html#benbandabsentitlement-24625](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbandabsentitlement-24625.html#benbandabsentitlement-24625)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BAND_ABS_ENTITLEMENT_PK | BAND_ENTITLEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAND_ENTITLEMENT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BAND_ENTITLEMENT_NAME | VARCHAR2 | 30 |  | Yes | Identifies band entitlement name. |
| BAND_ENTITLEMENT_UOM | VARCHAR2 | 10 |  | Yes | Identifies band entitlement unit of measure. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BAND_ABS_ENTITLEMENT_PK | Unique | FUSION_TS_TX_DATA | BAND_ENTITLEMENT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
