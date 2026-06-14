# HRT_FEEDBACK_SUGGESTIONS_TL

Feedback suggestions translation table.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtfeedbacksuggestionstl-17261.html#hrtfeedbacksuggestionstl-17261](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtfeedbacksuggestionstl-17261.html#hrtfeedbacksuggestionstl-17261)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_FEEDBACK_SUGGESTIONS_TL_PK | SUGGESTION_ID, ENTERPRISE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUGGESTION_ID | NUMBER |  | 18 | Yes | Unique ID for the item |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SUGGESTION_DESCR | VARCHAR2 | 4000 |  |  | Suggestion text. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_FEEDBACK_SUGGESTIONS_TL_U1 | Unique | FUSION_TS_TX_DATA | SUGGESTION_ID, ENTERPRISE_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
