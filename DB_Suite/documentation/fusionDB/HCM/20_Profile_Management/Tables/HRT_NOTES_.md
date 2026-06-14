# HRT_NOTES_

This Table is for HCM Notes Functionality.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtnotes-30384.html#hrtnotes-30384](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtnotes-30384.html#hrtnotes-30384)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_NOTES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, NOTE_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTE_ID | NUMBER |  | 18 | Yes | Primary Key identifier of a task. |
| HIDDEN_FLAG | VARCHAR2 | 1 |  |  | Feedback Hidden Flag |
| RECEIVER_ID | NUMBER |  | 18 |  | Notes Receiver ID |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Kudos/Notes Active Flag |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE ID for SAAS compliance |
| NOTE_TYPE_CODE | VARCHAR2 | 30 |  |  | Classification of notes. eg- General Notes/Meeting Notes |
| NOTE_TEXT | CLOB |  |  |  | Stores the actual note information. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Source Object Type of the object against which the note is created. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Source Object Identifier of the object against which the note is created. |
| AUTHOR_ID | NUMBER |  | 18 | Yes | Person Identifier of the creator of the note. |
| VISIBILITY_FLAG | VARCHAR2 | 1 |  |  | This will be 'P' for private notes. |
| NOTE_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Required for display purposes in the UI. |
| NOTE_CREATION_DATE | TIMESTAMP |  |  |  | Required for display purpose in UI |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CONTEXT_TYPE | VARCHAR2 | 30 |  |  | Context Type of Note |
| CONTEXT_ID | NUMBER |  | 18 |  | Context Identifier of the note. |
| NOTE_VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Specify the visibility of the note. |
| CONTEXT_NAME_VO | VARCHAR2 | 300 |  |  | Specify the VO for retrieving context name. |
| CONTEXT_TYPE2 | VARCHAR2 | 30 |  |  | Additional Context Type of Note |
| CONTEXT_ID2 | NUMBER |  | 18 |  | Additional Context Identifier of the note. |
| CONTEXT_NAME_VO2 | VARCHAR2 | 300 |  |  | Specify the VO for retrieving additional context name. |
| NOTE_TEXT_AUDIT | VARCHAR2 | 4000 |  |  | Stores the actual note information for auditing. |
| CARD_TITLE | VARCHAR2 | 500 |  |  | Title of the card that is associated with this note |
| IMAGE_REFERENCE_URL | VARCHAR2 | 4000 |  |  | Image reference URL that is associated with this note |
| REFERENCE_COUNT | NUMBER |  | 18 |  | Reference count |
| NOTE_CODE | VARCHAR2 | 35 |  |  | Alternate key or user key that contains a user defined value that can be used to identify a note record |
| TAG_LIST | VARCHAR2 | 2000 |  |  | Specify list of person who are tagged for this note |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_NOTESN1_ | Non Unique | Default | NOTE_ID, ENTERPRISE_ID, LAST_UPDATE_DATE |
| HRT_NOTES_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, NOTE_ID, ENTERPRISE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
