# HNS_INVEST_RECOMMENDS_

HNS INVEST RECOMMENDS. This table all recommendation related data for an investigation.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestrecommends-8835.html#hnsinvestrecommends-8835](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestrecommends-8835.html#hnsinvestrecommends-8835)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INVEST_RECOMMENDS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, RECOMMEND_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMEND_ID | NUMBER |  | 18 | Yes | RECOMMEND_ID: Primary key for HNS_INVEST_RECOMMENDS table . |
| RECOMMENDATION_SUMMARY | VARCHAR2 | 1000 |  |  | Recommendation summary. This is a field to store recommendation summary. |
| RECOMMEND_SUGGESTION_FLAG | VARCHAR2 | 1 |  |  | Recommendation suggestion flag for improvement. |
| FINDING_ID | NUMBER |  | 18 |  | Investigation Finding Identifier. Foreign key for HNS_INVEST_FINDINGS |
| ACTION_FLAG | VARCHAR2 | 1 |  |  | IS_ACTION : This flag signifies whether there is an action associated with the recommendation. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the investigation recommendation  is checked for deletion. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INVEST_RECOMMENDSN1_ | Non Unique | Default | RECOMMEND_ID, LAST_UPDATE_DATE |
| HNS_INVEST_RECOMMENDS_UK1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, RECOMMEND_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
