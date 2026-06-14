# PER_PORTRAIT_CONTENT_TL

This table stores the Translated Portrait Content  data.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitcontenttl-22405.html#perportraitcontenttl-22405](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitcontenttl-22405.html#perportraitcontenttl-22405)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PORTRAIT_CONTENT_TL_PK | LANGUAGE, PORTRAIT_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PORTRAIT_CONTENT_ID | NUMBER |  | 18 | Yes | System generated primary key |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| PORTRAIT_CONTENT_ITEM_NAME | VARCHAR2 | 240 |  |  | Display name for the Portrait content item |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Additional information about the Portrait Content Item |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PORTRAIT_CONTENT_TL_PK | Unique | Default | LANGUAGE, PORTRAIT_CONTENT_ID, ORA_SEED_SET1 |
| PER_PORTRAIT_CONTENT_TL_PK1 | Unique | Default | LANGUAGE, PORTRAIT_CONTENT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
