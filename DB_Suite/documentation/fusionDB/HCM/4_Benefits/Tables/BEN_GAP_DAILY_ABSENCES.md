# BEN_GAP_DAILY_ABSENCES

This table is used to store daily absence details like absence date, work pattern and the level of entitlement for an absence plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bengapdailyabsences-31206.html#bengapdailyabsences-31206](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bengapdailyabsences-31206.html#bengapdailyabsences-31206)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_GAP_DAILY_ABSENCES_PK | GAP_DAILY_ABSENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GAP_DAILY_ABSENCE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| GAP_ABSENCE_PLAN_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_GAP_ABSENCES_PLANS. |
| ABSENCE_DATE | DATE |  |  | Yes | The date of a day or fraction of a day of an absence. |
| WORK_PATTERN_DAY_TYPE | VARCHAR2 | 30 |  | Yes | Work pattern day type WORKON or OFFWORK. |
| LEVEL_OF_ENTITLEMENT | VARCHAR2 | 30 |  | Yes | Level of entitlement is the entitlement band info. |
| LEVEL_OF_PAY | VARCHAR2 | 30 |  | Yes | Band info for paid days. |
| DURATION | NUMBER |  |  | Yes | Duration for this day or a fraction of the day. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DURATION_IN_HOURS | NUMBER |  | 11 |  | Duration for this day or a fraction of the day expressed in hours. |
| WORKING_DAYS_PER_WEEK | NUMBER |  | 6 |  | Average number of days per week that a person worked on this day of absence. |
| FTE | NUMBER |  | 25 |  | Full time equivalent of the assignment as of the absence date. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_GAP_DAILY_ABSENCES_N1 | Non Unique | Default | GAP_ABSENCE_PLAN_ID, ABSENCE_DATE |
| BEN_GAP_DAILY_ABSENCES_PK | Unique | Default | GAP_DAILY_ABSENCE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
