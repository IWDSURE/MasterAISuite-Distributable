# ANC_PER_ABS_ENTRY_DTLS

This table holds information of  the person absence entry details.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentrydtls-26546.html#ancperabsentrydtls-26546](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentrydtls-26546.html#ancperabsentrydtls-26546)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_ENTRY_DTLS_PK | ENTERPRISE_ID, PER_ABS_ENTRY_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_ENTRY_DTL_ID | NUMBER |  | 18 | Yes | PER_ABS_ENTRY_DTL_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_ENTRY_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| ABSENCE_DATE | DATE |  |  |  | ABSENCE_DATE |
| ABSENCE_DATETIME | TIMESTAMP |  |  |  | Start Date time |
| ABSENCE_END_DATETIME | TIMESTAMP |  |  |  | End Date time |
| START_TIME | VARCHAR2 | 30 |  |  | START_TIME |
| END_TIME | VARCHAR2 | 30 |  |  | END_TIME |
| DURATION | NUMBER |  |  |  | DURATION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ROW_SEQ | NUMBER |  | 18 |  | row number used in HDL |
| SOURCE | VARCHAR2 | 10 |  |  | Represents the source of absence detail. |
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
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | INFORMATION_CATEGORY |
| INFORMATION1 | VARCHAR2 | 150 |  |  | INFORMATION1 |
| INFORMATION2 | VARCHAR2 | 150 |  |  | INFORMATION2 |
| INFORMATION3 | VARCHAR2 | 150 |  |  | INFORMATION3 |
| INFORMATION4 | VARCHAR2 | 150 |  |  | INFORMATION4 |
| INFORMATION5 | VARCHAR2 | 150 |  |  | INFORMATION5 |
| INFORMATION6 | VARCHAR2 | 150 |  |  | INFORMATION6 |
| INFORMATION7 | VARCHAR2 | 150 |  |  | INFORMATION7 |
| INFORMATION8 | VARCHAR2 | 150 |  |  | INFORMATION8 |
| INFORMATION9 | VARCHAR2 | 150 |  |  | INFORMATION9 |
| INFORMATION10 | VARCHAR2 | 150 |  |  | INFORMATION10 |
| INFORMATION11 | VARCHAR2 | 150 |  |  | INFORMATION11 |
| INFORMATION12 | VARCHAR2 | 150 |  |  | INFORMATION12 |
| INFORMATION13 | VARCHAR2 | 150 |  |  | INFORMATION13 |
| INFORMATION14 | VARCHAR2 | 150 |  |  | INFORMATION14 |
| INFORMATION15 | VARCHAR2 | 150 |  |  | INFORMATION15 |
| INFORMATION16 | VARCHAR2 | 150 |  |  | INFORMATION16 |
| INFORMATION17 | VARCHAR2 | 150 |  |  | INFORMATION17 |
| INFORMATION18 | VARCHAR2 | 150 |  |  | INFORMATION18 |
| INFORMATION19 | VARCHAR2 | 150 |  |  | INFORMATION19 |
| INFORMATION20 | VARCHAR2 | 150 |  |  | INFORMATION20 |
| INFORMATION21 | VARCHAR2 | 150 |  |  | INFORMATION21 |
| INFORMATION22 | VARCHAR2 | 150 |  |  | INFORMATION22 |
| INFORMATION23 | VARCHAR2 | 150 |  |  | INFORMATION23 |
| INFORMATION24 | VARCHAR2 | 150 |  |  | INFORMATION24 |
| INFORMATION25 | VARCHAR2 | 150 |  |  | INFORMATION25 |
| INFORMATION26 | VARCHAR2 | 150 |  |  | INFORMATION26 |
| INFORMATION27 | VARCHAR2 | 150 |  |  | INFORMATION27 |
| INFORMATION28 | VARCHAR2 | 150 |  |  | INFORMATION28 |
| INFORMATION29 | VARCHAR2 | 150 |  |  | INFORMATION29 |
| INFORMATION30 | VARCHAR2 | 150 |  |  | INFORMATION30 |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | INFORMATION_NUMBER1 |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | INFORMATION_NUMBER2 |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | INFORMATION_NUMBER3 |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | INFORMATION_NUMBER4 |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | INFORMATION_NUMBER5 |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | INFORMATION_NUMBER6 |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | INFORMATION_NUMBER7 |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | INFORMATION_NUMBER8 |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | INFORMATION_NUMBER9 |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | INFORMATION_NUMBER10 |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | INFORMATION_NUMBER11 |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | INFORMATION_NUMBER12 |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | INFORMATION_NUMBER13 |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | INFORMATION_NUMBER14 |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | INFORMATION_NUMBER15 |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | INFORMATION_NUMBER16 |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | INFORMATION_NUMBER17 |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | INFORMATION_NUMBER18 |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | INFORMATION_NUMBER19 |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | INFORMATION_NUMBER20 |
| INFORMATION_DATE1 | DATE |  |  |  | INFORMATION_DATE1 |
| INFORMATION_DATE2 | DATE |  |  |  | INFORMATION_DATE2 |
| INFORMATION_DATE3 | DATE |  |  |  | INFORMATION_DATE3 |
| INFORMATION_DATE4 | DATE |  |  |  | INFORMATION_DATE4 |
| INFORMATION_DATE5 | DATE |  |  |  | INFORMATION_DATE5 |
| INFORMATION_DATE6 | DATE |  |  |  | INFORMATION_DATE6 |
| INFORMATION_DATE7 | DATE |  |  |  | INFORMATION_DATE7 |
| INFORMATION_DATE8 | DATE |  |  |  | INFORMATION_DATE8 |
| INFORMATION_DATE9 | DATE |  |  |  | INFORMATION_DATE9 |
| INFORMATION_DATE10 | DATE |  |  |  | INFORMATION_DATE10 |
| INFORMATION_DATE11 | DATE |  |  |  | INFORMATION_DATE11 |
| INFORMATION_DATE12 | DATE |  |  |  | INFORMATION_DATE12 |
| INFORMATION_DATE13 | DATE |  |  |  | INFORMATION_DATE13 |
| INFORMATION_DATE14 | DATE |  |  |  | INFORMATION_DATE14 |
| INFORMATION_DATE15 | DATE |  |  |  | INFORMATION_DATE15 |
| DUR_PREF_CD | VARCHAR2 | 30 |  |  | Duration preference code for elapsed shift and UOM days. |
| UNPAID_BREAK_DURATION | NUMBER |  |  |  | UNPAID_BREAK_DURATION |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_ENTRY_DTLS_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID, ENTERPRISE_ID |
| ANC_PER_ABS_ENTRY_DTLS_UK1 | Unique | Default | ENTERPRISE_ID, PER_ABS_ENTRY_DTL_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
