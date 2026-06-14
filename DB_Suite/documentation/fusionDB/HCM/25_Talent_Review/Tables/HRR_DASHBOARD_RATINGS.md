# HRR_DASHBOARD_RATINGS

Talent Review Dashboard Rating comments transaction table.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrdashboardratings-26712.html#hrrdashboardratings-26712](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrdashboardratings-26712.html#hrrdashboardratings-26712)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_DASHBOARD_RATINGS_PK | DASHBOARD_RATING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DASHBOARD_RATING_ID | NUMBER |  | 18 | Yes | Unique identifier for the rating of a metric code for a person |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier for business group of the reviewee |
| METRIC_CODE | VARCHAR2 | 240 |  | Yes | Metric code for which rating or comments would be stored |
| DASHBOARD_ID | NUMBER |  | 18 | Yes | Identifier for dashboard row |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifier for person who is reviewee of meeting |
| MEETING_ID | NUMBER |  | 18 | Yes | Identifier for meeting in which the rating is given for person |
| RATING_COMMENTS | CLOB |  |  |  | Rating comments for each rating of the reviewee of the meeting |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_DASHBOARD_RATINGS_PK | Unique | FUSION_TS_TX_DATA | DASHBOARD_RATING_ID |
| HRR_DASHBOARD_RATINGS_U1 | Unique | FUSION_TS_TX_DATA | DASHBOARD_ID, METRIC_CODE |
| HRR_DASHBOARD_RATINGS_U2 | Unique | FUSION_TS_TX_DATA | MEETING_ID, PERSON_ID, METRIC_CODE |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
