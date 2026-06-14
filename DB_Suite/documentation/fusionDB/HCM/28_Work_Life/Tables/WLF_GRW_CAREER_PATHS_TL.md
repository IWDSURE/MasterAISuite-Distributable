# WLF_GRW_CAREER_PATHS_TL

Table to store the translated text field(s) for career paths.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwcareerpathstl-16798.html#wlfgrwcareerpathstl-16798](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwcareerpathstl-16798.html#wlfgrwcareerpathstl-16798)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_CAREER_PATHS_TL_PK | CAREER_PATH_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAREER_PATH_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 1000 |  | Yes | The user provided name of the career path. |
| DESCRIPTION | VARCHAR2 | 4000 |  | Yes | The user provided description of the career path. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_CAREER_PATHS_TL_U1 | Unique | Default | CAREER_PATH_ID, LANGUAGE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
