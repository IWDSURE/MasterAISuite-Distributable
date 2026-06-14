# PER_PERSON_ADDR_USAGES_F

This table is used to store the person address usages records.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonaddrusagesf-25212.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonaddrusagesf-25212.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERSON_ADDR_USAGES_F_PK | PERSON_ADDR_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PERSON_ADDR_USAGE_ID | NUMBER |  | 18 | Yes | System generated part of the primary key. Surrogate key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | The person to whom the address belongs, refers to PER_PERSONS |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ADDRESS_ID | NUMBER |  | 18 | Yes | The address which is owned by this usage record. |  |
| ADDRESS_TYPE | VARCHAR2 | 30 |  |  | Type of address, for example, home address, work address, etc. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Person Address Usage Attributes (PER_PERSON_ADDR_USG_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERSON_ADDR_USAGES_F_FK1 | Non Unique | Default | PERSON_ID |
| PER_PERSON_ADDR_USAGES_F_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_PERSON_ADDR_USAGES_F_FK3 | Non Unique | Default | ADDRESS_ID |
| PER_PERSON_ADDR_USAGES_F_PK | Unique | Default | PERSON_ADDR_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
