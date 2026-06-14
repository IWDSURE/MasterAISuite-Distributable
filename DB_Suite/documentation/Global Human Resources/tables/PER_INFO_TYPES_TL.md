# PER_INFO_TYPES_TL

This table stores the Translated Info Types setup data.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinfotypestl-3114.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perinfotypestl-3114.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_INFO_TYPES_TL_PK | CATEGORY, INFORMATION_TYPE, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CATEGORY | VARCHAR2 | 240 |  | Yes | Category of the Information Type |  |
| INFORMATION_TYPE | VARCHAR2 | 40 |  | Yes | Information type, maps to flexfield context. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Translated Description of the information type. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_INFO_TYPES_TL_PK | Unique | Default | CATEGORY, INFORMATION_TYPE, LANGUAGE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
