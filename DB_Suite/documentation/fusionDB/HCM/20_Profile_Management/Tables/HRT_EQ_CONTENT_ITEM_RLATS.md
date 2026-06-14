# HRT_EQ_CONTENT_ITEM_RLATS

This table defines relation between content item and the variant

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrteqcontentitemrlats-4823.html#hrteqcontentitemrlats-4823](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrteqcontentitemrlats-4823.html#hrteqcontentitemrlats-4823)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_EQ_CONTENT_ITEM_RLATS_PK | EQ_CONTENT_ITEM_RLATS_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EQ_CONTENT_ITEM_RLATS_ID | NUMBER |  | 18 | Yes | Unique key identifier for the relationship between contentitem and variant |
| SGUID | VARCHAR2 | 32 |  |  | SGUID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| GLOBAL_ID | VARCHAR2 | 30 |  |  | Unique Identifier for content item |
| RELATED_GLOBAL_ID | VARCHAR2 | 30 |  |  | Unique Identifier for EQ content items |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_TYPE_B table |
| RELATED_CONTENT_TYPE_ID | NUMBER |  | 18 |  | Hold the content type the record is linked to |
| RELATED_CONTENT_ITEM_ID | NUMBER |  | 18 |  | Hold the contentitemid the record is linked to |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign key to HRT_CONTENT_ITEMS_B table |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_EQ_CONTENT_ITEM_RLATS_N1 | Non Unique | Default | CONTENT_ITEM_ID |
| HRT_EQ_CONTENT_ITEM_RLATS_N2 | Non Unique | Default | RELATED_CONTENT_ITEM_ID |
| HRT_EQ_CONTENT_ITEM_RLATS_N3 | Non Unique | Default | GLOBAL_ID, RELATED_GLOBAL_ID |
| HRT_EQ_CONTENT_ITEM_RLATS_PK | Unique | Default | EQ_CONTENT_ITEM_RLATS_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_EQ_CONTENT_ITEM_RLATS_PK1 | Unique | Default | EQ_CONTENT_ITEM_RLATS_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
