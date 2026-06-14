# PAY_ASSIGNED_PAYROLLS_F_

Stores details of which payrolls an employee is assigned to at a point in time. This allows an employee to transition payrolls even when their periods overlap

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payassignedpayrollsf-23002.html#payassignedpayrollsf-23002](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payassignedpayrollsf-23002.html#payassignedpayrollsf-23002)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ASSIGNED_PAYROLLS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNED_PAYROLL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNED_PAYROLL_ID | NUMBER |  | 18 | Yes | ASSIGNED_PAYROLL_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ELEMENT_CRITERIA_ID | NUMBER |  | 18 |  | ELEMENT_CRITERIA_ID |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | PRIMARY_FLAG |
| TIME_CARD_REQ | VARCHAR2 | 20 |  |  | TIME_CARD_REQ |
| OVERRIDING_PERIOD_ID | NUMBER |  | 18 |  | OVERRIDING_PERIOD |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| ASG_INFORMATION_TYPE | VARCHAR2 | 150 |  |  | ASG_INFORMATION_TYPE |
| ASG_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| ASG_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ASSIGNED_PAYROLLS_FN1_ | Non Unique | Default | ASSIGNED_PAYROLL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_ASSIGNED_PAYROLLS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASSIGNED_PAYROLL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
