# IRC_TN_JA_REQUEST_MORE_INFO

This is the table for storing Request More information details of a Job Application on Talent Network.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjarequestmoreinfo-8375.html#irctnjarequestmoreinfo-8375](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjarequestmoreinfo-8375.html#irctnjarequestmoreinfo-8375)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JA_REQ_MORE_INFO_PK | JA_APP_MORE_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_APP_MORE_INFO_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| JOB_APP_ID | NUMBER |  | 18 | Yes | To store the Job Application Id. Foreign Key to IRC_TN_JOB_APPLICATIONS. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | To store the subscriber id. Foreign Key to IRC_TN_SUBSCRIBERS. |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agent who submitted the candidate job application. Foreign key to IRC_AGENCIES table. |
| AGENT_ID | NUMBER |  | 18 | Yes | Stores the AGENT_ID of the Agent who submitted the candidate job application. Foreign key to IRC_AGENTS table. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Talent Network Request More Info Status as a lookup code. Lookup type is ORA_IRC_PADC_STATUS. |
| RMI_IDENTIFIER_GUID | VARCHAR2 | 64 |  |  | System generated unique identifier for deep links. |
| RMI_REQUESTED_DATE | TIMESTAMP |  |  |  | Indicates the date when the RMI is created on Talent Network. |
| RMI_SUBMITTED_DATE | TIMESTAMP |  |  |  | Indicates the date when the RMI is Submitted/Responded by the agent on Talent Network. |
| FA_SECONDARY_FLOW_ID | NUMBER |  | 18 |  | Stores the Secondary Flow Id from FA. Derived from IRC_JA_SECONDARY_FLOWS.SECONDARY_FLOW_ID. |
| FA_STEP_ACTION_USAGE_ID | NUMBER |  | 18 |  | Stores the Step Action Usage Id from FA. Derived from IRC_JA_SECONDARY_FLOWS.STEP_ACTION_USAGE_ID. |
| FA_APPLY_FLOW_ID | NUMBER |  | 18 |  | Stores the Apply Flow Id from FA. Derived from IRC_APPLY_FLOWS.APPLY_FLOW_ID. |
| FA_APPLY_FLOW_VERSION_ID | NUMBER |  | 18 |  | Stores the Apply Flow Version Id from FA. Derived from IRC_JA_SECONDARY_FLOWS.AF_VERSION_ID. |
| FA_SEC_FLOW_TRIGGER_DATE | TIMESTAMP |  |  |  | Indicates the date when the RMI is triggered on FA. Derived from IRC_JA_SECONDARY_FLOWS.SEC_FLOW_TRIGGER_DATE. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JA_REQ_MORE_INFO_FK1 | Non Unique | Default | JOB_APP_ID |
| IRC_TN_JA_REQ_MORE_INFO_FK2 | Non Unique | Default | SUBSCRIBER_ID |
| IRC_TN_JA_REQ_MORE_INFO_FK3 | Non Unique | Default | AGENCY_ID |
| IRC_TN_JA_REQ_MORE_INFO_FK4 | Non Unique | Default | AGENT_ID |
| IRC_TN_JA_REQ_MORE_INFO_PK | Unique | Default | JA_APP_MORE_INFO_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
