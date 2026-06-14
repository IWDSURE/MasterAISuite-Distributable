# BEN_GAP_DURATION_SUMMARY

This table is used to store absence details like Absence start date , Absence end date, No. of days in each band level of absence.
This table will be populated with the above data when the person enrolls into the absence with the configuration for log duration summary set to Yes

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bengapdurationsummary-19848.html#bengapdurationsummary-19848](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bengapdurationsummary-19848.html#bengapdurationsummary-19848)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_GAP_DURATION_SUMMARY_PK | GAP_DURATION_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GAP_DURATION_SUMMARY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Holds the assignment id |
| GAP_ABSENCE_PLAN_ID | NUMBER |  |  | Yes | Gap absence plan id |
| SUMMARY_TYPE | VARCHAR2 | 30 |  | Yes | Indicates the summary type |
| GAP_LEVEL | VARCHAR2 | 30 |  | Yes | Indicates the gap level |
| DURATION_IN_DAYS | NUMBER |  | 15 | Yes | Duration in days |
| DURATION_IN_HOURS | NUMBER |  | 15 | Yes | duration in hours |
| DATE_START | DATE |  |  | Yes | Start date of the absence duration. |
| DATE_END | DATE |  |  | Yes | End date of the absence duration. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_GAP_DURATION_SUMMARY_N2 | Non Unique | Default | ASSIGNMENT_ID, GAP_ABSENCE_PLAN_ID, SUMMARY_TYPE |
| BEN_GAP_DURATION_SUMMARY_N3 | Non Unique | Default | ASSIGNMENT_ID, SUMMARY_TYPE, DATE_START |
| BEN_GAP_DURATION_SUMMARY_PK | Unique | Default | GAP_DURATION_SUMMARY_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
