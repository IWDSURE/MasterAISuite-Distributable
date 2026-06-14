# CMP_MKT_SURVEY_DATA_COPY

Contains backup of Market Survey Imported Data

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsurveydatacopy-16080.html#cmpmktsurveydatacopy-16080](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsurveydatacopy-16080.html#cmpmktsurveydatacopy-16080)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_SURVEY_DATA_COPY_PK | SURVEY_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_DATA_ID | NUMBER |  | 18 | Yes | Primary Key |
| BATCH_ID | NUMBER |  | 18 |  | Batch Id |
| VENDOR_ID | NUMBER |  | 18 | Yes | Vendor Id |
| COMP_TYPE_ID | NUMBER |  | 18 | Yes | Comp Type Id |
| JOB_LIST_ID | NUMBER |  | 18 | Yes | Job List Id |
| COUNTRY_CODE | VARCHAR2 | 30 |  |  | Country Code |
| VENDOR_LOCATION_ID | NUMBER |  | 18 |  | Vendor Location Id |
| VENDOR_LOCATION | VARCHAR2 | 300 |  |  | Vendor Location until we implement Location Table |
| INDUSTRY | VARCHAR2 | 300 |  |  | Industry |
| OTHER_GROUP | VARCHAR2 | 300 |  |  | Other Group |
| TEN_PERCENT | NUMBER |  |  |  | 10% |
| TWENTY_FIVE_PERCENT | NUMBER |  |  |  | 25% |
| FIFTY_PERCENT | NUMBER |  |  |  | 50% |
| SEVENTY_FIVE_PERCENT | NUMBER |  |  |  | 75% |
| NINTY_PERCENT | NUMBER |  |  |  | 90% |
| AVERAGE_MEAN | NUMBER |  |  |  | Average Mean |
| CURRENCY | VARCHAR2 | 30 |  |  | Currency |
| PARTICIPATING_COMPANIES | NUMBER |  |  |  | Participating Companies |
| PARTICIPATING_INCUMBANTS | NUMBER |  |  |  | Participating Incumbants |
| MISC_NUMBER_1_DATA | NUMBER |  |  |  | Number 1 data |
| MISC_NUMBER_2_DATA | NUMBER |  |  |  | Number 2 data |
| MISC_NUMBER_3_DATA | NUMBER |  |  |  | Number 3 data |
| MISC_NUMBER_4_DATA | NUMBER |  |  |  | Number 4 data |
| MISC_TEXT_1_DATA | VARCHAR2 | 300 |  |  | Text 1 data |
| MISC_TEXT_2_DATA | VARCHAR2 | 300 |  |  | Text 2 data |
| MISC_TEXT_3_DATA | VARCHAR2 | 300 |  |  | Text 3 data |
| ADJUSTMENT_COMMENT | VARCHAR2 | 300 |  |  | User comment for adjustment operation |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| ADJUSTMENT_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last survey data adjustment of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TWENTY_PERCENT | NUMBER |  |  |  | 20% |
| THIRTY_PERCENT | NUMBER |  |  |  | 30% |
| FORTY_PERCENT | NUMBER |  |  |  | 40% |
| SIXTY_PERCENT | NUMBER |  |  |  | 60% |
| SEVENTY_PERCENT | NUMBER |  |  |  | 70% |
| EIGHTY_PERCENT | NUMBER |  |  |  | 80% |
| ONE_HUNDRED_PERCENT | NUMBER |  |  |  | 100% |
| INCLUSION_FACTOR | NUMBER |  |  |  | Inclusion factor |
| BATCH_NAME | VARCHAR2 | 200 |  |  | Name of the batch. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_SURVEY_DATA_COPY_U1 | Unique | Default | SURVEY_DATA_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
