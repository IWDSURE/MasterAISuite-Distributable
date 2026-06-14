# FAI_SUPPT_OBJECT_FIELDS_TL

This table stores the display name and description of fields in supported business objects for agent tools in different languages.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisupptobjectfieldstl-28796.html#faisupptobjectfieldstl-28796](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisupptobjectfieldstl-28796.html#faisupptobjectfieldstl-28796)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_SUPPT_OBJECT_FIELDS_TL_PK | FIELD_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FIELD_ID | NUMBER |  | 18 | Yes | Foreign Key to the base table FAI_SUPPT_OBJECT_FIELDS_B. Part of the primary key. |
| FIELD_DISPLAY_NAME | VARCHAR2 | 400 |  | Yes | The translatable display name of the field. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The translatable description of the field. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_SUPPT_OBJECT_FIELDS_TL_PK | Unique | Default | FIELD_ID, LANGUAGE, ORA_SEED_SET1 |
| FAI_SUPPT_OBJECT_FIELDS_TL_PK1 | Unique | Default | FIELD_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
