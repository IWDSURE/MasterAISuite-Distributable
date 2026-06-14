# PER_EMAIL_ADDRESSES

This table stores email addresses of different types for a person.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremailaddresses-10456.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremailaddresses-10456.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EMAIL_ADDRESSES_PK | EMAIL_ADDRESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| EMAIL_ADDRESS_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate key. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom this e-mail address is recorded. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| EMAIL_TYPE | VARCHAR2 | 30 |  | Yes | Type of email (e.g. work, personal) |  |
| DATE_FROM | DATE |  |  |  | Date from which e-mail address commences. |  |
| DATE_TO | DATE |  |  |  | Date e-mail address is valid to. |  |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | E-mail address.Not marked as mandatory in order to always allow creation of a first row for every person even when email is not provided. |  |
| MASTERED_IN_LDAP_FLAG | VARCHAR2 | 30 |  |  | Flag to indicate whether the email address is mastered in LDAP or not. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | E-mail Addresses Attributes (PER_EMAIL_ADDRESSES_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EMAIL_ADDRESSES_FK1 | Non Unique | Default | PERSON_ID |
| PER_EMAIL_ADDRESSES_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_EMAIL_ADDRESSES_N1 | Non Unique | Default | EMAIL_ADDRESS |
| PER_EMAIL_ADDRESSES_N2 | Non Unique | Default | UPPER("EMAIL_ADDRESS"), EMAIL_TYPE |
| PER_EMAIL_ADDRESSES_N3 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_EMAIL_ADDRESSES_PK | Unique | Default | EMAIL_ADDRESS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
