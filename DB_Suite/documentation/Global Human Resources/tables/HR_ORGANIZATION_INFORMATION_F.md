# HR_ORGANIZATION_INFORMATION_F

This table holds the information types data for organizations.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationinformationf-16628.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationinformationf-16628.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ORG_INFORMATION_PK | ORG_INFORMATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ORG_INFORMATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |  |
| ORG_INFORMATION_CONTEXT | VARCHAR2 | 80 |  | Yes | Indicates the context of the descriptive flexfields. |  |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F | Active |
| ORG_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Active |
| ORG_INFORMATION_NUMBER1 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER2 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER3 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER4 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER5 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER6 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER7 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER8 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER9 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER10 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER11 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER12 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER13 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER14 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER15 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER16 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER17 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER18 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER19 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_NUMBER20 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE1 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE2 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE3 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE4 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE5 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE6 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE7 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE8 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE9 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE10 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE11 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE12 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE13 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE14 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ORG_INFORMATION_DATE15 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| SEQUENCE_NUMBER | NUMBER |  | 8 |  | Sequence Number for multi row contexts |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ORGANIZATION_INFORMATION_N1 | Non Unique | FUSION_TS_TX_DATA | ORG_INFORMATION_CONTEXT |
| HR_ORGANIZATION_INFORMATION_N2 | Non Unique | FUSION_TS_TX_DATA | ORGANIZATION_ID, ORG_INFORMATION_CONTEXT |
| HR_ORGANIZATION_INFORMATION_N3 | Non Unique | Default | UPPER("ORG_INFORMATION3") |
| HR_ORG_INFORMATION_F_N11 | Non Unique | Default | UPPER("ORG_INFORMATION1") |
| HR_ORG_INFORMATION_F_N12 | Non Unique | Default | UPPER("ORG_INFORMATION2") |
| HR_ORG_INFORMATION_F_N14 | Non Unique | Default | UPPER("ORG_INFORMATION4") |
| HR_ORG_INFORMATION_F_N15 | Non Unique | Default | UPPER("ORG_INFORMATION5") |
| HR_ORG_INFORMATION_F_N16 | Non Unique | Default | ORG_INFORMATION6 |
| HR_ORG_INFORMATION_F_N17 | Non Unique | Default | ORG_INFORMATION7 |
| HR_ORG_INFORMATION_F_N18 | Non Unique | Default | ORG_INFORMATION8 |
| HR_ORG_INFORMATION_F_N19 | Non Unique | Default | ORG_INFORMATION9 |
| HR_ORG_INFORMATION_F_N20 | Non Unique | Default | ORG_INFORMATION10 |
| HR_ORG_INFORMATION_F_N31 | Non Unique | Default | ORG_INFORMATION_NUMBER1 |
| HR_ORG_INFORMATION_F_N32 | Non Unique | Default | ORG_INFORMATION_NUMBER2 |
| HR_ORG_INFORMATION_F_N33 | Non Unique | Default | ORG_INFORMATION_NUMBER3 |
| HR_ORG_INFORMATION_F_N34 | Non Unique | Default | ORG_INFORMATION_NUMBER4 |
| HR_ORG_INFORMATION_F_N35 | Non Unique | Default | ORG_INFORMATION_NUMBER5 |
| HR_ORG_INFORMATION_F_N41 | Non Unique | Default | ORG_INFORMATION_DATE1 |
| HR_ORG_INFORMATION_F_N42 | Non Unique | Default | ORG_INFORMATION_DATE2 |
| HR_ORG_INFORMATION_F_N43 | Non Unique | Default | ORG_INFORMATION_DATE3 |
| HR_ORG_INFORMATION_F_N44 | Non Unique | Default | ORG_INFORMATION_DATE4 |
| HR_ORG_INFORMATION_F_N45 | Non Unique | Default | ORG_INFORMATION_DATE5 |
| HR_ORG_INFORMATION_PK | Unique | FUSION_TS_TX_DATA | ORG_INFORMATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORG_INFORMATION_U1 | Unique | Default | LAST_UPDATE_DATE, ORG_INFORMATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
