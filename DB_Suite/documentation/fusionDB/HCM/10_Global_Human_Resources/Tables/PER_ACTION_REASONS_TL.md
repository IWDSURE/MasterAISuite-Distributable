# PER_ACTION_REASONS_TL

This table will store a list of action reasons for each action. This will also be translatable.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionreasonstl-20601.html#peractionreasonstl-20601](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionreasonstl-20601.html#peractionreasonstl-20601)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACTION_REASONS_TL_PK | ACTION_REASON_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_REASON_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate Key. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| ACTION_REASON | VARCHAR2 | 80 |  | Yes | Translation for the action reason |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Translated long Description. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ACTION_REASONS_TL_PK | Unique | Default | ACTION_REASON_ID, LANGUAGE, ORA_SEED_SET1 |
| PER_ACTION_REASONS_TL_PK1 | Unique | Default | ACTION_REASON_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
