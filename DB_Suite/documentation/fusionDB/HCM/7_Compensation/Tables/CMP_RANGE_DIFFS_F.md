# CMP_RANGE_DIFFS_F

Stores the Salary Range Differential Profiles. Differential Profiles provide a way to define and manage salary ranges that vary by location or business unit or job.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmprangediffsf-16974.html#cmprangediffsf-16974](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmprangediffsf-16974.html#cmprangediffsf-16974)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_RANGE_DIFFS_F_PK | RANGE_DIFF_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANGE_DIFF_ID | NUMBER |  | 18 | Yes | RANGE_DIFF_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CODE | VARCHAR2 | 80 |  |  | CODE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| CRITERIA | VARCHAR2 | 30 |  |  | CRITERIA |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ACTION_ID | NUMBER |  | 18 |  | ACTION_ID |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | ACTION_OCCURRENCE_ID |
| ACTION_REASON_ID | NUMBER |  | 18 |  | ACTION_REASON_ID |
| RANGE_DIFF_TYPE | VARCHAR2 | 30 |  |  | RANGE_DIFF_TYPE |
| GEOGRAPHY_TYPE_ID | NUMBER |  | 18 |  | GEOGRAPHY_TYPE_ID |
| PROCESS_WFH_FLAG | VARCHAR2 | 1 |  |  | PROCESS_WFH_FLAG |
| ADDRESS_TYPE1 | VARCHAR2 | 30 |  |  | ADDRESS_TYPE1 |
| ADDRESS_TYPE2 | VARCHAR2 | 30 |  |  | ADDRESS_TYPE2 |
| ADDRESS_TYPE3 | VARCHAR2 | 30 |  |  | ADDRESS_TYPE3 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_RANGE_DIFFS_F_N1 | Non Unique | Default | CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| CMP_RANGE_DIFFS_F_N2 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| CMP_RANGE_DIFFS_F_N3 | Non Unique | Default | CRITERIA |
| CMP_RANGE_DIFFS_F_PK | Unique | Default | RANGE_DIFF_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
