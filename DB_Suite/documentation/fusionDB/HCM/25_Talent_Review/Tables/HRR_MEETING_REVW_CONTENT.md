# HRR_MEETING_REVW_CONTENT

This meeting table includes the content to be reviewed in the meeting.

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingrevwcontent-29381.html#hrrmeetingrevwcontent-29381](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrmeetingrevwcontent-29381.html#hrrmeetingrevwcontent-29381)

## Primary Key

| Name | Columns |
|------|----------|
| HRR_MEETING_RVW_CONTENT_PK | REVIEW_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REVIEW_CONTENT_ID | NUMBER |  | 18 | Yes | Primary key to this table. |  |
| REVW_RATING_SEQUENCE | NUMBER |  | 14 |  | The sequence column stores the order of ratings, determining their display order in the UI. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |  |
| MEETING_ID | NUMBER |  | 18 | Yes | Foreign key to HRR_MEETINGS. |  |
| REVW_CAREER_INTEREST | VARCHAR2 | 30 |  |  | Indicates whether Career Interest should be reviewed in the meeting. | Obsolete |
| REVW_CAREER_POTENTIAL | VARCHAR2 | 30 |  |  | Indicates whether Career Potential should be reviewed in the meeting. | Obsolete |
| REVW_COMP_RECORDS | VARCHAR2 | 30 |  |  | Indicates whether Compensation Records should be reviewed in the meeting. | Obsolete |
| REVW_COMPETENCIES | VARCHAR2 | 30 |  |  | Indicates whether Competencies should be reviewed in the meeting. | Obsolete |
| REVW_GOALS | VARCHAR2 | 30 |  |  | Indicates whether Goals should be reviewed in the meeting. | Obsolete |
| REVW_PERF_RATINGS | VARCHAR2 | 30 |  |  | Indicates whether Performance Ratings should be reviewed in the meeting. | Obsolete |
| REVW_RISK_LOSS | VARCHAR2 | 30 |  |  | Indicates whether Risk of Loss should be reviewed in the meeting. | Obsolete |
| REVW_IMPACT_LOSS | VARCHAR2 | 30 |  |  | Indicates whether Impact of Loss should be reviewed in the meeting. | Obsolete |
| REVW_MOBILITY | VARCHAR2 | 30 |  |  | REVW_MOBILITY | Obsolete |
| REVW_TALENT_SCORE | VARCHAR2 | 30 |  |  | REVW_TALENT_SCORE | Obsolete |
| DATA_VALIDITY_CODE | VARCHAR2 | 30 |  |  | The data validity guideline is intended to help the participants determine if the data already captured in the system is still valid for the talent review meeting. | Obsolete |
| METRIC_ID | NUMBER |  | 18 | Yes | Metric defined in Dashboard template and enabled to be used as axis or underlay. |  |
| USE_AS_AXIS_FLAG | VARCHAR2 | 30 |  |  | Flag to specify if a metric can be used as an axis |  |
| USE_AS_UNDERLAY_FLAG | VARCHAR2 | 30 |  |  | Flag to specify if a metric can be used as an underlay |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRR_MEETING_REVW_CONTENT_FK1 | Non Unique | FUSION_TS_TX_DATA | MEETING_ID |
| HRR_MEETING_REVW_CONTENT_PK | Unique | FUSION_TS_TX_DATA | REVIEW_CONTENT_ID |

---

[← Back to Index](../25_Talent_Review_Tables_Index.md)
