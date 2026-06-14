# HNS_RISK_ASSESSMENTS_

HNS_RISK_ASSESSMENTS..This table stores the Risk Assessment details.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsriskassessments-12694.html#hnsriskassessments-12694](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsriskassessments-12694.html#hnsriskassessments-12694)

## Primary Key

| Name | Columns |
|------|----------|
| hns_risk_assessments_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, RISK_ASSESSMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RISK_ASSESSMENT_ID | NUMBER |  | 18 | Yes | RISK_ASSESSMENT_ID unique identifier. Primary key for HNS_RISK_ASSESSMENT table. |
| TASK_ID | NUMBER |  | 18 |  | Task Assigned to the Risk Assessment. |
| TASK_TYPE_CODE | VARCHAR2 | 30 |  |  | Task Type identifier. Lookup to the Task Type FND lookup. |
| CONSEQUENCE_CODE | VARCHAR2 | 30 |  |  | Consequence Code Identifier. Lookup from HNS_CONFIG_B.ORA_HNS_RISK_CONSEQUENCE. |
| LIKELIHOOD_CODE | VARCHAR2 | 30 |  |  | Likelihood Identifier. Lookup from HNS_CONFIG_B.ORA_HNS_RISK_LIKELIHOOD. |
| RISK_ASSESSMENT_DATE | TIMESTAMP |  |  |  | Risk Assessment Date. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to check whether is record is deleted. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_RISK_ASSESSMENTSN1_ | Non Unique | Default | RISK_ASSESSMENT_ID, LAST_UPDATE_DATE |
| hns_risk_assessments_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, RISK_ASSESSMENT_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
