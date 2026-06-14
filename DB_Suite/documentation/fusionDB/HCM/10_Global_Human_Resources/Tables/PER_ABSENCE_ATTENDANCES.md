# PER_ABSENCE_ATTENDANCES

This table holds details of employee absences from work. Records can be entered with PROJECTED dates and later confirmed as actual. Projected absences have no impact on absence balances.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsenceattendances-16843.html#perabsenceattendances-16843](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsenceattendances-16843.html#perabsenceattendances-16843)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ABSENCE_ATTENDANCES_PK | ABSENCE_ATTENDANCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| ABSENCE_ATTENDANCE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |  |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERIODS_OF_SERVICE table. |  |  |
| LINKED_ABSENCE_ID | NUMBER |  | 18 |  | No longer used. |  |  |
| MATERNITY_ID | NUMBER |  | 18 |  | ID of the maternity absence type that this absence is associated with. |  |  |
| SSP1_ISSUED | VARCHAR2 | 30 |  |  | Indicates whether statutory sick pay was paid. |  |  |
| PREGNANCY_RELATED_ILLNESS | VARCHAR2 | 30 |  |  | Indicates if this sickness absence is associated with maternity. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| ABSENCE_ATTENDANCE_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ABSENCE_ATTENDANCE_TYPES_B table. |  |  |
| ABS_ATTENDANCE_REASON_ID | NUMBER |  | 18 |  | Foreign Key to PER_ABS_ATTENDANCE_REASONS table. |  | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table. Identifies the person. |  | Active |
| PERIOD_OF_INCAPACITY_ID | NUMBER |  | 9 |  | No longer used. |  | Active |
| DATE_END | DATE |  |  |  | End date of the absence. |  | Active |
| DATE_NOTIFICATION | DATE |  |  |  | Date when the worker notified employer about the absence. |  | Active |
| DATE_PROJECTED_END | DATE |  |  |  | Projected end date of the absence. |  | Active |
| DATE_PROJECTED_START | DATE |  |  |  | Projected start date of the absence. |  | Active |
| DATE_START | DATE |  |  |  | Start date of the absence. |  | Active |
| TIME_END | VARCHAR2 | 5 |  |  | End time of the absence. |  | Active |
| TIME_PROJECTED_END | VARCHAR2 | 5 |  |  | Projected end time of the absence. |  | Active |
| TIME_PROJECTED_START | VARCHAR2 | 5 |  |  | Projected start time of the absence . |  | Active |
| TIME_START | VARCHAR2 | 5 |  |  | Start time of the absence. |  | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| ABS_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) | Active |
| ABS_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| ABS_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Legislative Information (PER_ABSENCE_LEG_DDF) |  |
| BATCH_ID | NUMBER |  | 9 |  | No longer used. |  | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| ABSENCE_CASE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ABSENCE_CASES table. |  | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Attributes (PER_ABSENCE_DFF) |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ABSENCE_ATTENDANCES_FK1 | Non Unique | Default | ABSENCE_ATTENDANCE_TYPE_ID |
| PER_ABSENCE_ATTENDANCES_FK2 | Non Unique | Default | ABS_ATTENDANCE_REASON_ID |
| PER_ABSENCE_ATTENDANCES_FK3 | Non Unique | Default | ABSENCE_CASE_ID |
| PER_ABSENCE_ATTENDANCES_N1 | Non Unique | Default | PERSON_ID |
| PER_ABSENCE_ATTENDANCES_PK | Unique | Default | ABSENCE_ATTENDANCE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
