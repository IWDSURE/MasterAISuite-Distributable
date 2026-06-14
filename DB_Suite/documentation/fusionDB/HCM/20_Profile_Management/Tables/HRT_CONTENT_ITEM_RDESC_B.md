# HRT_CONTENT_ITEM_RDESC_B

This table defines the rating descriptions that are used in Content Item.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemrdescb-12829.html#hrtcontentitemrdescb-12829](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemrdescb-12829.html#hrtcontentitemrdescb-12829)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_ITEM_RDESC_B_PK | CONTENT_RATING_DESC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CONTENT_RATING_DESC_ID | NUMBER |  | 18 | Yes | Unique identifier of Content Item Rating Description | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to Content Type table | Active |
| CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Foreign key to Content Item table | Active |
| RATING_LEVEL_ID | NUMBER |  | 18 | Yes | Foreign key to Rating Level table | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_ITEM_RDESC_B_N1 | Non Unique | Default | RATING_LEVEL_ID |
| HRT_CONTENT_ITEM_RDESC_B_PK | Unique | Default | CONTENT_RATING_DESC_ID |
| HRT_CONTENT_ITEM_RDESC_N2 | Non Unique | Default | CONTENT_ITEM_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
