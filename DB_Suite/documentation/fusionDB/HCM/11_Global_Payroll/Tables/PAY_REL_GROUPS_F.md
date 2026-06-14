# PAY_REL_GROUPS_F

Defines setup information for how payroll relationships behave within a legislation.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelgroupsf-12461.html#payrelgroupsf-12461](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelgroupsf-12461.html#payrelgroupsf-12461)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_REL_GROUPS_F_PK | RELATIONSHIP_GROUP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| RELATIONSHIP_GROUP_ID | NUMBER |  | 18 | Yes | RELATIONSHIP_GROUP_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| ELEMENT_CRITERIA_ID | NUMBER |  | 18 | Yes | ELEMENT_CRITERIA_ID |  |
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 |  | ASSIGNMENT_STATUS_TYPE_ID |  |
| TIME_CARD_REQ | VARCHAR2 | 20 |  |  | TIME_CARD_REQ |  |
| TRANSFER_TO_PROJ_FLAG | VARCHAR2 | 20 |  |  | TRANSFER_TO_PROJ_FLAG |  |
| OVERRIDING_PERIOD_ID | NUMBER |  | 18 |  | OVERRIDING_PERIOD_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| REL_INFORMATION_TYPE | VARCHAR2 | 150 |  |  | REL_INFORMATION_TYPE | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| REL_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Relationship Group Information (PAY_REL_GROUPS_DDF) |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_REL_GROUPS_F_N1 | Non Unique | Default | ELEMENT_CRITERIA_ID |
| PAY_REL_GROUPS_F_PK | Unique | Default | RELATIONSHIP_GROUP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
