# PER_CONTACT_EXTRA_INFO_F

This table records the Extra Information particular to a contact relationship.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percontactextrainfof-27929.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percontactextrainfof-27929.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CONTACT_EXTRA_INFO_F_PK | CONTACT_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| CONTACT_EXTRA_INFO_ID | NUMBER |  | 18 | Yes | System generated part of primary key. Surrogate key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| CONTACT_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | Contact Relationship ID to which this record applies. |  |
| INFORMATION_TYPE | VARCHAR2 | 30 |  | Yes | The information type, from PER_INFO_TYPES_B |  |
| CEI_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Oracle-reserved descriptive flexfield structure defining column |  |
| CEI_INFORMATION1 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION2 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION3 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION4 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION5 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION6 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION7 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION8 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION9 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION10 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION11 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION12 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION13 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION14 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION15 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION16 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION17 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION18 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION19 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION20 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION21 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION22 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION23 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION24 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION25 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION26 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION27 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION28 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION29 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION30 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column |  |
| CEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive flexfield structure defining column | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CEI_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Contact EIT Attributes (PER_PERSON_CONTACT_EIT_DFF) |
| CEI_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| CEI_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_CONTACT_EXTRA_INFO_FK1 | Non Unique | Default | CONTACT_RELATIONSHIP_ID |
| PER_CONTACT_EXTRA_INFO_F_PK | Unique | Default | CONTACT_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_CONTACT_EXTRA_INFO_N1 | Non Unique | Default | INFORMATION_TYPE, CONTACT_RELATIONSHIP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
