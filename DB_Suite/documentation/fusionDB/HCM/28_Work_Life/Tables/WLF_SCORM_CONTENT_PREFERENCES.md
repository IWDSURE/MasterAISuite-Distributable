# WLF_SCORM_CONTENT_PREFERENCES

SCORM content stored preferences for a user

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormcontentpreferences-14663.html#wlfscormcontentpreferences-14663](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormcontentpreferences-14663.html#wlfscormcontentpreferences-14663)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_CONTENT_PREFS_PK | CONTENT_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_PREFERENCE_ID | NUMBER |  | 18 | Yes | CONTENT_PREFERENCE_ID |
| ATTEMPT_INTERACTION_ID | NUMBER |  | 18 |  | FK to EVENT_ATTEMPT_INTERACTIONS.attempt_interaction_id |
| AUDIO_LEVEL | NUMBER |  |  |  | AUDIO_LEVEL |
| PREFERRED_LANGUAGE | VARCHAR2 | 250 |  |  | Indicates the code of the language into which the contents of the translatable columns are translated. |
| DELIVERY_SPEED | NUMBER |  |  |  | DELIVERY_SPEED |
| AUDIO_CAPTIONING | NUMBER |  |  |  | AUDIO_CAPTIONING |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SCORM_CONTENT_PREFS_N1 | Non Unique | Default | ATTEMPT_INTERACTION_ID |
| WLF_SCORM_CONTENT_PREFS_U1 | Unique | FUSION_TS_TX_DATA | CONTENT_PREFERENCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
