# HRT_LANG_SUGGESTIONS_TL

Language Suggestions translation table

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtlangsuggestionstl-7143.html#hrtlangsuggestionstl-7143](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtlangsuggestionstl-7143.html#hrtlangsuggestionstl-7143)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_LANG_SUGGESTIONS_TL_PK | SUGGESTION_ID, LANGUAGE, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUGGESTION_ID | NUMBER |  | 18 | Yes | Unique identifier for Language Suggestions |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | This is the unique identifier for the enterprise. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SUGGESTION_TEXT | VARCHAR2 | 2000 |  | Yes | Suggestion Text captures an example of the recommended way to use language. |
| PROPER_USE_TEXT | VARCHAR2 | 2000 |  |  | Proper Use Text captures the recommended way to use language, without using the keywords that are not recommended. |
| IMPROPER_USE_TEXT | VARCHAR2 | 4000 |  |  | Improper Use Text captures the non recommended way to use language and keywords. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_LANG_SUGGESTIONS_TL_U1 | Unique | FUSION_TS_TX_DATA | SUGGESTION_ID, LANGUAGE, ENTERPRISE_ID |
| HRT_LANG_SUGGESTIONS_TL_U2 | Unique | FUSION_TS_TX_DATA | SUGGESTION_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
