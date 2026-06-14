# PAY_ALL_PAYROLLS_F

This table contains definitions of groups of workers who share the same frequency of processing and payment. It defines the default processing information for consolidation groups, payment types, cost allocation, and date offsets..

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payallpayrollsf-30314.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payallpayrollsf-30314.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAYROLLS_F_PK | PAYROLL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PAYROLL_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |  |
| PROCESS_SUB_DATE_OFFSET | NUMBER |  | 5 |  | Number of days payroll submission date for entries is offset from end of period. |  |
| PROCESS_SUB_WRT | VARCHAR2 | 1 |  |  | PROCESS_SUB_WRT |  |
| PROCESS_SUB_BASE_DATE | VARCHAR2 | 1 |  |  | PROCESS_SUB_BASE_DATE |  |
| PROCESS_SUB_FALLS | NUMBER |  | 2 |  | PROCESS_SUB_FALLS |  |
| PROCESS_SUB_OFFSET | VARCHAR2 | 1 |  |  | PROCESS_SUB_OFFSET |  |
| PROCESS_SUB_FIXED_DATE | DATE |  |  |  | PROCESS_SUB_FIXED_DATE |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| REPORTING_NAME | VARCHAR2 | 80 |  |  | REPORTING_NAME |  |
| PAYROLL_NAME | VARCHAR2 | 80 |  | Yes | User name for this payroll. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| CONSOLIDATION_SET_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_CONSOLIDATION_SETS. |  |
| GL_SET_OF_BOOKS_ID | NUMBER |  | 18 |  | Foreign key to GL_SETS_OF_BOOKS. |  |
| PERIOD_TYPE | VARCHAR2 | 30 |  | Yes | Foreign key to PER_TIME_PERIOD_TYPES. |  |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |  |
| FIRST_PERIOD_END_DATE | DATE |  |  | Yes | End date of the first processing period.  Used to generate first and all successive pay period dates for this payroll. |  |
| NUMBER_OF_YEARS | NUMBER |  | 5 | Yes | Number of years of pay periods to generate. |  |
| PERIOD_RESET_YEARS | NUMBER |  | 9 |  | Number of Years after which the payroll periods would be reset. Used for Lunar Month Period Types. |  |
| CUT_OFF_DATE_OFFSET | NUMBER |  | 5 |  | Number of days cut-off date for entries is offset from end of period. |  |
| REGULAR_EARN_DATE_OFFSET | NUMBER |  | 5 |  | REGULAR_EARN_DATE_OFFSET |  |
| REGULAR_PROCESS_DATE_OFFSET | NUMBER |  | 5 |  | REGULAR_PROCESS_DATE_OFFSET |  |
| DEFAULT_PAYDATE_OFFSET | NUMBER |  | 5 |  | DEFAULT_PAYDATE_OFFSET |  |
| PAYSLIP_VIEW_DATE_OFFSET | NUMBER |  | 5 |  | Number of days after payment date, on or after which, user can view his payslip |  |
| NEGATIVE_PAY_ALLOWED_FLAG | VARCHAR2 | 30 |  |  | Indicates whether negative payments are allowed. |  |
| DEFAULT_PAYMENT_METHOD_ID | NUMBER |  | 18 |  | Foreign key to PAY_ORG_PAYMENT_METHODS. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| BASE_OFFSETS | VARCHAR2 | 1 |  |  | BASE_OFFSETS |  |
| PAYMENTS_WRT | VARCHAR2 | 1 |  |  | PAYMENTS_WRT |  |
| PAYDATE_BASE_WRT | VARCHAR2 | 1 |  |  | PAYDATE_BASE_WRT |  |
| PAYSLIP_BASE_WRT | VARCHAR2 | 1 |  |  | PAYSLIP_BASE_WRT |  |
| CUTOFF_BASE_WRT | VARCHAR2 | 1 |  |  | CUTOFF_BASE_WRT |  |
| PROCESS_BASE_WRT | VARCHAR2 | 1 |  |  | PROCESS_BASE_WRT |  |
| EARN_BASE_WRT | VARCHAR2 | 1 |  |  | EARN_BASE_WRT |  |
| PAYSLIP_BASE_DATE | VARCHAR2 | 1 |  |  | PAYSLIP_BASE_DATE |  |
| CUTOFF_BASE_DATE | VARCHAR2 | 1 |  |  | CUTOFF_BASE_DATE |  |
| PROCESS_BASE_DATE | VARCHAR2 | 1 |  |  | PROCESS_BASE_DATE |  |
| EARN_BASE_DATE | VARCHAR2 | 1 |  |  | EARN_BASE_DATE |  |
| PAYDATE_BASE_DATE | VARCHAR2 | 1 |  |  | PAYDATE_BASE_DATE |  |
| PROCESS_FALLS | NUMBER |  | 2 |  | PROCESS_FALLS |  |
| EARN_FALLS | NUMBER |  | 2 |  | EARN_FALLS |  |
| PAYDATE_FALLS | NUMBER |  | 2 |  | PAYDATE_FALLS |  |
| PAYSLIP_FALLS | NUMBER |  | 2 |  | PAYSLIP_FALLS |  |
| CUTOFF_FALLS | NUMBER |  | 2 |  | CUTOFF_FALLS |  |
| PAYSLIP_OFFSET | VARCHAR2 | 1 |  |  | PAYSLIP_OFFSET |  |
| EARN_OFFSET | VARCHAR2 | 1 |  |  | EARN_OFFSET |  |
| PROCESS_OFFSET | VARCHAR2 | 1 |  |  | PROCESS_OFFSET |  |
| CUTOFF_OFFSET | VARCHAR2 | 1 |  |  | CUTOFF_OFFSET |  |
| PAYDATE_OFFSET | VARCHAR2 | 1 |  |  | PAYDATE_OFFSET |  |
| FIXED_DATE | VARCHAR2 | 1 |  |  | FIXED_DATE |  |
| PAYSLIP_FIXED_DATE | DATE |  |  |  | PAYSLIP_FIXED_DATE |  |
| CUTOFF_FIXED_DATE | DATE |  |  |  | CUTOFF_FIXED_DATE |  |
| PROCESS_FIXED_DATE | DATE |  |  |  | PROCESS_FIXED_DATE |  |
| EARN_FIXED_DATE | DATE |  |  |  | EARN_FIXED_DATE |  |
| PAYDATE_FIXED_DATE | DATE |  |  |  | PAYDATE_FIXED_DATE |  |
| PRL_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer descriptive flexfield structure definition column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer descriptive flexfield column. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |
| PRL_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Payroll Developer DF (Payroll Developer DF) |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ALL_PAYROLLS_F_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_ALL_PAYROLLS_F_N2 | Non Unique | Default | PAYROLL_NAME |
| PAY_ALL_PAYROLLS_F_PK | Unique | Default | PAYROLL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
