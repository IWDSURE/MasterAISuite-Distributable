# WLF_ADVISOR_TRANSLATIONS

Table to hold translations data for various objects

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfadvisortranslations-4777.html#wlfadvisortranslations-4777](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfadvisortranslations-4777.html#wlfadvisortranslations-4777)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ADVISOR_TRANSLATIONS_PK | ADVISOR_TRANSLATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADVISOR_TRANSLATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| ADVISOR_TRANSLATION_NUMBER | VARCHAR2 | 30 |  | Yes | System generated unique identifier for easy reference. |
| SKILLS_ADVISOR_PROCESS_ID | NUMBER |  | 18 | Yes | Bulk advisor request identifier. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of an object undergoing translation. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of an object undergoing translation. |
| SOURCE_LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the object was originally created. |
| TARGET_LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language to which object should be translated to. |
| ORIGINAL_TEXT1 | VARCHAR2 | 4000 |  |  | Original text1 of the object. |
| PROVIDER_TEXT1 | VARCHAR2 | 4000 |  |  | Translation text1 provided by the provider. |
| SELECTED_TEXT1 | VARCHAR2 | 4000 |  |  | Translation text1 that was selected by the user, post edits if any. |
| ORIGINAL_TEXT2 | VARCHAR2 | 4000 |  |  | Original text2 of the object |
| PROVIDER_TEXT2 | VARCHAR2 | 4000 |  |  | Translation text2 provided by the provider. |
| SELECTED_TEXT2 | VARCHAR2 | 4000 |  |  | Translation text2 that was selected by the user, post edits if any. |
| ORIGINAL_TEXT3 | VARCHAR2 | 4000 |  |  | Original text3 of the object. |
| PROVIDER_TEXT3 | VARCHAR2 | 4000 |  |  | Translation text3 provided by the provider. |
| SELECTED_TEXT3 | VARCHAR2 | 4000 |  |  | Translation text3 that was selected by the user, post edits if any. |
| ORIGINAL_HTML_TEXT1 | CLOB |  |  |  | Original HTML text1 of the object. |
| PROVIDER_HTML_TEXT1 | CLOB |  |  |  | Translation HTML text1 provided by the provider. |
| SELECTED_HTML_TEXT1 | CLOB |  |  |  | Translation HTML text1 that was selected by the user, post edits if any. |
| ORIGINAL_HTML_TEXT2 | CLOB |  |  |  | Original HTML text2 of the object. |
| PROVIDER_HTML_TEXT2 | CLOB |  |  |  | Translation HTML text2 provided by the provider. |
| SELECTED_HTML_TEXT2 | CLOB |  |  |  | Translation HTML text2 that was selected by the user, post edits if any. |
| PROCESSING_JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS job that processed the translation. |
| CURATED_FLAG | VARCHAR2 | 1 |  |  | Curated flag to capture users acceptance. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ADVISOR_TRANSLATIONS_N1 | Non Unique | Default | SKILLS_ADVISOR_PROCESS_ID |
| WLF_ADVISOR_TRANSLATIONS_N2 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE |
| WLF_ADVISOR_TRANSLATIONS_U1 | Unique | Default | ADVISOR_TRANSLATION_ID |
| WLF_ADVISOR_TRANSLATIONS_U2 | Unique | Default | ADVISOR_TRANSLATION_NUMBER |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
