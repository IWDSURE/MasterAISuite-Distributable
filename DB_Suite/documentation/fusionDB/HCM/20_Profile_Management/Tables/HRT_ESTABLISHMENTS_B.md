# HRT_ESTABLISHMENTS_B

This table is used to maintain a list of educational establishments e.g. schools, colleges, universities, etc.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtestablishmentsb-8151.html#hrtestablishmentsb-8151](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtestablishmentsb-8151.html#hrtestablishmentsb-8151)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_ESTABLISHMENTS_B_PK | ESTABLISHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ESTABLISHMENT_ID | NUMBER |  | 18 | Yes | Unique identifier of Establishment |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| SCHOOL_CODE | VARCHAR2 | 30 |  |  | School Code which has to be unique |  |
| PARTY_ID | NUMBER |  | 18 |  | Foreign key to Party table |  |
| COUNTRY_ID | NUMBER |  | 18 |  | Country Id |  |
| STATE_PROVINCE_ID | NUMBER |  | 18 |  | State Province Id |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Educational Establishments (HRT_ESTABLISHMENTS_B) |
| EST_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer descriptive flexfield structure defining column. |  |
| EST_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| EST_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_ESTABLISHMENTS_B_PK | Unique | Default | ESTABLISHMENT_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
