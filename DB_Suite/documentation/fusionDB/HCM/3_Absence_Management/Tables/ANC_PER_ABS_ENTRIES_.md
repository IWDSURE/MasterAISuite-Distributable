# ANC_PER_ABS_ENTRIES_

This table holds information of the person absence entry.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentries-9852.html#ancperabsentries-9852](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentries-9852.html#ancperabsentries-9852)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_ENTRIES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PER_ABSENCE_ENTRY_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ABS_RECORD_SOURCE | VARCHAR2 | 60 |  |  | Represents the source of absence from where absence is recorded |
| ASSIGNMENT_STATUS_UPDATE | VARCHAR2 | 30 |  |  | ASSIGNMENT_STATUS_UPDATE |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_ENTRY_ID |
| PER_ABSENCE_HEADER_ID | NUMBER |  | 18 |  | This columns foreign Key value from absence header table. |
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 |  | PERIOD_OF_SERVICE_ID |
| PAYROLL_CHG_FLAG | VARCHAR2 | 20 |  |  | PAYROLL_CHG_FLAG |
| ABSENCE_CASE_ID | NUMBER |  | 18 |  | References HR Absence Case Identifier |
| SINGLE_DAY_FLAG | VARCHAR2 | 1 |  |  | SINGLE_DAY_FLAG |
| START_DATE_DURATION | NUMBER |  |  |  | START_DATE_DURATION |
| END_DATE_DURATION | NUMBER |  |  |  | END_DATE_DURATION |
| ABSENCE_PATTERN_CD | VARCHAR2 | 30 |  |  | ABSENCE_PATTERN_CD |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ABSENCE_TYPE_ID | NUMBER |  | 18 |  | ABSENCE_TYPE |
| CHILD_EVENT_TYPE_CD | VARCHAR2 | 30 |  |  | Child event type code for Maternity |
| ABSENCE_TYPE_REASON_ID | NUMBER |  | 18 |  | ABSENCE_REASON |
| ABSENCE_ENTRY_BASIC_FLAG | VARCHAR2 | 30 |  |  | ABSENCE_PATTERN |
| ABSENCE_STATUS_CD | VARCHAR2 | 30 |  |  | ABSENCE_STATUS_CD |
| APPROVAL_STATUS_CD | VARCHAR2 | 30 |  |  | APPROVAL_STATUS_CD |
| APPROVAL_DATETIME | TIMESTAMP |  |  |  | APPROVAL_DATETIME |
| START_DATE | DATE |  |  |  | START_DATE |
| START_DATETIME | TIMESTAMP |  |  |  | START_DATETIME |
| SUBMITTED_DATETIME | TIMESTAMP |  |  |  | Absence or Bid submission date with timestamp |
| END_DATETIME | TIMESTAMP |  |  |  | END_DATETIME |
| END_DATE | DATE |  |  |  | END_DATE |
| START_TIME | VARCHAR2 | 30 |  |  | START_TIME |
| END_TIME | VARCHAR2 | 30 |  |  | END_TIME |
| PLANNED_END_DATE | DATE |  |  |  | PLANED_END_DATE |
| OPEN_ENDED_FLAG | VARCHAR2 | 1 |  |  | OPEN_ENDED_FLAG |
| CONFIRMED_DATE | DATE |  |  |  | CONFIRMED_DATE |
| SUBMITTED_DATE | DATE |  |  |  | Absence submission date |
| CONDITION_START_DATE | DATE |  |  |  | CONDITION_START_DATE |
| DURATION | NUMBER |  |  |  | DURATION |
| UOM | VARCHAR2 | 30 |  |  | UOM |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | PROCESSING_STATUS |
| AGREEMENT_ID | NUMBER |  | 18 |  | AGREEMENT_ID |
| BAND_DTL_ID | NUMBER |  | 18 |  | BAND_DTL_ID |
| CONSUMED_BY_AGREEMENT | VARCHAR2 | 30 |  |  | CONSUMED_BY_AGREEMENT |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| PROJECT_ID | NUMBER |  | 18 |  | PROJECT_ID |
| EMPLOYEE_SHIFT_FLAG | VARCHAR2 | 20 |  |  | EMPLOYEE_SHIFT_FLAG |
| TIME_CARD_TRANSFER_STATUS | VARCHAR2 | 80 |  |  | This column tracks the transfer status of integration with Time based on Shift breakdown data at Absence level |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | INFORMATION_CATEGORY |
| INFORMATION1 | VARCHAR2 | 150 |  |  | INFORMATION1 |
| INFORMATION2 | VARCHAR2 | 150 |  |  | INFORMATION2 |
| INFORMATION3 | VARCHAR2 | 150 |  |  | INFORMATION3 |
| INFORMATION4 | VARCHAR2 | 150 |  |  | INFORMATION4 |
| INFORMATION5 | VARCHAR2 | 150 |  |  | INFORMATION5 |
| INFORMATION6 | VARCHAR2 | 150 |  |  | INFORMATION6 |
| INFORMATION7 | VARCHAR2 | 150 |  |  | INFORMATION7 |
| INFORMATION8 | VARCHAR2 | 150 |  |  | INFORMATION8 |
| INFORMATION9 | VARCHAR2 | 150 |  |  | INFORMATION9 |
| INFORMATION10 | VARCHAR2 | 150 |  |  | INFORMATION10 |
| INFORMATION11 | VARCHAR2 | 150 |  |  | INFORMATION11 |
| INFORMATION12 | VARCHAR2 | 150 |  |  | INFORMATION12 |
| INFORMATION13 | VARCHAR2 | 150 |  |  | INFORMATION13 |
| INFORMATION14 | VARCHAR2 | 150 |  |  | INFORMATION14 |
| INFORMATION15 | VARCHAR2 | 150 |  |  | INFORMATION15 |
| INFORMATION16 | VARCHAR2 | 150 |  |  | INFORMATION16 |
| INFORMATION17 | VARCHAR2 | 150 |  |  | INFORMATION17 |
| INFORMATION18 | VARCHAR2 | 150 |  |  | INFORMATION18 |
| INFORMATION19 | VARCHAR2 | 150 |  |  | INFORMATION19 |
| INFORMATION20 | VARCHAR2 | 150 |  |  | INFORMATION20 |
| INFORMATION21 | VARCHAR2 | 150 |  |  | INFORMATION21 |
| INFORMATION22 | VARCHAR2 | 150 |  |  | INFORMATION22 |
| INFORMATION23 | VARCHAR2 | 150 |  |  | INFORMATION23 |
| INFORMATION24 | VARCHAR2 | 150 |  |  | INFORMATION24 |
| INFORMATION25 | VARCHAR2 | 150 |  |  | INFORMATION25 |
| INFORMATION26 | VARCHAR2 | 150 |  |  | INFORMATION26 |
| INFORMATION27 | VARCHAR2 | 150 |  |  | INFORMATION27 |
| INFORMATION28 | VARCHAR2 | 150 |  |  | INFORMATION28 |
| INFORMATION29 | VARCHAR2 | 150 |  |  | INFORMATION29 |
| INFORMATION30 | VARCHAR2 | 150 |  |  | INFORMATION30 |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | INFORMATION_NUMBER1 |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | INFORMATION_NUMBER2 |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | INFORMATION_NUMBER3 |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | INFORMATION_NUMBER4 |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | INFORMATION_NUMBER5 |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | INFORMATION_NUMBER6 |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | INFORMATION_NUMBER7 |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | INFORMATION_NUMBER8 |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | INFORMATION_NUMBER9 |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | INFORMATION_NUMBER10 |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | INFORMATION_NUMBER11 |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | INFORMATION_NUMBER12 |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | INFORMATION_NUMBER13 |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | INFORMATION_NUMBER14 |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | INFORMATION_NUMBER15 |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | INFORMATION_NUMBER16 |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | INFORMATION_NUMBER17 |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | INFORMATION_NUMBER18 |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | INFORMATION_NUMBER19 |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | INFORMATION_NUMBER20 |
| INFORMATION_DATE1 | DATE |  |  |  | INFORMATION_DATE1 |
| INFORMATION_DATE2 | DATE |  |  |  | INFORMATION_DATE2 |
| INFORMATION_DATE3 | DATE |  |  |  | INFORMATION_DATE3 |
| INFORMATION_DATE4 | DATE |  |  |  | INFORMATION_DATE4 |
| INFORMATION_DATE5 | DATE |  |  |  | INFORMATION_DATE5 |
| INFORMATION_DATE6 | DATE |  |  |  | INFORMATION_DATE6 |
| INFORMATION_DATE7 | DATE |  |  |  | INFORMATION_DATE7 |
| INFORMATION_DATE8 | DATE |  |  |  | INFORMATION_DATE8 |
| INFORMATION_DATE9 | DATE |  |  |  | INFORMATION_DATE9 |
| INFORMATION_DATE10 | DATE |  |  |  | INFORMATION_DATE10 |
| INFORMATION_DATE11 | DATE |  |  |  | INFORMATION_DATE11 |
| INFORMATION_DATE12 | DATE |  |  |  | INFORMATION_DATE12 |
| INFORMATION_DATE13 | DATE |  |  |  | INFORMATION_DATE13 |
| INFORMATION_DATE14 | DATE |  |  |  | INFORMATION_DATE14 |
| INFORMATION_DATE15 | DATE |  |  |  | INFORMATION_DATE15 |
| SPL_CONDITION | VARCHAR2 | 1000 |  |  | Special Condition |
| INITIAL_REPORT_BY_ID | NUMBER |  | 18 |  | INITIAL_REPORT_BY_ID |
| NOTIFICATION_DATE | DATE |  |  |  | Notification date |
| LATE_NOTIFY_FLAG | VARCHAR2 | 30 |  |  | Late |
| INITIAL_TIMELY_NOTIFY_FLAG | VARCHAR2 | 30 |  |  | Initial Notification timely |
| CERTIFICATION_AUTH_FLAG | VARCHAR2 | 30 |  |  | Authorization |
| AUTH_STATUS_UPDATE_DATE | DATE |  |  |  | Authorization Status Updated |
| TIMELINESS_OVERRIDE_DATE | DATE |  |  |  | Timeliness Override Date |
| DISEASE_CODE | VARCHAR2 | 250 |  |  | Disease Code |
| PERIOD_OF_INCAP_TO_WORK_FLAG | VARCHAR2 | 30 |  |  | Period Of Incapacity to Work |
| ESTABLISHMENT_DATE | DATE |  |  |  | Establishemnt Date |
| USER_MODE | VARCHAR2 | 10 |  |  | Represents user interface absence is entered. User mode values are EMP, MGR, ADMIN, APPROVAL. |
| SOURCE | VARCHAR2 | 10 |  |  | Represents the source of absence. Values are 'ANC', 'TC', 'XLS'. |
| FREQUENCY | VARCHAR2 | 30 |  |  | FREQUENCY |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| BLOCKED_LEAVE_CANDIDATE | VARCHAR2 | 30 |  |  | BLOCKED_LEAVE_CANDIDATE |
| OVERRIDDEN | VARCHAR2 | 10 |  |  | When absence record timing are not in the scheduled timings , this flag will set  to Yes. |
| APPROVAL_OUTCOME | VARCHAR2 | 30 |  |  | Approval Outcome |
| ESS_DURATION_UPDATE | VARCHAR2 | 10 |  |  | When absence duration is updated by ESS Evaluate Absences process, value will be set to Y |
| EXPEDITE | VARCHAR2 | 150 |  |  | Determines if payroll processing is to be expedited |
| OVERRIDE_PAY_METHOD | NUMBER |  |  |  | Payment method override for expedited payroll processing |
| OVERRIDE_CHECK_PRINTER | VARCHAR2 | 150 |  |  | Check printer localtion for expedited payroll processing |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| LAST_ENTRY_MODE | VARCHAR2 | 20 |  |  | Last Entry Mode |
| PAYROLL_MAPPING_ID | NUMBER |  | 18 |  | To store payroll mapping id |
| PAYROLL_STATUS | VARCHAR2 | 32 |  |  | To store the payroll transfer/integration status |
| BID_PREFERENCE | NUMBER |  |  |  | To identify the bid preference. |
| BID_FLAG | VARCHAR2 | 30 |  |  | To differentiate between Absence & Bid |
| BID_ID | NUMBER |  | 18 |  | Key to the BIDs created. |
| START_DT_DUR_PREF_CD | VARCHAR2 | 30 |  |  | Start date duration preference code for elapsed shift and UOM days. |
| END_DT_DUR_PREF_CD | VARCHAR2 | 30 |  |  | End date duration preference code for elapsed shift and UOM days. |
| UNPAID_BREAK_DURATION | NUMBER |  |  |  | UNPAID_BREAK_DURATION |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_ENTRIESN1_ | Non Unique | Default | PER_ABSENCE_ENTRY_ID, ENTERPRISE_ID |
| ANC_PER_ABS_ENTRIES_UK1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PER_ABSENCE_ENTRY_ID, ENTERPRISE_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
