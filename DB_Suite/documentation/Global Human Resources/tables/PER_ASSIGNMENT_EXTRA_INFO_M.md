# PER_ASSIGNMENT_EXTRA_INFO_M

This stores extensible data (Customer, Localization or Verticalization) for Assignments or Sets of Employment/Placement Terms. Changes are related to making this table "Effective Dated".

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentextrainfom-24132.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentextrainfom-24132.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASSIGN_EXTRA_INFO_M_PK | ASSIGNMENT_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_EXTRA_INFO_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_ASSIGNMENTS_M. |
| INFORMATION_TYPE | VARCHAR2 | 40 |  | Yes | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| AEI_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| AEI_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| AEI_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| AEI_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 | Yes | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| AEI_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AEI_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| EFFECTIVE_LATEST_CHANGE | VARCHAR2 | 30 |  | Yes | Date Effective Entity: 'Y' indicates that this row represents the latest change in the day. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from the Legal Entity. |
| AEI_INFORMATION_NUMBER1 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER2 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER3 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER4 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER5 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER6 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER7 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER8 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER9 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER10 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER11 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER12 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER13 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER14 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER15 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER16 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER17 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER18 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER19 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_NUMBER20 | NUMBER |  |  |  | Developer flex field numeric column |
| AEI_INFORMATION_DATE1 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE2 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE3 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE4 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE5 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE6 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE7 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE8 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE9 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE10 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE11 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE12 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE13 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE14 | DATE |  |  |  | Developer flex field date column |
| AEI_INFORMATION_DATE15 | DATE |  |  |  | Developer flex field date column |
| AEI_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive flex field numeric column |
| AEI_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive flex field date column |
| AEI_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive flex field date column |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASSIGN_EXTRA_INFO_M_N1 | Non Unique | Default | ASSIGNMENT_ID |
| PER_ASSIGN_EXTRA_INFO_M_PK | Unique | Default | ASSIGNMENT_EXTRA_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, EFFECTIVE_LATEST_CHANGE, EFFECTIVE_SEQUENCE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
