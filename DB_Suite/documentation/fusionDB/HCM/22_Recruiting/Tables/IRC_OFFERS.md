# IRC_OFFERS

Stores all the offer related details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircoffers-14745.html#ircoffers-14745](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircoffers-14745.html#ircoffers-14745)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_OFFERS_PK | OFFER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OFFER_ID | NUMBER |  | 18 | Yes | System generated primary key for this entity. |
| START_DATE_CHANGED_FLAG | VARCHAR2 | 1 |  |  | Indicates if proposed start date is changed in HR phase. |
| BATCH_CREATION_FLAG | VARCHAR2 | 1 |  |  | Indicates if offer was created as part of a batch. |
| ADDITIONALTEXT1 | CLOB |  |  |  | Offer Letter additional text 1. |
| ADDITIONALTEXT2 | CLOB |  |  |  | Offer Letter additional text 2. |
| OFFER_LETTER_LAYOUT_ID | NUMBER |  | 18 |  | Foreign key to IRC_DESCRIPTIONS_B table. Refers to BIP template used to generate the offer letter. |
| ONBOARDING_OSN_ID | NUMBER |  | 18 |  | Foreign key to IRC_ONBOARDING_OSN |
| EXPIRATION_DATE | DATE |  |  |  | Stores offer expiration date of this offer. |
| OFFER_NAME | VARCHAR2 | 240 |  | Yes | Stores the name of this offer. Offer name is not translatable. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Foreign key to IRC_SUBMISSIONS table. Refers to the Job submission. |
| PRESELECTED_HR_ACTION_ID | NUMBER |  | 18 |  | Stores the action id of the Offer. Foreign key to the PER_ACTIONS_B table. |
| HANDOFF_HR_SCENARIO_ID | NUMBER |  | 2 |  | Stores Offer handoff scenario ID |
| PERSON_ID | NUMBER |  | 18 |  | Stores the person id of the candidate for  this Offer. Foreign key to PER_PERSONS table. |
| PRESELECTED_HR_ACTIONTYPE_CODE | VARCHAR2 | 30 |  |  | Stores the action type code that you can also get on the preselected hr action relation. |
| RECRUITER_ID | NUMBER |  | 18 | Yes | Stores the PERSON_ID of the recruiter for this Offer. Foreign key to PER_PERSONS table. |
| RECRUITER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the recruiter's assignment for this Offer. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| ASSIGNMENT_OFFER_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the Offer. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| HIRING_MANAGER_ID | NUMBER |  | 18 | Yes | Stores the PERSON_ID of the hiring manager for this Offer. Foreign key to PER_PERSONS table. |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the hiring manager's assignment for this Offer. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| OFFER_COMMENTS | CLOB |  |  |  | Contains the text in the "Comments" field of the Comments And Attachments section for an Offer |
| COMMENTS | VARCHAR2 | 1000 |  |  | Stores the comments associated to the offer. |
| DESCRIPTION | CLOB |  |  |  | (Rich) text for describing the offer to the candidate. |
| ESIGNATURE_INSTRUCTIONS | CLOB |  |  |  | Copy of the ESignature instructions for EOffer. |
| ACCEPTED_ON_BEHALF | VARCHAR2 | 1 |  |  | To recall if current Offer got accepted on behalf of the candidate. The default value 'N' represents Candidate Acceptance, 'Y' represents Recruiter Acceptance on behalf of the candidate and 'A' represents Agent Acceptance on behalf of the candidate. |
| ACCEPTED_ON_BEHALF_BY_ID | NUMBER |  | 18 |  | User who has accepted on behalf of the candidate |
| ACCEPTED_ON_BEHALF_DATE | DATE |  |  |  | Date at which the offer got accepted on behalf |
| APPROVAL_SUBMITTED_DATE | TIMESTAMP |  |  |  | Indicates Date and Time of Offer Submission for approval |
| APPROVAL_REJECTED_DATE | TIMESTAMP |  |  |  | Indicates Date and Time of Offer approval rejection |
| EXTENDED_DATE | TIMESTAMP |  |  |  | Stores last extended date of the offer. |
| WITHDRAWN_REJECTED_DATE | TIMESTAMP |  |  |  | Stores last withdrawn date of the offer. |
| ACCEPTED_DATE | TIMESTAMP |  |  |  | Stores last accepted date of the offer. |
| APPROVED_DATE | TIMESTAMP |  |  |  | Stores the approved date of the offer. |
| DRAFTED_DATE | TIMESTAMP |  |  |  | Stores last drafted date of the offer. |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP6 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP7 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP8 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP9 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP10 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER21 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER22 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER23 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER24 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER25 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER26 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER27 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER28 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER29 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER30 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR1 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR2 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR3 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR4 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR5 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR6 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR7 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR8 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR9 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR10 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR11 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR12 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR13 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR14 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR15 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR16 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR17 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR18 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR19 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR20 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR21 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR22 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR23 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR24 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR25 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR26 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR27 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR28 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR29 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR30 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR31 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR32 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR33 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR34 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR35 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR36 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR37 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR38 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR39 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR40 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR41 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR42 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR43 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR44 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR45 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR46 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR47 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR48 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR49 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR50 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR51 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR52 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR53 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR54 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR55 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR56 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR57 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR58 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR59 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR60 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR61 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR62 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR63 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR64 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR65 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR66 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR67 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR68 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR69 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR70 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR71 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR72 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR73 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR74 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR75 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR76 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR77 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR78 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR79 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR80 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR81 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR82 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR83 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR84 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR85 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR86 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR87 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR88 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR89 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CHAR90 | VARCHAR2 | 1000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OFFER_LETTER_CUSTOMIZED_FLAG | VARCHAR2 | 1 |  | Yes | Column that tells if the offer letter is customized or relies on the Content Library version. |
| RTF_RESOLVED_FLAG | VARCHAR2 | 1 |  | Yes | Column that indicates whether the custom offer letter was resolved before downloading. |
| MOVE_TO_HR_STATUS | VARCHAR2 | 30 |  |  | Stores the Move to HR status lookup code of the offer.  The corresponding lookup type is ORA_IRC_OFFER_MOVE_TO_HR_STATUS. |
| MOVE_TO_HR_DATE | TIMESTAMP |  |  |  | Timestamp when the offer got moved to HR phase. |
| OFFER_MOVE_STATUS | VARCHAR2 | 30 |  |  | Indicates last move status of offer. The corresponding lookup type is ORA_IRC_OFFER_MOVE_STATUS. |
| EXTEND_SCHEDULE_DATE | TIMESTAMP |  |  |  | Indicates the date and time when the offer is scheduled to be extended. |
| EXTEND_UPDATE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the last update of extend offer. |
| EXTEND_UPDATED_BY | VARCHAR2 | 64 |  |  | Indicates the user who last updated extend offer. |
| EXTEND_REQUEST_ID | NUMBER |  | 18 |  | Indicates the latest request ID of the job for extend offer. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the object. |
| PARENT_OFFER_ID | NUMBER |  | 18 |  | Foreign key to IRC_OFFERS_B.OFFER_ID |
| MERGED_FLAG | VARCHAR2 | 1 |  |  | Determines if the Offer is a result of merge. |
| BYPASS_OFFER_LC_FLAG | VARCHAR2 | 1 |  |  | Determines if the user has opted to speed through offer phase. |
| DUP_CHECK_FAILED_FLAG | VARCHAR2 | 1 |  |  | Flag to determine duplicate check status. |
| STATE_POST_PROCESS_STATUS | VARCHAR2 | 30 |  |  | Stores the Post processing status for a given state. Lookup ORA_IRC_STATE_PROCESS_STATUS. |
| ASYNC_QUEUED_DATE | TIMESTAMP |  |  |  | Indicates the date when the offer was queued for asynchronous processing. |
| ASYNC_RETRY_COUNT | NUMBER |  |  |  | Indicates the number of times the retry has been attempted for an asynchronous process. |
| HR_PROCESSED_DATE | TIMESTAMP |  |  |  | Stores the timestamp when the Offer was last moved to HR Processed State. |
| AUTO_PROCESS_FLAG | VARCHAR2 | 1 |  |  | Column that determines whether the offer for internal candidate should be included or excluded in Auto Processing. |
| MOVE_TO_HR_PREVAL_FLAG | VARCHAR2 | 1 |  |  | Column that determines if the Move to HR prevalidations are completed. |
| REDRAFT_COUNT | NUMBER |  |  |  | Indicates the number of times that the current offer is redrafted. |
| VISITED_SECTIONS | CLOB |  |  |  | Offer visited sections information |
| PROJECTED_START_DATE | DATE |  |  |  | Stores the Proposed start date entered on the Basic Info of Assignment |
| CURRENT_STATE_ID | NUMBER |  | 18 |  | Stores the current state of the Job Application.Foreign Key to IRC_STATES_B |
| CURRENT_PHASE_ID | NUMBER |  | 18 |  | Stores the current phase of the Job Application. Foreign Key to table IRC_PHASES_B |
| REQUISITION_ID | NUMBER |  | 18 |  | Stores the Requisition ID of the Job Offer. Foreign Key to IRC_REQUISITIONS_B |
| CANDIDATE_NUMBER | VARCHAR2 | 30 |  |  | Stores the Candidate Number of Candidate on the Job Offer |
| REQUISITION_NUMBER | VARCHAR2 | 240 |  |  | Stores the Requisition Number of Requisition on the Job Offer |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | Stores the Person type of Candidate when applied to the job Application |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Stores the Business Unit ID of the Offer Assignment |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Stores the Department ID of the Offer Assignment |
| POSITION_ID | NUMBER |  | 18 |  | Stores the Position ID of the Offer Assignment |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Stores the Legal Employer ID of the Offer Assignment |
| JOB_ID | NUMBER |  | 18 |  | Stores the Job ID of the Offer Assignment |
| LOCATION_ID | NUMBER |  | 18 |  | Stores the Work Location ID of the Offer Assignment |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_OFFERS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_OFFERS_FK10 | Non Unique | Default | REQUISITION_ID |
| IRC_OFFERS_FK2 | Non Unique | Default | RECRUITER_ID |
| IRC_OFFERS_FK3 | Non Unique | Default | HIRING_MANAGER_ID |
| IRC_OFFERS_FK4 | Non Unique | Default | PRESELECTED_HR_ACTION_ID |
| IRC_OFFERS_FK5 | Non Unique | Default | ACCEPTED_ON_BEHALF_BY_ID |
| IRC_OFFERS_FK6 | Non Unique | Default | PERSON_ID |
| IRC_OFFERS_FK7 | Non Unique | Default | OFFER_LETTER_LAYOUT_ID |
| IRC_OFFERS_FK8 | Non Unique | Default | PARENT_OFFER_ID |
| IRC_OFFERS_FK9 | Non Unique | Default | ASSIGNMENT_OFFER_ID |
| IRC_OFFERS_IRC_ONBOARDING_FK1 | Non Unique | Default | ONBOARDING_OSN_ID |
| IRC_OFFERS_N1 | Non Unique | Default | CURRENT_STATE_ID, CURRENT_PHASE_ID, PROJECTED_START_DATE |
| IRC_OFFERS_N2 | Non Unique | Default | CANDIDATE_NUMBER |
| IRC_OFFERS_N3 | Non Unique | Default | REQUISITION_NUMBER |
| IRC_OFFERS_N4 | Non Unique | Default | APPROVAL_SUBMITTED_DATE |
| IRC_OFFERS_U1 | Unique | Default | OFFER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
