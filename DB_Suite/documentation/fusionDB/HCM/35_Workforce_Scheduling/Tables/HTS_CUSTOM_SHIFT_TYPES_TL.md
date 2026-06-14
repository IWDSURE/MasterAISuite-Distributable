# HTS_CUSTOM_SHIFT_TYPES_TL

Translation table for Shifts. The table will store attributes for a shift that are translated in different languages.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscustomshifttypestl-7756.html#htscustomshifttypestl-7756](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htscustomshifttypestl-7756.html#htscustomshifttypestl-7756)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_CUSTOM_SHIFT_TYPES_TL_PK | SHIFT_TYPE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHIFT_TYPE_ID | NUMBER |  | 18 | Yes | Shift identifier to uniquely identify a shift |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SHIFT_NAME | VARCHAR2 | 240 |  | Yes | Name identifies a Shift. |
| SHIFT_DESC | VARCHAR2 | 2000 |  |  | Description can be used to provide additional details for a Shift. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID- Enterprise Id column |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_CUSTOM_SHIFT_TYPES_TL_UK1 | Unique | Default | SHIFT_TYPE_ID, LANGUAGE, ORA_SEED_SET1 |
| HTS_CUSTOM_SHIFT_TYPES_TL_UK11 | Unique | Default | SHIFT_TYPE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
