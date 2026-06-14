# HWP_ATTRIBUTES_TL

Translation table for Attributes/Indicators

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpattributestl-17377.html#hwpattributestl-17377](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpattributestl-17377.html#hwpattributestl-17377)

## Primary Key

| Name | Columns |
|------|----------|
| HWP_ATTRIBUTES_TL_PK | ATTRIBUTE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Attribute ID. |
| ATTR_NAME | VARCHAR2 | 400 |  | Yes | Attribute Name. |
| ATTR_DESCRIPTION | VARCHAR2 | 1000 |  |  | Attribute Description. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWP_ATTRIBUTES_TL_PK | Unique | Default | ATTRIBUTE_ID, LANGUAGE, ORA_SEED_SET1 |
| HWP_ATTRIBUTES_TL_PK1 | Unique | Default | ATTRIBUTE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../33_Workforce_Predictions_Tables_Index.md)
