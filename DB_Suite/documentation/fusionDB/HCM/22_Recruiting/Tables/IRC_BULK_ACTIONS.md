# IRC_BULK_ACTIONS

Stores Bulk action data for processing.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbulkactions-25994.html#ircbulkactions-25994](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbulkactions-25994.html#ircbulkactions-25994)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BULK_ACTIONS_PK | BULK_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BULK_ACTION_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CONTEXT_TYPE | VARCHAR2 | 64 |  |  | Business Object Type - It can be SUBMISSION_LIST or PROSPECT_LIST or POOL_MEMBER_LIST or CANDIDATE_SEARCH_LIST or RECOMMENDATION_LIST |
| CONTEXT_ID | NUMBER |  | 18 |  | Stores the Id releated to the Context Type Ex: REQUISITION_ID , POOL_ID etc |
| ACTION_CODE | VARCHAR2 | 64 |  |  | Stores what type of action need to be performed for Bulk actions like MOVE_CANDIDATE or SEND_EMAIL or DELETE_SUBMISSION |
| STATUS_CODE | VARCHAR2 | 64 |  |  | Stores the status of the Bulk Action. Lookup type - ORA_IRC_BULK_ACTION_STATUS |
| SUBMITTED_BY_USER | VARCHAR2 | 64 |  |  | stores the username who created the row. |
| SUBMITTED_DATE | TIMESTAMP |  |  |  | stores the date and time of the creation of the row. |
| QUERY | CLOB |  |  |  | Stores the query |
| QUERY_PARAMS | BLOB |  |  |  | Stores query params list in hash map |
| SELECTED_FILTERS | CLOB |  |  |  | Stores filtered label and values for display purpose (notification email and on action page) |
| QUERY_SOURCE | VARCHAR2 | 64 |  |  | Stores what type of Query it need to be like FILTER_BASED (or) MANUAL_SELECTION |
| UNSELECTED_IDS | CLOB |  |  |  | Stores Comma separated unselected Object Ids list |
| ESS_JOB_ID | NUMBER |  | 18 |  | Store ESS Job Id |
| ACTION_DATA | BLOB |  |  |  | Stores HashMap object which contains action data like new phase/state, email template etc.. |
| CONSUMER_IMPL_CLASS | VARCHAR2 | 240 |  |  | Stores Implementation class patch which need to be executed

Ex: "oracle.apps.hcm.recruiting.thirdParty.backgroundCheck.publicModelService.bulkActions.SubmissionBulkAction" |
| CONSUMER_AM_DEF | VARCHAR2 | 240 |  |  | Stores Consumer Application Module Definition in which action need to be performed

Ex: "oracle.apps.hcm.recruiting.hiring.submissions.core.protectedModel.applicationModule.SubmissionAM" |
| CONSUMER_AM_CONFIG_DEF | VARCHAR2 | 64 |  |  | Stores Consumer Application Module Configuration Definition in which action need to be performed

Ex: "SubmissionAMLocal" |
| NOTIFICATION_TOKENS | CLOB |  |  |  | Stores notification tokens for which bulk action is processed |
| TOTAL_COUNT | NUMBER |  | 18 |  | Stores total number of rows for which bulk action is processed |
| FAILED_COUNT | NUMBER |  | 18 |  | Stores failed rows count for which bulk action is processed |
| SKIPPED_COUNT | NUMBER |  | 18 |  | Stores skipped rows count for which bulk action is processed |
| CANCELLED_COUNT | NUMBER |  | 18 |  | Stores cancelled rows count for which bulk action is processed |
| FAILED_IDS | CLOB |  |  |  | Stores Comma separated failed row Ids |
| SKIPPED_IDS | CLOB |  |  |  | Stores Comma separated skipped row Ids |
| CANCELLED_IDS | CLOB |  |  |  | Comma separated cancelled row Ids |
| DEBUG_QUERY_PARAMS | CLOB |  |  |  | Stores query params in CLOB format. This is used for debugging purpose |
| DEBUG_ACTION_DATA | CLOB |  |  |  | Stores action data in CLOB format. This is used for debugging purpose |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BULK_ACTIONS_N1 | Non Unique | Default | CONTEXT_TYPE, CONTEXT_ID |
| IRC_BULK_ACTIONS_N2 | Non Unique | Default | STATUS_CODE, ACTION_CODE, LAST_UPDATE_DATE |
| IRC_BULK_ACTIONS_PK | Unique | Default | BULK_ACTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
