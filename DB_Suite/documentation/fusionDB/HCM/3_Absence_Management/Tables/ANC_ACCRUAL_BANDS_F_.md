# ANC_ACCRUAL_BANDS_F_

Absence Accrual Bands Base Table

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancaccrualbandsf-18713.html#ancaccrualbandsf-18713](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancaccrualbandsf-18713.html#ancaccrualbandsf-18713)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_ACCRUAL_BANDS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ACCRUAL_BAND_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCRUAL_BAND_ID | NUMBER |  | 18 | Yes | Accrual Band |
| LIST_ID | NUMBER |  | 18 |  | HCM List Unique Identifier in hr vbcs lists table |
| ABSENCE_PLAN_ID | NUMBER |  | 18 |  | Absence Plan |
| ANC_ACCRUAL_BANDS_F_ALTCD | VARCHAR2 | 240 |  |  | Accrual Bands Alternate Code |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |
| ACC_BAND_SEQUENCE | NUMBER |  |  |  | Accrual Band Sequence |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ACC_INPUT_EXPRESSION | CLOB |  |  |  | Accrual Input Expression |
| ACCRUAL_RATE | NUMBER |  |  |  | Accrual Rate |
| ACCRUAL_CEILING | NUMBER |  |  |  | Accrual Ceiling |
| ANNUAL_ACC_LIMIT | NUMBER |  |  |  | ANNUAL_ACC_LIMIT |
| ACC_CARRYOVER_LIMIT | NUMBER |  |  |  | Accrual Carryover Limit |
| ACC_OUTPUT_FORMULA_ID | NUMBER |  | 18 |  | Accrual Output Formula |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Information Category |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Information Column 1 |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Information Column 2 |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Information Column 3 |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Information Column 4 |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Information Column 5 |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Information Column 6 |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Information Column 7 |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Information Column 8 |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Information Column 9 |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Information Column 10 |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Information Column 11 |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Information Column 12 |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Information Column 13 |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Information Column 14 |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Information Column 15 |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Information Column 16 |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Information Column 17 |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Information Column 18 |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Information Column 19 |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Information Column 20 |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Information Column 21 |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Information Column 22 |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Information Column 23 |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Information Column 24 |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Information Column 25 |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Information Column 26 |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Information Column 27 |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Information Column 28 |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Information Column 29 |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Information Column 30 |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
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
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | Information Number Column 1 |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | Information Number Column 2 |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | Information Number Column 3 |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | Information Number Column 4 |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | Information Number Column 5 |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | Information Number Column 6 |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | Information Number Column 7 |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | Information Number Column 8 |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | Information Number Column 9 |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | Information Number Column 10 |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | Information Number Column 11 |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | Information Number Column 12 |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | Information Number Column 13 |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | Information Number Column 14 |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | Information Number Column 15 |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | Information Number Column 16 |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | Information Number Column 17 |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | Information Number Column 18 |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | Information Number Column 19 |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | Information Number Column 20 |
| INFORMATION_DATE1 | DATE |  |  |  | Information Date Column 1 |
| INFORMATION_DATE2 | DATE |  |  |  | Information Date Column 2 |
| INFORMATION_DATE3 | DATE |  |  |  | Information Date Column 3 |
| INFORMATION_DATE4 | DATE |  |  |  | Information Date Column 4 |
| INFORMATION_DATE5 | DATE |  |  |  | Information Date Column 5 |
| INFORMATION_DATE6 | DATE |  |  |  | Information Date Column 6 |
| INFORMATION_DATE7 | DATE |  |  |  | Information Date Column 7 |
| INFORMATION_DATE8 | DATE |  |  |  | Information Date Column 8 |
| INFORMATION_DATE9 | DATE |  |  |  | Information Date Column 9 |
| INFORMATION_DATE10 | DATE |  |  |  | Information Date Column 10 |
| INFORMATION_DATE11 | DATE |  |  |  | Information Date Column 11 |
| INFORMATION_DATE12 | DATE |  |  |  | Information Date Column 12 |
| INFORMATION_DATE13 | DATE |  |  |  | Information Date Column 13 |
| INFORMATION_DATE14 | DATE |  |  |  | Information Date Column 14 |
| INFORMATION_DATE15 | DATE |  |  |  | Information Date Column 15 |
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
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
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
| ANC_CHAR1 | VARCHAR2 | 255 |  |  | Absence Character column 1 |
| ANC_CHAR2 | VARCHAR2 | 255 |  |  | Absence Character column 2 |
| ANC_CHAR3 | VARCHAR2 | 255 |  |  | Absence Character column 3 |
| ANC_CHAR4 | VARCHAR2 | 255 |  |  | Absence Character column 4 |
| ANC_CHAR5 | VARCHAR2 | 255 |  |  | Absence Character column 5 |
| ANC_NUMBER1 | NUMBER |  |  |  | Absence Number column 1 |
| ANC_NUMBER2 | NUMBER |  |  |  | Absence Number column 2 |
| ANC_NUMBER3 | NUMBER |  |  |  | Absence Number column 3 |
| ANC_NUMBER4 | NUMBER |  |  |  | Absence Number column 4 |
| ANC_NUMBER5 | NUMBER |  |  |  | Absence Number column 5 |
| ANC_DATE1 | DATE |  |  |  | Absence Date column 1 |
| ANC_DATE2 | DATE |  |  |  | Absence Date column 2 |
| ANC_DATE3 | DATE |  |  |  | Absence Date column 3 |
| ANC_DATE4 | DATE |  |  |  | Absence Date column 4 |
| ANC_DATE5 | DATE |  |  |  | Absence Date column 5 |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_ACCRUAL_BANDS_FN1_ | Non Unique | Default | ACCRUAL_BAND_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| ANC_ACCRUAL_BANDS_FU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ACCRUAL_BAND_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
