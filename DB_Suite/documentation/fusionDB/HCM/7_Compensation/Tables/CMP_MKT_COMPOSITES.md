# CMP_MKT_COMPOSITES

Stores Market Survey Composite data in the database.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomposites-6659.html#cmpmktcomposites-6659](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcomposites-6659.html#cmpmktcomposites-6659)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_COMPOSITES_PK | COMPOSITE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPOSITE_ID | NUMBER |  | 18 | Yes | COMPOSITE_ID |
| COMPOSITE_MAPPING_CODE | VARCHAR2 | 30 |  |  | Indicates if the composite is mapped to internal HR Job or Position. |
| JOB_ID | NUMBER |  | 18 |  | Job List Id |
| POSITION_ID | NUMBER |  | 18 |  | HR Position Id |
| LOCATION_ID | NUMBER |  | 18 |  | Location Id |
| MARKET_SEGMENT_ID | NUMBER |  | 18 |  | MARKET_SEGMENT_ID |
| COUNTRY_CODE | VARCHAR2 | 30 |  | Yes | Country Code |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | Currency Code |
| COMP_TYPE_ID | NUMBER |  | 18 | Yes | Comp Type Id |
| TEN_PERCENT | NUMBER |  |  |  | 10% |
| START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| END_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| TWENTY_PERCENT | NUMBER |  |  |  | 20% |
| TWENTY_FIVE_PERCENT | NUMBER |  |  |  | 25% |
| THIRTY_PERCENT | NUMBER |  |  |  | 30% |
| FORTY_PERCENT | NUMBER |  |  |  | 40% |
| FIFTY_PERCENT | NUMBER |  |  |  | 50% |
| SIXTY_PERCENT | NUMBER |  |  |  | 60% |
| SEVENTY_PERCENT | NUMBER |  |  |  | 70% |
| SEVENTY_FIVE_PERCENT | NUMBER |  |  |  | 75% |
| EIGHTY_PERCENT | NUMBER |  |  |  | 80% |
| NINTY_PERCENT | NUMBER |  |  |  | 90% |
| ONE_HUNDRED_PERCENT | NUMBER |  |  |  | 100% |
| AVERAGE_MEAN | NUMBER |  |  |  | Average Mean |
| INDUSTRY | VARCHAR2 | 300 |  |  | Industry |
| OTHER_GROUP | VARCHAR2 | 300 |  |  | Other Group |
| MISC_NUMBER_1_DATA | NUMBER |  |  |  | Miscellaneous Number 1 |
| MISC_NUMBER_2_DATA | NUMBER |  |  |  | Miscellaneous Number 2 |
| MISC_NUMBER_3_DATA | NUMBER |  |  |  | Miscellaneous Number 3 |
| MISC_NUMBER_4_DATA | NUMBER |  |  |  | Miscellaneous Number 4 |
| MISC_TEXT_1_DATA | VARCHAR2 | 300 |  |  | Miscellaneous Text 1 |
| MISC_TEXT_2_DATA | VARCHAR2 | 300 |  |  | Miscellaneous Text 2 |
| MISC_TEXT_3_DATA | VARCHAR2 | 300 |  |  | Miscellaneous Text 3 |
| SOURCE_CODE | VARCHAR2 | 30 |  |  | Source Code |
| SOURCE_FACTOR | NUMBER |  |  |  | Source Factor |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_COMPOSITES_U1 | Unique | Default | COMPOSITE_ID |
| CMP_MKT_COMPOSITES_U2 | Unique | Default | COUNTRY_CODE, COMP_TYPE_ID, START_DATE, JOB_ID, POSITION_ID, LOCATION_ID, MARKET_SEGMENT_ID, CURRENCY_CODE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
