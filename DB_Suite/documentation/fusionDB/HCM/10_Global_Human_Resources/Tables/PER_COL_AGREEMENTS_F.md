# PER_COL_AGREEMENTS_F

This table stores Collective Agreements. Collective Agreements are agreements between workers and employers to support the regulation of working conditions.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percolagreementsf-6687.html#percolagreementsf-6687](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percolagreementsf-6687.html#percolagreementsf-6687)

## Primary Key

| Name | Columns |
|------|----------|
| PER_COL_AGREEMENTS_F_PK | COLLECTIVE_AGREEMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COLLECTIVE_AGREEMENT_ID | NUMBER |  | 18 | Yes | COLLECTIVE_AGREEMENT_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| STATUS | VARCHAR2 | 15 |  | Yes | STATUS |
| IDENTIFICATION_CODE | VARCHAR2 | 30 |  | Yes | IDENTIFICATION_CODE |
| LEGISLATION_CODE | VARCHAR2 | 150 |  | Yes | LEGISLATION_CODE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CATEGORY_CODE | VARCHAR2 | 80 |  | Yes | Extensible Flexfield Category Code |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BARGAINING_UNIT_CODE | VARCHAR2 | 30 |  |  | BARGAINING_UNIT_CODE |
| UNION_ID | NUMBER |  | 18 |  | UNION_ID |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | DESCRIPTION |
| EMPLOYEE_ORG_NAME | VARCHAR2 | 150 |  |  | EMPLOYEE_ORG_NAME |
| EMPLOYEE_ORG_CONTACT | VARCHAR2 | 150 |  |  | EMPLOYEE_ORG_CONTACT |
| EMPLOYER_ORG_NAME | VARCHAR2 | 150 |  |  | EMPLOYER_ORG_NAME |
| EMPLOYER_ORG_CONTACT | VARCHAR2 | 150 |  |  | EMPLOYER_ORG_CONTACT |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAG_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | CAG_INFORMATION_CATEGORY |
| CAG_INFORMATION1 | VARCHAR2 | 150 |  |  | CAG_INFORMATION1 |
| CAG_INFORMATION2 | VARCHAR2 | 150 |  |  | CAG_INFORMATION2 |
| CAG_INFORMATION3 | VARCHAR2 | 150 |  |  | CAG_INFORMATION3 |
| CAG_INFORMATION4 | VARCHAR2 | 150 |  |  | CAG_INFORMATION4 |
| CAG_INFORMATION5 | VARCHAR2 | 150 |  |  | CAG_INFORMATION5 |
| CAG_INFORMATION6 | VARCHAR2 | 150 |  |  | CAG_INFORMATION6 |
| CAG_INFORMATION7 | VARCHAR2 | 150 |  |  | CAG_INFORMATION7 |
| CAG_INFORMATION8 | VARCHAR2 | 150 |  |  | CAG_INFORMATION8 |
| CAG_INFORMATION9 | VARCHAR2 | 150 |  |  | CAG_INFORMATION9 |
| CAG_INFORMATION10 | VARCHAR2 | 150 |  |  | CAG_INFORMATION10 |
| CAG_INFORMATION11 | VARCHAR2 | 150 |  |  | CAG_INFORMATION11 |
| CAG_INFORMATION12 | VARCHAR2 | 150 |  |  | CAG_INFORMATION12 |
| CAG_INFORMATION13 | VARCHAR2 | 150 |  |  | CAG_INFORMATION13 |
| CAG_INFORMATION14 | VARCHAR2 | 150 |  |  | CAG_INFORMATION14 |
| CAG_INFORMATION15 | VARCHAR2 | 150 |  |  | CAG_INFORMATION15 |
| CAG_INFORMATION16 | VARCHAR2 | 150 |  |  | CAG_INFORMATION16 |
| CAG_INFORMATION17 | VARCHAR2 | 150 |  |  | CAG_INFORMATION17 |
| CAG_INFORMATION18 | VARCHAR2 | 150 |  |  | CAG_INFORMATION18 |
| CAG_INFORMATION19 | VARCHAR2 | 150 |  |  | CAG_INFORMATION19 |
| CAG_INFORMATION20 | VARCHAR2 | 150 |  |  | CAG_INFORMATION20 |
| CAG_INFORMATION21 | VARCHAR2 | 150 |  |  | CAG_INFORMATION21 |
| CAG_INFORMATION22 | VARCHAR2 | 150 |  |  | CAG_INFORMATION22 |
| CAG_INFORMATION23 | VARCHAR2 | 150 |  |  | CAG_INFORMATION23 |
| CAG_INFORMATION24 | VARCHAR2 | 150 |  |  | CAG_INFORMATION24 |
| CAG_INFORMATION25 | VARCHAR2 | 150 |  |  | CAG_INFORMATION25 |
| CAG_INFORMATION26 | VARCHAR2 | 150 |  |  | CAG_INFORMATION26 |
| CAG_INFORMATION27 | VARCHAR2 | 150 |  |  | CAG_INFORMATION27 |
| CAG_INFORMATION28 | VARCHAR2 | 150 |  |  | CAG_INFORMATION28 |
| CAG_INFORMATION29 | VARCHAR2 | 150 |  |  | CAG_INFORMATION29 |
| CAG_INFORMATION30 | VARCHAR2 | 150 |  |  | CAG_INFORMATION30 |
| CAG_INFORMATION_NUMBER1 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER1 |
| CAG_INFORMATION_NUMBER2 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER2 |
| CAG_INFORMATION_NUMBER3 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER3 |
| CAG_INFORMATION_NUMBER4 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER4 |
| CAG_INFORMATION_NUMBER5 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER5 |
| CAG_INFORMATION_NUMBER6 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER6 |
| CAG_INFORMATION_NUMBER7 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER7 |
| CAG_INFORMATION_NUMBER8 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER8 |
| CAG_INFORMATION_NUMBER9 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER9 |
| CAG_INFORMATION_NUMBER10 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER10 |
| CAG_INFORMATION_NUMBER11 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER11 |
| CAG_INFORMATION_NUMBER12 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER12 |
| CAG_INFORMATION_NUMBER13 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER13 |
| CAG_INFORMATION_NUMBER14 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER14 |
| CAG_INFORMATION_NUMBER15 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER15 |
| CAG_INFORMATION_NUMBER16 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER16 |
| CAG_INFORMATION_NUMBER17 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER17 |
| CAG_INFORMATION_NUMBER18 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER18 |
| CAG_INFORMATION_NUMBER19 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER19 |
| CAG_INFORMATION_NUMBER20 | NUMBER |  |  |  | CAG_INFORMATION_NUMBER20 |
| CAG_INFORMATION_DATE1 | DATE |  |  |  | CAG_INFORMATION_DATE1 |
| CAG_INFORMATION_DATE2 | DATE |  |  |  | CAG_INFORMATION_DATE2 |
| CAG_INFORMATION_DATE3 | DATE |  |  |  | CAG_INFORMATION_DATE3 |
| CAG_INFORMATION_DATE4 | DATE |  |  |  | CAG_INFORMATION_DATE4 |
| CAG_INFORMATION_DATE5 | DATE |  |  |  | CAG_INFORMATION_DATE5 |
| CAG_INFORMATION_DATE6 | DATE |  |  |  | CAG_INFORMATION_DATE6 |
| CAG_INFORMATION_DATE7 | DATE |  |  |  | CAG_INFORMATION_DATE7 |
| CAG_INFORMATION_DATE8 | DATE |  |  |  | CAG_INFORMATION_DATE8 |
| CAG_INFORMATION_DATE9 | DATE |  |  |  | CAG_INFORMATION_DATE9 |
| CAG_INFORMATION_DATE10 | DATE |  |  |  | CAG_INFORMATION_DATE10 |
| CAG_INFORMATION_DATE11 | DATE |  |  |  | CAG_INFORMATION_DATE11 |
| CAG_INFORMATION_DATE12 | DATE |  |  |  | CAG_INFORMATION_DATE12 |
| CAG_INFORMATION_DATE13 | DATE |  |  |  | CAG_INFORMATION_DATE13 |
| CAG_INFORMATION_DATE14 | DATE |  |  |  | CAG_INFORMATION_DATE14 |
| CAG_INFORMATION_DATE15 | DATE |  |  |  | CAG_INFORMATION_DATE15 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_COL_AGREEMENTS_F_FK1 | Non Unique | FUSION_TS_TX_IDX | BUSINESS_GROUP_ID |
| PER_COL_AGREEMENTS_F_FK2 | Non Unique | FUSION_TS_TX_IDX | LEGISLATION_CODE |
| PER_COL_AGREEMENTS_F_PK | Unique | FUSION_TS_TX_IDX | COLLECTIVE_AGREEMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
