# PER_SENIORITY_DATES

This is transactional table for storing seniority dates.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persenioritydates-30819.html#persenioritydates-30819](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persenioritydates-30819.html#persenioritydates-30819)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SENIORITY_DATES_PK | SENIORITY_DATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SENIORITY_DATE_ID | NUMBER |  | 18 | Yes | This is unique Id for Seniority Date Item |
| SENIORITY_DATE_CODE | VARCHAR2 | 32 |  |  | This Code is used to identify the Seniority Date Item. |
| TRIGGERING_FIELD_NUMBER | NUMBER |  | 18 |  | This is the field on which the Seniority Date is defined. |
| TRIGGERING_FIELD_DATE | DATE |  |  |  | TRIGGERING_FIELD_DATE |
| TRIGGERING_FIELD_TEXT | VARCHAR2 | 150 |  |  | Stores seniority attributes like LegislationCode which is of type text. |
| TRIGGERING_FIELD | VARCHAR2 | 30 |  |  | Lookup code for the Triggering Field. |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | Lookup code for the Levels. |
| SENIORITY_DATE | DATE |  |  |  | Actual Seniority date value will be stored in this field.
User can override the value in this field. |
| PERSON_ID | NUMBER |  | 18 | Yes | This is Mandatory Field and it stores Person Id. |
| LEVEL_OBJECT_ID | NUMBER |  | 18 |  | LEVEL_OBJECT_ID |
| OVERRIDE_COMMENT | VARCHAR2 | 300 |  |  | OVERRIDE_COMMENT |
| DEFAULTED_SENIORITY_DATE | DATE |  |  |  | The Seniority Date value, when the the seniority record is first created. Even if user overrides Seniority Date this value will not change. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | ACTION_OCCURRENCE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SDT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | DFF Context Column |
| SDT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | DFF Segment Column For Text Type |
| SDT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | DFF Segment Column For Number Type |
| SDT_ATTRIBUTE_DATE1 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE2 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE3 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE4 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE5 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE6 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE7 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE8 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE9 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE10 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE11 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE12 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE13 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE14 | DATE |  |  |  | DFF Segment Column For Date Type |
| SDT_ATTRIBUTE_DATE15 | DATE |  |  |  | DFF Segment Column For Date Type |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SENIORITY_DATES_N1 | Non Unique | Default | PERSON_ID, SENIORITY_DATE_CODE, TRIGGERING_FIELD_NUMBER |
| PER_SENIORITY_DATES_U1 | Unique | Default | SENIORITY_DATE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
