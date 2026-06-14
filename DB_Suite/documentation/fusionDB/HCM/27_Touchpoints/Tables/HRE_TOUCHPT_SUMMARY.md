# HRE_TOUCHPT_SUMMARY

It will store the computed touchpoints summary of interactions and checkins for team and company.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptsummary-9457.html#hretouchptsummary-9457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptsummary-9457.html#hretouchptsummary-9457)

## Primary Key

| Name | Columns |
|------|----------|
| hre_touchpt_summary_PK | TOUCHPT_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOUCHPT_SUMMARY_ID | NUMBER |  | 18 | Yes | System generated primary key for this table. |
| INTERACTION_DATA | CLOB |  |  |  | Interaction Data object for Coach O Agent |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ALL_PEOPLE_F |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M |
| INTRCNS_TEAM_DIRECTS_COUNT | NUMBER |  | 9 |  | Count of direct employees under Manager hierarchy having interactions. |
| TEAM_TOTAL_INTERACTIONS | NUMBER |  | 9 |  | Count of total number of interactions per team for the aggregation period. |
| TEAM_TOTAL_CHECK_INS | NUMBER |  | 9 |  | Count of total number of checkins per team for the aggregation period. |
| TEAM_AVG_INTERACTIONS | NUMBER |  | 9 |  | Average number of interactions per team for the aggregation period. |
| INTRCNS_CMPNY_DIR_COUNT | NUMBER |  | 9 |  | Count of direct employees in the company having interactions. |
| CHECK_INS_TEAM_DIRECTS_COUNT | NUMBER |  | 9 |  | Count of team directs having checkins |
| CHECK_INS_CMPNY_DIRECTS_COUNT | NUMBER |  | 9 |  | Count of company directs having checkins |
| COMPANY_TOTAL_CHECK_INS | NUMBER |  | 9 |  | Count of checkins in the company |
| COMPANY_TOTAL_INTERACTIONS | NUMBER |  | 9 |  | Count of interactions in the company |
| COMPANY_AVG_INTERACTIONS | NUMBER |  | 9 |  | Average number of interactions of all teams for the aggregation period. |
| TEAM_AVG_CHECK_INS | NUMBER |  | 9 |  | Average number of checkins per team for the aggregation period. |
| COMPANY_AVG_CHECK_INS | NUMBER |  | 9 |  | Average number of checkins of all teams for the aggregation period. |
| TEAM_COMPLETED_CHECK_INS | NUMBER |  | 9 |  | Count of total number of completed checkins in team for the current month. |
| TEAM_PENDING_CHECK_INS | NUMBER |  | 9 |  | Count of total number of pending checkins in team for the current month. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TOUCHPT_SUMMARY_N3 | Non Unique | HRE_TOUCHPT_SUMMARY_N3 | ASSIGNMENT_ID |
| HRE_TOUCHPT_SUMMARY_N5 | Non Unique | HRE_TOUCHPT_SUMMARY_N5 | BUSINESS_GROUP_ID |
| HRE_TOUCHPT_SUMMARY_N6 | Non Unique | HRE_TOUCHPT_SUMMARY_N6 | PERSON_ID, ASSIGNMENT_ID |
| hre_touchpt_summary_PK | Unique | Default | TOUCHPT_SUMMARY_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
