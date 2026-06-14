# PER_PHONES

This table stores phone numbers of different types for a person.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perphones-13476.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perphones-13476.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PHONES_PK | PHONE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PHONE_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate key. |  |
| LEGISLATION_CODE | VARCHAR2 | 4 |  |  | Legislation code derived from Legal Entity. |  |
| DATE_FROM | DATE |  |  | Yes | Date the phone number becomes effective |  |
| DATE_TO | DATE |  |  |  | Date the phone number stops being effective |  |
| PHONE_TYPE | VARCHAR2 | 30 |  | Yes | Indicates the phone type for which the details are stored. |  |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | Telephone number. Not marked as mandatory in order to always allow creation of a first phone row for every person even when phone number is not provided. |  |
| SPEED_DIAL_NUMBER | VARCHAR2 | 60 |  |  | Speed Dial Number of the Phone Number being created or updated. |  |
| AREA_CODE | VARCHAR2 | 30 |  |  | Area Code of the Phone Number being created or updated. |  |
| SEARCH_PHONE_NUMBER | VARCHAR2 | 240 |  |  | Derived column for internal use. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Phones Attributes (PER_PHONES_DFF) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| VALIDITY | VARCHAR2 | 30 |  |  | Valid times that this phone number can be used |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| COUNTRY_CODE_NUMBER | VARCHAR2 | 30 |  |  | Country code of the Phone Number |  |
| EXTENSION | VARCHAR2 | 60 |  |  | Extension number |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom this phone number  is recorded |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PHONES_FK1 | Non Unique | Default | PERSON_ID |
| PER_PHONES_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_PHONES_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_PHONES_N2 | Non Unique | Default | SEARCH_PHONE_NUMBER |
| PER_PHONES_N3 | Non Unique | Default | REVERSE("SEARCH_PHONE_NUMBER") |
| PER_PHONES_N4 | Non Unique | Default | TRANSLATE("SEARCH_PHONE_NUMBER",'0123456789'||TRANSLATE("SEARCH_PHONE_NUMBER",'x0123456789','x'),'0123456789') |
| PER_PHONES_PK | Unique | Default | PHONE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
