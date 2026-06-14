# WLF_GRW_GUIDES_F_TL

Table to store language-dependent translations for grow guides.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguidesftl-14379.html#wlfgrwguidesftl-14379](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguidesftl-14379.html#wlfgrwguidesftl-14379)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_GUIDES_F_TL_PK | GUIDE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GUIDE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 250 |  | Yes | Name of guide to succinctly capture the essence of the guide. |
| DESCRIPTION | CLOB |  |  |  | Long description about the guide. |
| PLAIN_DESCRIPTION | VARCHAR2 | 4000 |  |  | Brief description in plain text about the guide. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_GUIDES_F_TL_N1 | Non Unique | Default | LANGUAGE, NAME |
| WLF_GRW_GUIDES_F_TL_U1 | Unique | Default | GUIDE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
