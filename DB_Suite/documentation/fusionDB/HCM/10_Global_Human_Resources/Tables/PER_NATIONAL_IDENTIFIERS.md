# PER_NATIONAL_IDENTIFIERS

This table records National Identifiers for the person, in different Legislation Codes, and different types within a single legislation.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernationalidentifiers-19386.html#pernationalidentifiers-19386](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pernationalidentifiers-19386.html#pernationalidentifiers-19386)

## Primary Key

| Name | Columns |
|------|----------|
| PER_NATIONAL_IDENTIFIERS_PK | NATIONAL_IDENTIFIER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| NATIONAL_IDENTIFIER_ID | NUMBER |  | 18 | Yes | System generated part of primary key. Surrogate key. |  |
| PLACE_OF_ISSUE | VARCHAR2 | 30 |  |  | Place where the NID is issued. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Person for whom the NID is recorded. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | Legislation code derived from Legal Entity. |  |
| NATIONAL_IDENTIFIER_TYPE | VARCHAR2 | 30 |  |  | Type of National Identifier |  |
| NATIONAL_IDENTIFIER_NUMBER | VARCHAR2 | 30 |  |  | National identification number. Not marked as mandatory in order to always allow creation of a first row for every person even when NID is not provided. |  |
| ISSUE_DATE | DATE |  |  |  | Date of Issue |  |
| EXPIRATION_DATE | DATE |  |  |  | Expiration date of the national identifier |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | National Identifiers Attributes (PER_NATIONAL_IDENTIFIERS_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_NATIONAL_IDENTIFIERS_FK1 | Non Unique | Default | PERSON_ID |
| PER_NATIONAL_IDENTIFIERS_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_NATIONAL_IDENTIFIERS_N1 | Non Unique | Default | NATIONAL_IDENTIFIER_TYPE, NATIONAL_IDENTIFIER_NUMBER |
| PER_NATIONAL_IDENTIFIERS_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_NATIONAL_IDENTIFIERS_N3 | Non Unique | Default | UPPER("NATIONAL_IDENTIFIER_NUMBER") |
| PER_NATIONAL_IDENTIFIERS_PK | Unique | Default | NATIONAL_IDENTIFIER_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
