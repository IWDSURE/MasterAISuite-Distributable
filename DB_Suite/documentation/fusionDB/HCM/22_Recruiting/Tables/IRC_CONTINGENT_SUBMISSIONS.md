# IRC_CONTINGENT_SUBMISSIONS

This table is used for storing Contingent Submissions details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccontingentsubmissions-25285.html#irccontingentsubmissions-25285](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccontingentsubmissions-25285.html#irccontingentsubmissions-25285)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CONTINGENT_SUBMISSIONS_PK | CONTINGENT_SUBMISSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTINGENT_SUBMISSION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CANDIDATES table. |
| TN_AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agency |
| STEP_STATUS_CODE | VARCHAR2 | 64 |  |  | Stores Contingent Submission Workflow Step Code. The corresponding lookup type is ORA_IRC_CS_STEP_STATUS_TYPE |
| STEP_SUB_STATUS_CODE | VARCHAR2 | 64 |  |  | Stores Contingent Submission Workflow Secondary Step Code |
| PROJECTED_START_DATE | DATE |  |  |  | Contingent Submission assignment Projected Start Date |
| PROJECTED_END_DATE | DATE |  |  |  | Contingent Submission assignment Projected End Date |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | Person type of the job applicant when they applied for the job. |
| SUBMISSION_DATE | TIMESTAMP |  |  |  | Stores the date when this submission was submitted. |
| SUBM_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Stores the last modified date for the Submission. This is updated even when the child entities of the Submission table are updated. This can be used by customers to export submissions which were updated after a certain date. |
| SUBMISSION_LANGUAGE_CODE | VARCHAR2 | 4 |  |  | Stores the language code for the submission |
| PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to profiles table HRT_PROFILES_B. |
| TN_AGENCY_NAME | VARCHAR2 | 240 |  |  | Stores the Agency Name of the Agency |
| TN_AGENT_ID | NUMBER |  | 18 |  | Stores the TN_AGENT_ID of the Agency to which the agent belong. |
| TN_AGENT_NAME | VARCHAR2 | 300 |  |  | Stores the First Name and Last Name of the Agent |
| BILL_RATE | NUMBER |  |  |  | Stores the Bill Rate value provided the agency while submitting the Contingent Application |
| BILL_FREQUENCY_CODE | VARCHAR2 | 64 |  |  | Stores the Bill Frequency value provided the agency while submitting the Contingent Application |
| BILL_CURRENCY_CODE | VARCHAR2 | 64 |  |  | Stores  the Bill Currency Code value provided the agency while submitting the Contingent Application |
| DUPLICATE_RESOLVED_FLAG | VARCHAR2 | 1 |  |  | Indicates if there was a duplicate resolution |
| SUBMITTED_PERSON_ID | NUMBER |  | 18 |  | Stores the Original Person Id value when the application was created |
| REF_CONT_SUBMISSION_ID | NUMBER |  | 18 |  | Stores Reference Contingent  Submission Id |
| AGENCY_PROVIDED_URL | VARCHAR2 | 4000 |  |  | Stores the  Reference URL value provided by the agency while submitting the Contingent Application |
| AGENCY_REFERENCE_ID | VARCHAR2 | 64 |  |  | Stores the Reference Id value provided by the agency while submitting the Contingent Application |
| HANDOVER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Unique identifier of the newly created work relationship assignment(PWK/CWK). Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| CONVERTED_ASSIGNMENT_ID | NUMBER |  | 18 |  | Unique identifier of the newly created work relationship assignment when PWK is converted to CWK. Foreign key to PER_ALL_ASSIGNMENTS_M table |
| HR_SYNC_SCENARIO | NUMBER |  | 18 |  | Value identifying HR processing scenario of the Contingent Application. Ex Scenario 1 - Net New Hir, Scenario 2 - Returning Ex worker etc. |
| COMMENTS | CLOB |  |  |  | Stores the agency provided comments for the Contingent Application |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CONTINGENT_SUBMISSIONS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_CONTINGENT_SUBMISSIONS_FK2 | Non Unique | Default | PERSON_ID |
| IRC_CONTINGENT_SUBMISSIONS_FK3 | Non Unique | Default | PROFILE_ID |
| IRC_CONTINGENT_SUBMISSIONS_FK4 | Non Unique | Default | CONVERTED_ASSIGNMENT_ID |
| IRC_CONTINGENT_SUBMISSIONS_FK5 | Non Unique | Default | HANDOVER_ASSIGNMENT_ID |
| IRC_CONTINGENT_SUBMISSIONS_PK | Unique | Default | CONTINGENT_SUBMISSION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
