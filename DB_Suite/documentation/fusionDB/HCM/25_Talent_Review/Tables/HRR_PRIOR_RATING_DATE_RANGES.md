# HRR_PRIOR_RATING_DATE_RANGES

The prior rating date range information is stored here. Prior ratings of reviewees are captured for this given range.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrpriorratingdateranges-17501.html#hrrpriorratingdateranges-17501](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrpriorratingdateranges-17501.html#hrrpriorratingdateranges-17501)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_PRIOR_RATING_DATE_RAN_PK | PRIOR_RATING_DATE_RANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRIOR_RATING_DATE_RANGE_ID | NUMBER |  | 18 | Yes | Unique identifier for Prior ratings date range. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_MEETINGS.MEETING_ID. |
| FROM_DATE | DATE |  |  |  | The date from which prior rating to be considered |
| TO_DATE | DATE |  |  |  | The date to which prior rating to be considered |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_PRIOR_RATING_DATE_RAN_FK1 | Non Unique | Default | MEETING_ID |
| HRR_PRIOR_RATING_DATE_RAN_PK | Unique | Default | PRIOR_RATING_DATE_RANGE_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
