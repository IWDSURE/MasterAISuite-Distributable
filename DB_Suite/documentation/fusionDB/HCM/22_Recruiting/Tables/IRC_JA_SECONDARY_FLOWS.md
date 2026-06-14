# IRC_JA_SECONDARY_FLOWS

Transactional table that stores information regarding the trigger and then submission of a secondary flow.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjasecondaryflows-8402.html#ircjasecondaryflows-8402](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjasecondaryflows-8402.html#ircjasecondaryflows-8402)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_SECONDARY_FLOWS_PK | SECONDARY_FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SECONDARY_FLOW_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_SUBMISSIONS table. Column provides an association with original job application. |
| AF_VERSION_ID | NUMBER |  | 18 |  | Foreign key to IRC_AF_VERSIONS table. The apply flow version used to submit the secondary flow. |
| ESIGN_DESC_VERSION_ID | NUMBER |  | 18 |  | Foreign key to IRC_DESC_VERSIONS_B table. The esign version used to submit secondary apply flow. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_LC_ACTION_USAGES_B table. Associate a secondary flow trigger/submission with an action in the candidate selection process. |
| STATUS_CODE | VARCHAR2 | 32 |  | Yes | ORA_TRIGGERED' for secondary flows triggered but not yet submitted or 'ORA_SUBMITTED' for secondary flows that have been both triggered and submitted. |
| SEC_FLOW_TRIGGER_DATE | TIMESTAMP |  |  | Yes | Stores the timestamp when the secondary flow was triggered. This is one of three columns to track the progress made on the secondary flow. |
| SEC_FLOW_TRIGGERED_BY | VARCHAR2 | 64 |  | Yes | Stores the name of the recruiter or hiring manager, who triggered the secondary flow. This is one of three columns to track the progress made on the secondary flow. |
| SEC_FLOW_SUBM_DATE | TIMESTAMP |  |  |  | Stores the timestamp when the secondary flow was submitted by the candidate. This is one of three columns to track the progress made on the secondary flow. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_SECONDARY_FLOWS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_JA_SECONDARY_FLOWS_FK2 | Non Unique | Default | AF_VERSION_ID |
| IRC_JA_SECONDARY_FLOWS_FK3 | Non Unique | Default | ESIGN_DESC_VERSION_ID |
| IRC_JA_SECONDARY_FLOWS_U1 | Unique | Default | SECONDARY_FLOW_ID |
| IRC_JA_SECONDARY_FLOWS_U2 | Unique | Default | STEP_ACTION_USAGE_ID, SUBMISSION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
