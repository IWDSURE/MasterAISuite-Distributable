# IRC_CAND_DUP_CHECK_SUMMARY

This table stores the Duplicate check Status summary for a Candidate.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupchecksummary-26805.html#irccanddupchecksummary-26805](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupchecksummary-26805.html#irccanddupchecksummary-26805)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_DUP_CHECK_SUMMARY_PK | DUP_CHK_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DUP_CHK_LOG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Reference PersonId . This is the candidate on whom dup check is being run. Foreign key to irc_candidates. |
| DUP_STRENGTH | VARCHAR2 | 40 |  |  | Indicates the highest category on which a match has been found for the Reference Person Id. This column will be exposed as a DBI in FF This will store one of the values from the LookupCode from the existing LOV "ORA_IRC_CAND_MATCHSCORE":
ORA_HIGHEST - NID match
ORA_HIGHER - 5 columns match
ORA_HIGH - All H categories
ORA_MEDIUM - All M categories
ORA_LOWEST - All L categories. |
| DUP_STRENGTH_COUNT | NUMBER |  | 18 |  | Number of candidates found in the highest match category. |
| STATUS | VARCHAR2 | 40 |  |  | Status of dup check run:
ORA_SUCCESS : if run is successful
ORA_FAILED : if there are any failures during the run. |
| EXCEPTION | CLOB |  |  |  | Error message in case of failure. |
| ES_ENABLED | VARCHAR2 | 1 |  | Yes | Indicates the Engine used when the results were stored in this table:
Y : if Elastic Search is used to run the Dup Check
N : if Sem search is used to run the Dup Check. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Foreign key association with IRC_SUBMISSIONS table. 
One of the three columns required to derive during which CSP, Phase and State a particular Dup Check run was auto-triggered. |
| STATE_ID | NUMBER |  | 18 |  | Foreign Key association with IRC_STATES_B.
One of the three columns required to derive during which CSP, Phase and State a particular Dup Check run was auto-triggered. |
| PHASE_ID | NUMBER |  | 18 |  | Foreign Key association with IRC_PHASES_B.
One of the three columns required to derive during which CSP, Phase and State a particular Dup Check run was auto-triggered. |
| REQUESTED_BY | VARCHAR2 | 64 |  | Yes | Indicates the user who initiated the Dup Check Run. |
| REQUESTED_ON | TIMESTAMP |  |  | Yes | Indicates the date and time when the Dup Check Run was initiated. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_DUP_CHECK_SUMMARY_FK1 | Unique | Default | PERSON_ID |
| IRC_CAND_DUP_CHECK_SUMMARY_FK2 | Non Unique | Default | SUBMISSION_ID |
| IRC_CAND_DUP_CHECK_SUMMARY_FK3 | Non Unique | Default | STATE_ID |
| IRC_CAND_DUP_CHECK_SUMMARY_FK4 | Non Unique | Default | PHASE_ID |
| IRC_CAND_DUP_CHECK_SUMMARY_PK | Unique | Default | DUP_CHK_LOG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
