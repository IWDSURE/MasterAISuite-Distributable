# WLF_LMC_CONTENT_PREFERENCES

SCORM content stored preferences for a user

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmccontentpreferences-24949.html#wlflmccontentpreferences-24949](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmccontentpreferences-24949.html#wlflmccontentpreferences-24949)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_CONTENT_PREFERENCES_PK | CONTENT_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_PREFERENCE_ID | NUMBER |  | 18 | Yes | CONTENT_PREFERENCE_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to the PER_PERSONS table |
| CONTENT_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
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
| USER_ID | NUMBER |  | 18 |  | Obsolete.  Replaced by PERSON_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LMC_CONTENT_PREFS_N1 | Non Unique | Default | PERSON_ID, CONTENT_ID |
| WLF_LMC_CONTENT_PREFS_PK | Unique | FUSION_TS_TX_DATA | CONTENT_PREFERENCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
