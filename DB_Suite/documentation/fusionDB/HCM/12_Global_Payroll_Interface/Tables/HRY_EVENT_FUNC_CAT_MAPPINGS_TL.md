# HRY_EVENT_FUNC_CAT_MAPPINGS_TL

Event Functional Categories Translation Table Data.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventfunccatmappingstl-25970.html#hryeventfunccatmappingstl-25970](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventfunccatmappingstl-25970.html#hryeventfunccatmappingstl-25970)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EVENT_FUNC_CAT_MAP_TL_PK | EVENT_FUNC_CAT_MAP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_FUNC_CAT_MAP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EVENT_FUNC_CAT_NAME | VARCHAR2 | 80 |  | Yes | Name of the Event Functional Category supported in Payroll Connect. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of the Event Category. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy  partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EVENT_FUNC_CAT_MAP_TL_PK | Unique | Default | EVENT_FUNC_CAT_MAP_ID, LANGUAGE, ORA_SEED_SET1 |
| HRY_EVENT_FUNC_CAT_MAP_TL_PK1 | Unique | Default | EVENT_FUNC_CAT_MAP_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
