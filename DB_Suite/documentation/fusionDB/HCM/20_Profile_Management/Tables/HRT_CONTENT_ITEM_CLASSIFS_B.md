# HRT_CONTENT_ITEM_CLASSIFS_B

This table defines the relations between content items and classifications.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemclassifsb-18296.html#hrtcontentitemclassifsb-18296](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemclassifsb-18296.html#hrtcontentitemclassifsb-18296)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_ITEM_CLASSIFS_B_PK | CONTENT_ITEM_CLASSIFICATION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_ITEM_CLASSIFICATION_ID | NUMBER |  | 18 | Yes | Unique Identifier for Content items classifications |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_TYPE_B table |
| CLASSIFICATION_TYPE | VARCHAR2 | 240 |  |  | Stores the type of the classification relation. This helps to decide whether it's a Business Capability, Business Driver, or Domain type of descriptor, or a skill source id. |
| CLASSIFICATION_CODE | VARCHAR2 | 240 |  |  | Store the lookup code of the classification selected or the skill source id |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_ITEM_CLASSIF_B_PK | Unique | HRT_CONTENT_ITEM_CLASSIF_B_PK | CONTENT_ITEM_CLASSIFICATION_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
