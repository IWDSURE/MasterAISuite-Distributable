# HRA_PF_DEFNS_B

This table stores the Process Flow Definitions of the performance management

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapfdefnsb-27727.html#hrapfdefnsb-27727](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapfdefnsb-27727.html#hrapfdefnsb-27727)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_PF_DEFNS_B_PK | PROCESS_FLOW_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PROCESS_FLOW_ID | NUMBER |  | 18 | Yes | Unique Id for the Process Flow definition set by the system |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| DATE_FROM | DATE |  |  | Yes | Defines the date from which the process flow definition is valid |  |
| DATE_TO | DATE |  |  | Yes | Defines the date till when the process flow definition is valid |  |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status code for the process flow definition defines if it is active or inactive |  |
| WKR_PERF_DOC_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker can generate performance document |  |
| MGR_PERF_DOC_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager can generate performance document |  |
| CONFIRM_CRITERIA_FLAG | VARCHAR2 | 30 |  |  | Flag to include step for setting of evaluation criteria |  |
| MGR_SET_EVAL_CRTRIA_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager can set evaluation criteria |  |
| WKR_SET_EVAL_CRTRIA_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker can set evaluation criteria |  |
| MGR_CMPLT_EVAL_CRTRIA_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager can complete evaluation criteria |  |
| WKR_CMPLT_EVAL_CRTRIA_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker can complete evaluation criteria |  |
| PRELIMINARY_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Flag to include step for entering preliminary ratings |  |
| ASSIGN_PARTICIPANTS_FLAG | VARCHAR2 | 30 |  |  | Flag to include steps for assignment of participants |  |
| MGR_SELECT_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether manager can select participants |  |
| WRK_SELECT_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker can select participants |  |
| MGR_TRACK_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether the manager can track participants |  |
| WRK_TRACK_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker can track participants |  |
| WRK_VIEW_SUB_FDBCK_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker can view feedback when it is submitted even before manager evaluation is completed. |  |
| WRK_REQUEST_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether the worker can send a request to the participants |  |
| MGR_ADD_QUESTION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether manager can add questions to the participants. |  |
| WRK_ADD_QUESTION_FLAG | VARCHAR2 | 30 |  |  | Indicates whether worker can add question for the participants. |  |
| MGR_ASSGN_PRTCPNT_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager can assign participants |  |
| WKR_ASSGN_PRTCPNT_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker can assign participants |  |
| PARTICIPANT_EVAL_FLAG | VARCHAR2 | 30 |  |  | Flag to include steps for participant evaluations of the worker |  |
| MGR_CMPLT_ASSGNMNT_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager can complete assignment cycle |  |
| WKR_CMPLT_ASSGNMNT_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker can complete assignment cycle |  |
| WKR_SELF_EVAL_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker performs self-evaluation |  |
| MGR_EVAL_OF_WRKR_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager performs evaluation of worker |  |
| EVAL_TASKS_CONCURRENT_FLAG | VARCHAR2 | 30 |  |  | Flag indicating whether worker self evaluation task and manager evaluation of worker task are concurrent. |  |
| DISABLE_RESUBMIT_MGR_EVAL | VARCHAR2 | 30 |  |  | Do not allow additional edit of manager evaluation task when completed |  |
| FIRST_APPROVAL_FLAG | VARCHAR2 | 30 |  |  | Flag to Include approval processing step |  |
| FIRST_APPROVAL_ID | VARCHAR2 | 30 |  |  | First approval Id |  |
| SECOND_APPROVAL_FLAG | VARCHAR2 | 30 |  |  | Flag to include second approval processing step |  |
| SECOND_APPROVAL_ID | VARCHAR2 | 30 |  |  | Second approval Id |  |
| AUTO_SUBMIT_APPROVAL_FLAG | VARCHAR2 | 30 |  |  | Flag to configure automatic submission of approval tasks |  |
| SHARE_PERFORMANCE_DOC_FLAG | VARCHAR2 | 30 |  |  | Flag to Include document sharing step |  |
| WKR_ACK_DOC_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker must acknowledge document |  |
| CONDUCT_MEETINGS_FLAG | VARCHAR2 | 30 |  |  | Flag to Include review meeting step |  |
| WKR_ACK_REVIEW_MTG_FLAG | VARCHAR2 | 30 |  |  | Flag indicating worker must acknowledge review meeting |  |
| FINAL_FEEDBACK_FLAG | VARCHAR2 | 30 |  |  | Flag to Include worker and/or manager final feedback step |  |
| WKR_FINAL_FEEDBCK_FLAG | VARCHAR2 | 30 |  |  | Flag indicating Worker can provide feedback on overall rating |  |
| MGR_FINAL_FEEDBACK_FLAG | VARCHAR2 | 30 |  |  | Flag indicating manager can provide feedback on worker's final feedback |  |
| NEXT_PERIOD_GOALS_FLAG | VARCHAR2 | 30 |  |  | Flag to include step to set next period goals |  |
| ALLOCATE_REWARDS_FLAG | VARCHAR2 | 30 |  |  | Flag to include step to allocate rewards |  |
| MANAGE_PROMOTIONS_FLAG | VARCHAR2 | 30 |  |  | Flag to include step to manage promotions |  |
| ALLOW_SHARE_LOCK_FOR_CALIB | VARCHAR2 | 30 |  |  | Indicates that sharing task can be locked for calibration in process flow. |  |
| MGR_REOPEN_PCPN_FDBCK_FLAG | VARCHAR2 | 30 |  |  | Indicates whether manager can reopen participant feedback. |  |
| WRK_REOPEN_PCPN_FDBCK_FLAG | VARCHAR2 | 30 |  |  | Indicates whether worker can reopen participant feedback. |  |
| PCPN_REOPEN_FDBCK_FLAG | VARCHAR2 | 30 |  |  | Indicates whether participant can reopen feedback. |  |
| CALENDAR_INVITE_FLAG | VARCHAR2 | 30 |  |  | Flag to enable calendar meeting invite. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_PF_DEFNS_B_PK | Unique | FUSION_TS_TX_DATA | PROCESS_FLOW_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
