# IRC_CAND_DUP_CHECK_DETAILS

This table stores the details of duplicate candidates found in the system for a Candidate.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupcheckdetails-17210.html#irccanddupcheckdetails-17210](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupcheckdetails-17210.html#irccanddupcheckdetails-17210)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_DUP_CHECK_DETAILS_PK | DUP_CHK_RESULTS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DUP_CHK_RESULTS_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| DUP_CHK_LOG_ID | NUMBER |  | 18 | Yes | Foreign Key association with IRC_CAN_DUP_CHECK_SUMMARY. |
| PERSON_ID | NUMBER |  | 18 | Yes | Reference PersonId . This is the candidate on whom dup check is being run. Foreign key to irc_candidates. |
| DUP_PERSON_ID | NUMBER |  | 18 | Yes | Reference PersonId . This is the candidate which was returned as a duplicate of the PERSON_ID. Foreign key to irc_candidates. |
| NID_MATCH | VARCHAR2 | 1 |  | Yes | Indicates whether there was a NID match between reference candidate and the duplicate candidate. |
| DOB_MATCH | VARCHAR2 | 1 |  | Yes | Indicates whether there was a DOB match between reference candidate and the duplicate candidate. |
| GROUP_CODE | VARCHAR2 | 3 |  |  | Indicates the Group Code against which the candidate and duplicate candidate were matched upon. It can contain any of the following values : HH for NID match, Hx for all High matches, Mx for all Medium matches and Lx for all Low matches. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_DUP_CHECK_DETAILS_FK1 | Non Unique | Default | DUP_CHK_LOG_ID |
| IRC_CAND_DUP_CHECK_DETAILS_FK2 | Non Unique | Default | PERSON_ID |
| IRC_CAND_DUP_CHECK_DETAILS_FK3 | Non Unique | Default | DUP_PERSON_ID |
| IRC_CAND_DUP_CHECK_DETAILS_PK | Unique | Default | DUP_CHK_RESULTS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
