# HRT_CONTENT_TYPE_RLATS

Content Type Relationship table holds the relationships between Content Types (e.g. Competency Content Type is a Parent of Sub_Competency Content Type).

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontenttyperlats-8244.html#hrtcontenttyperlats-8244](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontenttyperlats-8244.html#hrtcontenttyperlats-8244)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_TYPE_RLATS_PK | CONTENT_TYPE_RLAT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_TYPE_RLAT_ID | NUMBER |  | 18 | Yes | Unique identifier of Content Type relationship |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to Content Type |
| RELATED_CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Related Content Type Id |
| RELATIONSHIP_CODE | VARCHAR2 | 30 |  | Yes | Defines the relationship between Content Types |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RATING_INTERACTION_TYPE | VARCHAR2 | 30 |  |  | Defines how the rating should be identified between content types |
| DATE_FROM | DATE |  |  | Yes | Start date of the content type relationship |
| DATE_TO | DATE |  |  |  | End date of the content type relationship |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_TYPE_RLATS_N20 | Non Unique | Default | SGUID |
| HRT_CONTENT_TYPE_RLATS_PK | Unique | Default | CONTENT_TYPE_RLAT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_CONTENT_TYPE_RLATS_PK1 | Unique | Default | CONTENT_TYPE_RLAT_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
