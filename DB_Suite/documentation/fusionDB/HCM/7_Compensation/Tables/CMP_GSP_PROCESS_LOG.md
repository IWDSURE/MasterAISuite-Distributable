# CMP_GSP_PROCESS_LOG

CMP_GSP_PROCESS_LOG  table holds logging done in the pkg files gor gsp.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgspprocesslog-31550.html#cmpgspprocesslog-31550](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpgspprocesslog-31550.html#cmpgspprocesslog-31550)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_GSP_PROCESS_LOG_PK | GSP_TXN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GSP_TXN_ID | NUMBER |  | 18 | Yes | GSP_TXN_ID |
| TRANSACTION_TYPE | VARCHAR2 | 30 |  |  | TRANSACTION_TYPE |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| GRADE_LADDER_ID | NUMBER |  | 18 |  | GRADE_LADDER_ID |
| GRADE_ID | NUMBER |  | 18 |  | GRADE_ID |
| GRADE_STEP_ID | NUMBER |  | 18 |  | GRADE_STEP_ID |
| RATE_ID | NUMBER |  | 18 |  | RATE_ID |
| RATE_VALUE_ID | NUMBER |  | 18 |  | RATE_VALUE_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| SALARY_BASIS_ID | NUMBER |  | 18 |  | SALARY_BASIS_ID |
| FTE | NUMBER |  | 18 |  | FTE |
| CURRENT_SALARY | NUMBER |  | 18 |  | CURRENT_SALARY |
| PROPOSED_SALARY | NUMBER |  | 18 |  | PROPOSED_SALARY |
| SALARY_ID | NUMBER |  | 18 |  | SALARY_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| EFFECTIVE_DATE | TIMESTAMP |  |  |  | EFFECTIVE_DATE |
| MESSAGE_NAME | VARCHAR2 | 240 |  |  | MESSAGE_NAME |
| MESSAGE_TEXT | VARCHAR2 | 2000 |  |  | MESSAGE_TEXT |
| INFORMATION1 | VARCHAR2 | 240 |  |  | INFORMATION1 |
| INFORMATION2 | VARCHAR2 | 240 |  |  | INFORMATION2 |
| INFORMATION3 | VARCHAR2 | 240 |  |  | INFORMATION3 |
| INFORMATION4 | VARCHAR2 | 240 |  |  | INFORMATION4 |
| INFORMATION5 | VARCHAR2 | 240 |  |  | INFORMATION5 |
| INFORMATION6 | VARCHAR2 | 240 |  |  | INFORMATION6 |
| INFORMATION7 | VARCHAR2 | 240 |  |  | INFORMATION7 |
| INFORMATION8 | VARCHAR2 | 240 |  |  | INFORMATION8 |
| INFORMATION9 | VARCHAR2 | 240 |  |  | INFORMATION9 |
| INFORMATION10 | VARCHAR2 | 240 |  |  | INFORMATION10 |
| INFORMATION11 | VARCHAR2 | 240 |  |  | INFORMATION11 |
| INFORMATION12 | VARCHAR2 | 240 |  |  | INFORMATION12 |
| INFORMATION13 | VARCHAR2 | 240 |  |  | INFORMATION13 |
| INFORMATION14 | VARCHAR2 | 240 |  |  | INFORMATION14 |
| INFORMATION15 | VARCHAR2 | 240 |  |  | INFORMATION15 |
| INFORMATION16 | VARCHAR2 | 240 |  |  | INFORMATION16 |
| INFORMATION17 | VARCHAR2 | 240 |  |  | INFORMATION17 |
| INFORMATION18 | VARCHAR2 | 240 |  |  | INFORMATION18 |
| INFORMATION19 | VARCHAR2 | 240 |  |  | INFORMATION19 |
| INFORMATION20 | VARCHAR2 | 240 |  |  | INFORMATION20 |
| INFORMATION21 | VARCHAR2 | 240 |  |  | INFORMATION21 |
| INFORMATION22 | VARCHAR2 | 240 |  |  | INFORMATION22 |
| INFORMATION23 | VARCHAR2 | 240 |  |  | INFORMATION23 |
| INFORMATION24 | VARCHAR2 | 240 |  |  | INFORMATION24 |
| INFORMATION25 | VARCHAR2 | 240 |  |  | INFORMATION25 |
| INFORMATION26 | VARCHAR2 | 240 |  |  | INFORMATION26 |
| INFORMATION27 | VARCHAR2 | 240 |  |  | INFORMATION27 |
| INFORMATION28 | VARCHAR2 | 240 |  |  | INFORMATION28 |
| INFORMATION29 | VARCHAR2 | 240 |  |  | INFORMATION29 |
| INFORMATION30 | VARCHAR2 | 2000 |  |  | INFORMATION30 |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_GSP_PROCESS_LOG_U1 | Unique | Default | GSP_TXN_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
