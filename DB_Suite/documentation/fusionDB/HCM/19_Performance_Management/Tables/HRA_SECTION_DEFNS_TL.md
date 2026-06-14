# HRA_SECTION_DEFNS_TL

Section definitions (Translates)

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrasectiondefnstl-24405.html#hrasectiondefnstl-24405](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrasectiondefnstl-24405.html#hrasectiondefnstl-24405)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_SECTION_DEFNS_TL_PK | SECTION_DEF_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SECTION_DEF_ID | NUMBER |  | 18 | Yes | Foreign key to section definition and part of the composite primary key. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Translated name of the section. |  |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of the section. |  |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comments for the section. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_SECTION_DEFNS_TL_PK | Unique | Default | SECTION_DEF_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
