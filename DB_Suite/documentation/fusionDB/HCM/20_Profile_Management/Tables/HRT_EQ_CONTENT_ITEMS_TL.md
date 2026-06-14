# HRT_EQ_CONTENT_ITEMS_TL

This table defines the variants translation for different content items

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrteqcontentitemstl-16276.html#hrteqcontentitemstl-16276](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrteqcontentitemstl-16276.html#hrteqcontentitemstl-16276)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_EQ_CONTENT_ITEMS_TL_PK | EQ_CONTENT_ITEM_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EQ_CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Unique key identifier for variants |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  |  | Indicates the name of the variant |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_EQ_CONTENT_ITEMS_TL_N1 | Non Unique | Default | LANGUAGE, NAME |
| HRT_EQ_CONTENT_ITEMS_TL_N2 | Non Unique | Default | LANGUAGE, UPPER("NAME") |
| HRT_EQ_CONTENT_ITEMS_TL_PK | Unique | Default | EQ_CONTENT_ITEM_ID, BUSINESS_GROUP_ID, LANGUAGE, ORA_SEED_SET1 |
| HRT_EQ_CONTENT_ITEMS_TL_PK1 | Unique | Default | EQ_CONTENT_ITEM_ID, BUSINESS_GROUP_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
