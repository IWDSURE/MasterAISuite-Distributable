# PAY_TIME_PERIODS

This table contains the payroll calendar used as the basis for regular payroll processing.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimeperiods-10947.html#paytimeperiods-10947](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimeperiods-10947.html#paytimeperiods-10947)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TIME_PERIODS_PK | TIME_PERIOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| TIME_PERIOD_ID | NUMBER |  | 18 | Yes | TIME_PERIOD_ID |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |  |
| END_DATE | DATE |  |  |  | END_DATE |  |
| PERIOD_NAME | VARCHAR2 | 70 |  |  | PERIOD_NAME |  |
| PERIOD_NUM | NUMBER |  | 18 |  | PERIOD_NUM |  |
| PERIOD_TYPE | VARCHAR2 | 30 |  |  | PERIOD_TYPE |  |
| START_DATE | DATE |  |  |  | START_DATE |  |
| CUT_OFF_DATE | DATE |  |  |  | CUT_OFF_DATE |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |  |
| PERIOD_SET_NAME | VARCHAR2 | 30 |  |  | PERIOD_SET_NAME |  |
| PERIOD_YEAR | NUMBER |  | 18 |  | PERIOD_YEAR |  |
| PROC_PERIOD_TYPE | VARCHAR2 | 30 |  |  | PROC_PERIOD_TYPE |  |
| QUARTER_NUM | NUMBER |  | 18 |  | QUARTER_NUM |  |
| QUICKPAY_DISPLAY_NUMBER | NUMBER |  | 9 |  | QUICKPAY_DISPLAY_NUMBER |  |
| RUN_DISPLAY_NUMBER | NUMBER |  | 9 |  | RUN_DISPLAY_NUMBER |  |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |  |
| DEFAULT_PAYDATE | DATE |  |  |  | DEFAULT_PAYDATE |  |
| REGULAR_PROCESS_DATE | DATE |  |  |  | REGULAR_PROCESS_DATE |  |
| PROCESS_SUB_DATE | DATE |  |  |  | PROCESS_SUB_DATE |  |
| REGULAR_EARN_DATE | DATE |  |  |  | REGULAR_EARN_DATE |  |
| YEAR_NUMBER | NUMBER |  | 18 |  | YEAR_NUMBER |  |
| PERIOD_CATEGORY | VARCHAR2 | 30 |  |  | This is used to identify whether the period is an Earning or Deduction/Statutory Period |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Time Period Attributes (PAY_TIME_PERIODS_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| PRD_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | PRD_INFORMATION_CATEGORY | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| PRD_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Time Period Information (PAY_TIME_PERIODS_DDF) |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| PAYSLIP_VIEW_DATE | DATE |  |  |  | PAYSLIP_VIEW_DATE |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TIME_PERIODS_N1 | Non Unique | Default | PAYROLL_ID, END_DATE, START_DATE, PERIOD_CATEGORY |
| PAY_TIME_PERIODS_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PAY_TIME_PERIODS_N3 | Non Unique | Default | TIME_DEFINITION_ID, START_DATE, END_DATE |
| PAY_TIME_PERIODS_N4 | Non Unique | Default | PERIOD_NAME |
| PAY_TIME_PERIODS_PK | Unique | Default | TIME_PERIOD_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
