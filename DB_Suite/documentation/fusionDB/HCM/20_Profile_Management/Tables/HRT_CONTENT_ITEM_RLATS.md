# HRT_CONTENT_ITEM_RLATS

This table holds the relationships between Content Items (e.g. A Product Content Item (Parent) could have multiple Product Codes (Child)).

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemrlats-14136.html#hrtcontentitemrlats-14136](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemrlats-14136.html#hrtcontentitemrlats-14136)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_ITEM_RLATS_PK | CONTENT_ITEM_RLAT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CONTENT_ITEM_RLAT_ID | NUMBER |  | 18 | Yes | Unique identifier of Content Item Relationship | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to Content Type Id | Active |
| CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Foreign key to Content Item Id | Active |
| RELATED_CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Related Content Type Id | Active |
| RELATED_CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Related Content Item Id | Active |
| DATE_FROM | DATE |  |  | Yes | Start date of Content Item relationship | Active |
| DATE_TO | DATE |  |  |  | End date of Content Item relationship | Active |
| RELATIONSHIP_CODE | VARCHAR2 | 30 |  | Yes | Relationship Code | Active |
| MANDATORY_FLAG | VARCHAR2 | 30 |  |  | Defines if the Content Item in the relationship is required | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_ITEM_RLATS_N1 | Non Unique | Default | CONTENT_ITEM_ID, BUSINESS_GROUP_ID |
| HRT_CONTENT_ITEM_RLATS_PK | Unique | Default | CONTENT_ITEM_RLAT_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
