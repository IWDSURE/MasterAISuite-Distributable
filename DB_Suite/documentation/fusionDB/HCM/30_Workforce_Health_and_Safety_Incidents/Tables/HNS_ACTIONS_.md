# HNS_ACTIONS_

HNS ACTIONS. This table stores all Action related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsactions-20200.html#hnsactions-20200](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsactions-20200.html#hnsactions-20200)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_ACTIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for Action table. |
| ACTION_NO | VARCHAR2 | 32 |  |  | Unique user-defined identifierfor Action table. |
| RECOMMEND_ID | NUMBER |  | 18 |  | Recommendation Identifier. Foreign key for HNS_INVEST_RECOMMENDS table. |
| INCIDENT_ID | NUMBER |  | 18 |  | Incident Identifier. Foreign key for HNS_INCIDENTS_SUMMARY. |
| COMPLETED_FLAG | VARCHAR2 | 1 |  |  | Completed flag. Signifies whether the Action is completed. |
| ACTION_STATUS_CODE | VARCHAR2 | 30 |  |  | ACTION_STATUS_CODE column: Current Action Status. Lookup to FND_LOOKUP STATUS. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag. Signifies whether the Action is deleted.. |
| ACTION_SUMMARY | VARCHAR2 | 1000 |  |  | Summary information for an Action.This is a user entered field. |
| DESCRIPTION | CLOB |  |  |  | Detailed description for an Action.This is a user entered field. |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Type of Action identifier.E.g. Corrective, preventive |
| PRIORITY_CODE | VARCHAR2 | 30 |  |  | Priority Identifier. Seed data from FND_LOOKUP with Lookup Type = HNS_PRIORITY |
| REQ_RESOURCES | VARCHAR2 | 200 |  |  | Required Resources for an action. The column is comma delimited with the req resources will be separated by comma. |
| ACTION_DATE | TIMESTAMP |  |  |  | The date when the action was created and assigned to the action owner. |
| ACTION_REVIEWER_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to action reviewer. |
| ACTION_APPROVER_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to action approver. |
| ACTION_PRECOM_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to action precomm approver. |
| LESSONS_LEARNED | VARCHAR2 | 4000 |  |  | Lessons Learned. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ESTIMATED_COST | NUMBER |  |  |  | Estimated cost associated with the Action. |
| EST_COST_CURRENCY_CODE | VARCHAR2 | 10 |  |  | Estimated Cost Currency Code. Currency code related to the estimated cost. Default to USD. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_ACTIONSN1_ | Non Unique | Default | ACTION_ID, LAST_UPDATE_DATE |
| HNS_ACTIONS_UK1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, ACTION_ID |
| HNS_ACTIONS_UK2_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, ACTION_NO |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
