# HTS_WORK_PATTERNS_TL

Table to store translatable name of a work pattern

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternstl-15290.html#htsworkpatternstl-15290](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsworkpatternstl-15290.html#htsworkpatternstl-15290)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WORK_PATTERNS_TL_PK | WORK_PATTERN_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WORK_PATTERN_ID | NUMBER |  | 18 | Yes | Unique identifier for a work shift in base table. |
| WORK_PATTERN_NAME | VARCHAR2 | 240 |  |  | Name provided to identify the work pattern. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WORK_PATTERNS_TL_U1 | Unique | Default | WORK_PATTERN_ID, LANGUAGE |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
