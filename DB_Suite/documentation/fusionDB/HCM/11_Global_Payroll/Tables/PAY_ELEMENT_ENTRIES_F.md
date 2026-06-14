# PAY_ELEMENT_ENTRIES_F

This table contains element entries for each assignment. The actual values for each entry are held in PAY_ELEMENT_ENTRY_VALUES_F. An entry represents a specific instance of an element for a particular assignment. For example, there may be a salary element and each assignment receives a salary element entry.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelemententriesf-24243.html#payelemententriesf-24243](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelemententriesf-24243.html#payelemententriesf-24243)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_ENTRIES_F_PK | ELEMENT_ENTRY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | ELEMENT_ENTRY_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |  |
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | ELEMENT_TYPE_ID |  |
| ENTRY_TYPE | VARCHAR2 | 30 |  | Yes | ENTRY_TYPE |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATOR_TYPE | VARCHAR2 | 30 |  | Yes | CREATOR_TYPE |  |
| CREATOR_ID | NUMBER |  | 18 |  | CREATOR_ID |  |
| BATCH_ID | NUMBER |  | 18 |  | BATCH_ID |  |
| BATCH_ACTION_ID | NUMBER |  | 18 |  | BATCH_ACTION_ID |  |
| REASON | VARCHAR2 | 4000 |  |  | REASON |  |
| TARGET_ENTRY_ID | NUMBER |  | 18 |  | TARGET_ENTRY_ID |  |
| SUBPRIORITY | NUMBER |  | 9 |  | SUBPRIORITY |  |
| DATE_EARNED | DATE |  |  |  | DATE_EARNED |  |
| BALANCE_ADJ_COST_FLAG | VARCHAR2 | 30 |  |  | BALANCE_ADJ_COST_FLAG |  |
| MULTIPLE_ENTRY_COUNT | NUMBER |  | 18 |  | MULTIPLE_ENTRY_COUNT |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Entry Attributes (PAY_ELEMENT_ENTRIES_DFF) |
| ENTRY_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | ENTRY_INFORMATION_CATEGORY | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| ENTRY_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Entry Information (PAY_ELEMENT_ENTRIES_DDF) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ELEMENT_ENTRIES_F_FK1 | Non Unique | Default | ELEMENT_TYPE_ID, PERSON_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_ELEMENT_ENTRIES_F_FK2 | Non Unique | Default | PERSON_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_ELEMENT_ENTRIES_F_N1 | Non Unique | Default | CREATOR_ID, CREATOR_TYPE |
| PAY_ELEMENT_ENTRIES_F_N2 | Non Unique | Default | TARGET_ENTRY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, MULTIPLE_ENTRY_COUNT, CREATOR_TYPE |
| PAY_ELEMENT_ENTRIES_F_N3 | Non Unique | Default | ELEMENT_ENTRY_ID, ELEMENT_TYPE_ID |
| PAY_ELEMENT_ENTRIES_F_PK | Unique | Default | ELEMENT_ENTRY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
