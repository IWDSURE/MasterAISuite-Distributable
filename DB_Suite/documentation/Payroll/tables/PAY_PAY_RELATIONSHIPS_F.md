# PAY_PAY_RELATIONSHIPS_F

PAY_PAYROLL_RELATIONSHIPS_F is used to store date effective information for Payroll Relationship. The Payroll Relationship is the main entity for processing people in the Payroll Application.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrelationshipsf-8331.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrelationshipsf-8331.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAY_RELATIONSHIPS_F_PK | PAYROLL_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | PAYROLL_RELATIONSHIP_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| ELEMENT_CRITERIA_ID | NUMBER |  | 18 | Yes | ELEMENT_CRITERIA_ID |  |
| OVERRIDING_PERIOD_ID | NUMBER |  | 18 |  | OVERRIDING_PERIOD_ID |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| REL_INFORMATION_TYPE | VARCHAR2 | 150 |  |  | REL_INFORMATION_TYPE | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| REL_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Pay Relationship Information (PAY_PAY_RELATIONSHIPS_DDF) |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PAY_RELATIONSHIPS_F_N1 | Non Unique | Default | ELEMENT_CRITERIA_ID |
| PAY_PAY_RELATIONSHIPS_F_PK | Unique | Default | PAYROLL_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
