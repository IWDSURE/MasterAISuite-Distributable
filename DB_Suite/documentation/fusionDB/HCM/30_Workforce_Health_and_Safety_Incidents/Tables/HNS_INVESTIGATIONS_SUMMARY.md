# HNS_INVESTIGATIONS_SUMMARY

HNS INVESTIGATIONS SUMMARY. This table stores all investigation related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestigationssummary-15667.html#hnsinvestigationssummary-15667](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinvestigationssummary-15667.html#hnsinvestigationssummary-15667)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INVESTIGATIONS_SUMMARY_PK | INVESTIGATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INVESTIGATE_ID | NUMBER |  | 18 | Yes | Unique Investigation Identifier. Primary key for HNS_INVESTIGATIONS_SUMMARY table. |
| INVESTIGATE_NO | VARCHAR2 | 32 |  | Yes | Unique user generated Investigation  Identifier. |
| INVESTIGATE_DATE | TIMESTAMP |  |  | Yes | The date the investigation was initiated by the investigation owner. |
| INCIDENT_ID | NUMBER |  | 18 |  | Unique Incident Identifier. Foreign key for HNS_INCIDENTS_SUMMARY table. |
| INCIDENT_DETAIL_ID | NUMBER |  | 18 |  | Unique Incidents Event identifier. Foreign key for HNS_INCIDENTS_DETAIL. |
| INVESTIGATE_SUMMARY | VARCHAR2 | 1000 |  | Yes | The user entered summary on the investigation. |
| INVESTIGATE_TYPE_CODE | VARCHAR2 | 30 |  |  | Type of investigation. This signifies the level of investigation. Low level, high level. |
| INVESTIGATE_OWNER_ID | NUMBER |  |  |  | The employee ID of ther person who owns the investigation. The investigation owner will always be an employee. |
| INVEST_OWNER_ASSIGN_ID | NUMBER |  |  |  | The Assignment ID of ther person who owns the investigation. The investigation owner will always be an employee. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted Flag.Signifies whether investigation is deleted. |
| COMPLETED_FLAG | VARCHAR2 | 1 |  |  | Completed Flag. Signifies whether Investigation is completed |
| INVEST_STATUS_CODE | VARCHAR2 | 30 |  |  | INVEST_STATUS_CODE column: Current InVESTIGATION  Status. Lookup to FND_LOOKUP STATUS. |
| TARGET_COMPLETION_DATE | TIMESTAMP |  |  | Yes | Target Completion date for an investigation. |
| ACTUAL_COMPLETION_DATE | TIMESTAMP |  |  |  | Actual completion date for an investigation |
| LESSONS_LEARNED | VARCHAR2 | 4000 |  |  | Lessons Learned. |
| INVESTIGATE_DESCRIPTION | CLOB |  |  |  | Description entered by the user for the investigation. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| INVEST_REVIEWER_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to investigation reviewer. |
| INVEST_APPROVER_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to investigation approver. |
| INVEST_PRECOM_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to investigation precom approver. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | To store the Questionnaire referenced by the Investigation. |
| FINDING_COMMENT | VARCHAR2 | 4000 |  |  | User entered finding comments. |
| FINDING_FINAL_RESPONSE | VARCHAR2 | 4000 |  |  | User entered finding final response. |
| CASUAL_FACTORS_CODE | VARCHAR2 | 1000 |  |  | Code Lookup from FND_LOOKUP, ORA_HNS_CAUSAL_FACTORS. |
| CONTRIBUTING_FACTORS_CODE | VARCHAR2 | 1000 |  |  | Code Lookup from FND_LOOKUP, ORA_HNS_CONTRIBUTING_FACTORS. |
| UNDERLYING_FACTORS_CODE | VARCHAR2 | 1000 |  |  | Code Lookup from FND_LOOKUP,ORA_HNS_UNDERLYING_FACTORS. |
| IMMEDIATE_CAUSE_CODE | VARCHAR2 | 1000 |  |  | Code Lookup from FND_LOOKUP,ORA_HNS_IMMEDIATE_CAUSE. |
| ROOT_CAUSE_CODE | VARCHAR2 | 1000 |  |  | Code Lookup from FND_LOOKUP,ORA_HNS_ROOT_CAUSE. |
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
| ACTION_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Action Required Flag Column : Check box to confirm whether an action is required. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HNS_INVESTIGATIONS_SUMMARY_N1 | Non Unique | FUSION_TS_TX_DATA | INCIDENT_DETAIL_ID | Active |
| HNS_INVESTIGATIONS_SUMMARY_N2 | Non Unique | FUSION_TS_TX_DATA | INCIDENT_ID |  |
| HNS_INVEST_SUMMARY_UK1 | Unique | FUSION_TS_TX_DATA | INVESTIGATE_ID | Active |
| HNS_INVEST_SUMMARY_UK2 | Unique | FUSION_TS_TX_DATA | INVESTIGATE_NO | Active |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
