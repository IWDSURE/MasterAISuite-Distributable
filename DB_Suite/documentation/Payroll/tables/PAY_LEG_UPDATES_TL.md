# PAY_LEG_UPDATES_TL

PAY_LEG_UPDATES_TL - translation table for the translated name

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatestl-21876.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatestl-21876.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_LEG_UPDATES_TL_PK | PAY_STAT_UPDATE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_STAT_UPDATE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 120 |  | Yes | Name of the legislative update. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_LEG_UPDATES_TL_N1 | Non Unique | Default | UPPER("NAME"), LANGUAGE |
| PAY_LEG_UPDATES_TL_N2 | Non Unique | Default | NAME, LANGUAGE |
| PAY_LEG_UPDATES_TL_PK | Unique | Default | PAY_STAT_UPDATE_ID, LANGUAGE, ORA_SEED_SET1 |
| PAY_LEG_UPDATES_TL_PK1 | Unique | Default | PAY_STAT_UPDATE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
