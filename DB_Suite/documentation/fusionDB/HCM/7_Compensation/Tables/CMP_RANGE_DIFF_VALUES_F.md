# CMP_RANGE_DIFF_VALUES_F

Stores the Differential values for a Differential profile that vary by location or job or business unit.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmprangediffvaluesf-23180.html#cmprangediffvaluesf-23180](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmprangediffvaluesf-23180.html#cmprangediffvaluesf-23180)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_RANGE_DIFF_VALUES_F_PK | RANGE_DIFF_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANGE_DIFF_VALUE_ID | NUMBER |  | 18 | Yes | RANGE_DIFF_VALUE_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| RANGE_DIFF_ID | NUMBER |  | 18 | Yes | RANGE_DIFF_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | BUSINESS_UNIT_ID |
| DIFFERENTIAL | NUMBER |  |  |  | DIFFERENTIAL |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CRITERIA | VARCHAR2 | 30 |  |  | CRITERIA |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | ACTION_OCCURRENCE_ID |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |
| GEOGRAPHY_ID | NUMBER |  | 18 |  | GEOGRAPHY_ID |
| GRADE_RATE_ID | NUMBER |  | 18 |  | GRADE_RATE_ID |
| GRADE_RATE_MINIMUM_LIMIT | NUMBER |  |  |  | GRADE_RATE_MINIMUM_LIMIT |
| FREQUENCY | VARCHAR2 | 30 |  |  | FREQUENCY |
| ANNUALIZATION_FACTOR | NUMBER |  |  |  | ANNUALIZATION_FACTOR |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_RANGE_DIFF_VALUES_F_N1 | Non Unique | Default | RANGE_DIFF_ID |
| CMP_RANGE_DIFF_VALUES_F_N2 | Non Unique | Default | LOCATION_ID |
| CMP_RANGE_DIFF_VALUES_F_N3 | Non Unique | Default | JOB_ID |
| CMP_RANGE_DIFF_VALUES_F_N4 | Non Unique | Default | BUSINESS_UNIT_ID |
| CMP_RANGE_DIFF_VALUES_F_N5 | Non Unique | Default | CRITERIA |
| CMP_RANGE_DIFF_VALUES_F_PK | Unique | Default | RANGE_DIFF_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
