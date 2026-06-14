# CMP_MKT_VND_SURVEYS_B

Contains a lot of Vendor Survey data

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndsurveysb-23496.html#cmpmktvndsurveysb-23496](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndsurveysb-23496.html#cmpmktvndsurveysb-23496)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_VND_SURVEYS_B_PK | MKT_SURVEY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MKT_SURVEY_ID | NUMBER |  | 18 | Yes | Primary Key |
| MKT_SURVEY_CODE | VARCHAR2 | 30 |  | Yes | Survey Code |
| VENDOR_ID | NUMBER |  | 18 | Yes | Foreign Key |
| STATUS | VARCHAR2 | 30 |  | Yes | Status |
| APPROX_NUM_COMPANIES | NUMBER |  |  |  | Number of Companies |
| SURVEY_FEE_PARTICIPANT | NUMBER |  |  |  | Fee |
| SURVEY_FEE_NON_ARTICIPANT | NUMBER |  |  |  | Non Fee |
| MISC_1 | VARCHAR2 | 300 |  |  | Miscelaneous 1 |
| MISC_2 | VARCHAR2 | 300 |  |  | Miscelaneous 2 |
| MISC_3 | VARCHAR2 | 300 |  |  | Miscelaneous |
| COUNTRY | VARCHAR2 | 1 |  |  | Country |
| LOCATION | VARCHAR2 | 1 |  |  | Location |
| INDUSTRY | VARCHAR2 | 1 |  |  | Industry |
| GROUPS | VARCHAR2 | 1 |  |  | Groups |
| TEN_PERCENT | VARCHAR2 | 1 |  |  | 10% |
| TWENTY_FIVE_PERCENT | VARCHAR2 | 1 |  |  | 25% |
| FIFTY_PERCENT | VARCHAR2 | 1 |  |  | 50% |
| SEVENTY_FIVE_PERCENT | VARCHAR2 | 1 |  |  | 75% |
| NINTY_PERCENT | VARCHAR2 | 1 |  |  | 90% |
| AVERAGE_MEAN | VARCHAR2 | 1 |  |  | Average Mean |
| CURRENCY | VARCHAR2 | 1 |  |  | Currency |
| PARTICIPATING_COMPANIES | VARCHAR2 | 1 |  |  | Participating Companies |
| PARTICIPATING_INCUMBANTS | VARCHAR2 | 1 |  |  | Participating Incumbants |
| MISC_NUMBER_1 | VARCHAR2 | 1 |  |  | Number 1 |
| MISC_NUMBER_1_DATA | NUMBER |  |  |  | Number 1 data |
| MISC_NUMBER_2 | VARCHAR2 | 1 |  |  | Number 2 |
| MISC_NUMBER_2_DATA | NUMBER |  |  |  | Number 2 data |
| MISC_NUMBER_3 | VARCHAR2 | 1 |  |  | Number 3 |
| MISC_NUMBER_3_DATA | NUMBER |  |  |  | Number 3 data |
| MISC_NUMBER_4 | VARCHAR2 | 1 |  |  | Number 4 |
| MISC_NUMBER_4_DATA | NUMBER |  |  |  | Number 4 data |
| MISC_TEXT_1 | VARCHAR2 | 1 |  |  | Text 1 |
| MISC_TEXT_1_DATA | VARCHAR2 | 300 |  |  | Text 1 data |
| MISC_TEXT_2 | VARCHAR2 | 1 |  |  | Text 2 |
| MISC_TEXT_2_DATA | VARCHAR2 | 300 |  |  | Text 2 data |
| MISC_TEXT_3 | VARCHAR2 | 1 |  |  | Text 3 |
| MISC_TEXT_3_DATA | VARCHAR2 | 300 |  |  | Text 3 data |
| PART_FEE_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Participant Fee Currency Code |
| NON_PART_FEE_CURRENCY_CODE | VARCHAR2 | 30 |  |  | Non Participant Fee Currency Code |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MISC_NUMBER_1_DATA2 | VARCHAR2 | 300 |  |  | Number 1 data |
| MISC_NUMBER_2_DATA2 | VARCHAR2 | 300 |  |  | Number 2 data |
| MISC_NUMBER_3_DATA2 | VARCHAR2 | 300 |  |  | Number 3 data |
| MISC_NUMBER_4_DATA2 | VARCHAR2 | 300 |  |  | Number 4 data |
| TWENTY_PERCENT | VARCHAR2 | 1 |  |  | 20% |
| THIRTY_PERCENT | VARCHAR2 | 1 |  |  | 30% |
| FORTY_PERCENT | VARCHAR2 | 1 |  |  | 40% |
| SIXTY_PERCENT | VARCHAR2 | 1 |  |  | 60% |
| SEVENTY_PERCENT | VARCHAR2 | 1 |  |  | 70% |
| EIGHTY_PERCENT | VARCHAR2 | 1 |  |  | 80% |
| ONE_HUNDRED_PERCENT | VARCHAR2 | 1 |  |  | 100% |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_VND_SURVEYS_B_U1 | Unique | Default | MKT_SURVEY_ID |
| CMP_MKT_VND_SURVEYS_B_U2 | Unique | Default | MKT_SURVEY_CODE, VENDOR_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
