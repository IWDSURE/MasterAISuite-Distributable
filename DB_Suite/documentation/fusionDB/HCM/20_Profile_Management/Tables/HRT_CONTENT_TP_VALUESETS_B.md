# HRT_CONTENT_TP_VALUESETS_B

This table defines the content item value sets for different content item value set templates.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontenttpvaluesetsb-25100.html#hrtcontenttpvaluesetsb-25100](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontenttpvaluesetsb-25100.html#hrtcontenttpvaluesetsb-25100)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_TP_VALUESETS_B_PK | CONTENT_VALUE_SET_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_VALUE_SET_ID | NUMBER |  | 18 | Yes | Unique identifier for Content Type Value sets |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | This column stores foreign key to content type |
| CURATION_ENABLED_FLAG | VARCHAR2 | 1 |  |  | Whether the catalog is enabled for curation |
| STATUS | VARCHAR2 | 1 |  |  | This column is used for holding the catalog status |
| PARENT_CONTENT_VALUE_SET_ID | NUMBER |  | 18 |  | Foreign key to CONTENT_VALUES_SET_ID, used mainly as a container valueset for content sections supporting multiple valuesets. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CONTENT_VALUE_SET_CODE | VARCHAR2 | 30 |  |  | Unique code which identifies the Content Type Value set |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_TP_VALUESETS_B_PK | Unique | Default | CONTENT_VALUE_SET_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_CONTENT_TP_VALUESETS_B_PK1 | Unique | Default | CONTENT_VALUE_SET_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
