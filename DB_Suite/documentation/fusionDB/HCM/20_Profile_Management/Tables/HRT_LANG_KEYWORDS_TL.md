# HRT_LANG_KEYWORDS_TL

Language Suggestion Keywords translation table

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtlangkeywordstl-9930.html#hrtlangkeywordstl-9930](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtlangkeywordstl-9930.html#hrtlangkeywordstl-9930)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_LANG_KEYWORDS_TL_PK | KEYWORD_ID, LANGUAGE, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEYWORD_ID | NUMBER |  | 18 | Yes | Unique identifier of Keywords for Language Suggestion |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This is the unique identifier for the enterprise. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| KEYWORDS | VARCHAR2 | 200 |  | Yes | Keywords for the Language Ssuggestion. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_LANG_KEYWORDS_TL_U1 | Unique | FUSION_TS_TX_DATA | KEYWORD_ID, LANGUAGE, ENTERPRISE_ID |
| HRT_LANG_KEYWORDS_TL_U2 | Unique | FUSION_TS_TX_DATA | KEYWORD_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
