# PER_ABSENCE_ATTENDANCE_TYPES_B

PER_ABSENCE_ATTENDANCE_TYPES holds user definitions of absence types.
These types are used to identify specific types of absence or
attendance in PER_ABSENCE_ATTENDANCES. You can associate an absence
type with the input value of a non-recurring element to maintain a
running total of time taken. When an absence of this type is
subsequently given to an employee, a nonrecurring element entry is
automatically created for his or her primary assignment using the
duration of HOURS_OR_DAYS. The INCREASING_OR_DESCENDING_FLAG
determines whether the absence duration is mutiplied by -1 and the
running total for an assignment is the sum of all entries of
INPUT_VALUE_ID on the primary assignment.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsenceattendancetypesb-26562.html#perabsenceattendancetypesb-26562](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsenceattendancetypesb-26562.html#perabsenceattendancetypesb-26562)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ABSENCE_ATTENDANCE_TYP_PK | ABSENCE_ATTENDANCE_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| ABSENCE_ATTENDANCE_TYPE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  | Active |
| SCH_BASED_DUR | VARCHAR2 | 1 |  |  | Absence duration based on worker?s work schedule. |  |  |
| PER_OR_WORKREL_FLAG | VARCHAR2 | 1 |  |  | Indicates whether absence recording is at Person level or Work Relationship level.? Absence recording at the Person level uses the worker's primary assignment. |  |  |
| OVERRIDE_FLAG | VARCHAR2 | 1 |  |  | Indicates if users can override the duration value that the application calculates on the basis of the absence dates. |  |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Input value associated with the payroll element. |  | Active |
| DATE_EFFECTIVE | DATE |  |  | Yes | Indicates the date when the absence Type is effective from. |  | Active |
| ABSENCE_CATEGORY | VARCHAR2 | 30 |  |  | Absence category of the absence. |  | Active |
| DATE_END | DATE |  |  |  | Indicates the date until when the absence type is effective. |  | Active |
| HOURS_OR_DAYS | VARCHAR2 | 1 |  |  | Indicates whether the absence duration is expressed in hours or days.? |  | Active |
| INCREASING_OR_DECREASING_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the element entry increases or decreases the balance. |  | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| USER_ROLE | VARCHAR2 | 30 |  |  | No longer used. |  | Active |
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ASSIGNMENT_STATUS_TYPES table. |  | Active |
| ADVANCE_PAY | VARCHAR2 | 30 |  |  | No longer used. |  | Active |
| ABSENCE_OVERLAP_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the absence created with this absence type can overlap with other absences. |  | Active |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) | Active |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Type Legislative Information (PER_ABSENCE_TYPE_LEG_DDF) |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Type Attributes (PER_ABSENCE_TYPE_DFF) |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ABS_ATTENDANCE_TYPES_N1 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PER_ABS_ATTENDANCE_TYPES_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ABS_ATTENDANCE_TYPES_PK | Unique | FUSION_TS_TX_IDX | ABSENCE_ATTENDANCE_TYPE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
