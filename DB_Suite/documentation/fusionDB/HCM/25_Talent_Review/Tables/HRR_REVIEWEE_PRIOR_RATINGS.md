# HRR_REVIEWEE_PRIOR_RATINGS

Talent Review Dashboard Prior Rating transaction table.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrrevieweepriorratings-30723.html#hrrrevieweepriorratings-30723](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrrevieweepriorratings-30723.html#hrrrevieweepriorratings-30723)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_REVIEWEE_PR_RTNGS_PK | REVIEWEE_PRIOR_RATING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REVIEWEE_PRIOR_RATING_ID | NUMBER |  | 18 | Yes | Unique identifier for Reviewee prior ratings. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| DASHBOARD_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_DASHBOARDS.DASHBOARD_ID. |
| MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_MEETINGS.MEETING_ID. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id information of the Reviewee. |
| PERF_RT_LVL_ID | NUMBER |  | 18 |  | Performance rating level of the Reviewee. |
| POT_RT_LVL_ID | NUMBER |  | 18 |  | Potential rating levell of the Reviewee. |
| RISK_LOSS_RT_LVL_ID | NUMBER |  | 18 |  | Risk of loss rating levell of the Reviewee. |
| IMPACT_LOSS_RT_LVL_ID | NUMBER |  | 18 |  | Impact of loss rating levell of the Reviewee. |
| TALENT_SCORE_RT_LVL_ID | NUMBER |  | 18 |  | Talent score rating levell of the Reviewee. |
| EXTN_METRIC_VALUE1 | NUMBER |  | 18 |  | 1st Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE2 | NUMBER |  | 18 |  | 2nd Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE3 | NUMBER |  | 18 |  | 3rd Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE4 | NUMBER |  | 18 |  | 4th Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE5 | NUMBER |  | 18 |  | 5th Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE6 | NUMBER |  | 18 |  | 6th Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE7 | NUMBER |  | 18 |  | 7th Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE8 | NUMBER |  | 18 |  | 8th Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE9 | NUMBER |  | 18 |  | 9th Extensible rating level  of the Reviewee. |
| EXTN_METRIC_VALUE10 | NUMBER |  | 18 |  | 10th Extensible rating level  of the Reviewee. |
| MOBILITY_VALUE | VARCHAR2 | 30 |  |  | Mobility rating (no rating level) of the Reviewee. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_REVIEWEE_PR_RTNGS_FK1 | Non Unique | Default | DASHBOARD_ID |
| HRR_REVIEWEE_PR_RTNGS_PK | Unique | Default | REVIEWEE_PRIOR_RATING_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
