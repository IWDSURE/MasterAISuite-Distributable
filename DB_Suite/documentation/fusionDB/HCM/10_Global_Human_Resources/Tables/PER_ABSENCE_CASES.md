# PER_ABSENCE_CASES

This table is to store the Details of Absence Cases. Absence Case is a collection of Absences of an Employee grouped manually based on some criteria.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsencecases-18007.html#perabsencecases-18007](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perabsencecases-18007.html#perabsencecases-18007)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ABSENCE_CASES_PK | ABSENCE_CASE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ABSENCE_CASE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |  |
| START_DATE | TIMESTAMP |  |  |  | ST DATE |  |
| END_DATE | TIMESTAMP |  |  |  | END DT |  |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERIODS_OF_SERVICE table. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| NAME | VARCHAR2 | 240 |  | Yes | Identifies the name for the absence case. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table. Identifies the person. |  |
| INCIDENT_ID | NUMBER |  | 18 |  | Foreign key to PER_WORK_INCIDENTS table. |  |
| ABSENCE_CATEGORY | VARCHAR2 | 30 |  |  | A group of related absence types for reporting purposes. |  |
| AC_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| AC_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Absence Case Legislative Information (PER_ABSENCE_CASE_LEG_DDF) |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Absence Case Attributes (PER_ABSENCE_CASE_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | Denotes description for the Absence Case. |  |
| ABSENCE_CATEGORY_ID | NUMBER |  | 18 |  | ABSENCE_CATEGORY_ID |  |
| ABSENCE_CASE_CODE | VARCHAR2 | 35 |  | Yes | Alternate key or user key that contains a user defined value that can be used to identify an absence case record |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ABSENCE_CASES_N1 | Non Unique | Default | PERSON_ID |
| PER_ABSENCE_CASES_N2 | Non Unique | Default | ABSENCE_CATEGORY |
| PER_ABSENCE_CASES_N3 | Non Unique | Default | ABSENCE_CATEGORY_ID |
| PER_ABSENCE_CASES_N4 | Non Unique | Default | START_DATE |
| PER_ABSENCE_CASES_PK | Unique | Default | ABSENCE_CASE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
