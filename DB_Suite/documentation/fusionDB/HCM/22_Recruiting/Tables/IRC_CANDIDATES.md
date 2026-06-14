# IRC_CANDIDATES

This table contains candidates.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandidates-29033.html#irccandidates-29033](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandidates-29033.html#irccandidates-29033)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CANDIDATES_PK | PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | Primary key of the table and also foreign Key to PER_PERSONS. |  |
| CAND_ADDRESS_ID | NUMBER |  | 18 |  | This Column is used to point to the address row of the candidate |  |
| OBJECT_STATUS | VARCHAR2 | 40 |  |  | Indicates the status of the object. |  |
| CANDIDATE_NUMBER | VARCHAR2 | 30 |  | Yes | Unique readable number generated for Candidate. |  |
| POTENTIAL_DUPLICATE_FLAG | VARCHAR2 | 1 |  |  | This flag is used to determine whether profile is a possible duplicate or not. |  |
| PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to profiles table HRT_PROIFLES_B. |  |
| CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | This Flag is used to determine whether candidate is a verified or unverified. |  |
| CONFIRMED_DATE | TIMESTAMP |  |  |  | Stores the date and time of candidate confirmation. |  |
| VISIBLE_TO_CANDIDATE_FLAG | VARCHAR2 | 1 |  |  | This flag is used to determine whether candidate has access to his/her profile information or not. |  |
| ADDED_BY_FLOW_CODE | VARCHAR2 | 30 |  |  | This column gives details about which business flow created the candidate. |  |
| AVAILABILITY_DATE | DATE |  |  |  | Date the candidate is available. |  |
| SEARCH_DATE | DATE |  |  |  | Stores the search date for this candidate. |  |
| PREF_PHONE_CNT_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the preferred phone contact type for this candidate Ex: Home/Mobile/Work |  |
| CAND_LAST_MODIFIED_DATE | TIMESTAMP |  |  |  | Stores the last modified date for the Candidate. This is updated even when the child entitiies of the Candidate table are updated. This can be used by customers to export candidates which were updated after a certain date. |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| CAND_PREF_LANGUAGE_CODE | VARCHAR2 | 4 |  |  | Stores the code of the candidate's preferred language. |  |
| CAND_PREF_TIME_ZONE | VARCHAR2 | 64 |  |  | Stores the preferred timezone of the candidate. |  |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |  |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |  |
| OPT_IN_MKT_EMAILS_FLAG | VARCHAR2 | 1 |  |  | Stores whether the candidate has opted-in or opted-our for receiving marketing emails. Null value means unspecified. |  |
| OPT_IN_MKT_EMAILS_DATE | TIMESTAMP |  |  |  | Stores the date and time at which the candidate updated this preference of whether to receive or not recruiting marketing emails. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MERGED_FLAG | VARCHAR2 | 1 |  |  | Stores if the candidate has merged data or not. If Y then candidate is alpha and has merged data. |  |
| DELETION_QUALIFIER | VARCHAR2 | 64 |  |  | Stores the reason for deletion. Used to differentiate if candidate was merged because of right to be forgotten or merge scenario. For merge, value will be CAND_MERGE. |  |
| DELETED_BY_USER | VARCHAR2 | 64 |  |  | Indicates the user who deleted the row. |  |
| DELETION_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the deletion of the row. |  |
| EMAIL_VERIFIED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the candidate's preferred email address is verified or not. |  |
| EMAIL_PREFERRED_FLAG | VARCHAR2 | 1 |  |  | This flag indicates whether the candidate requested email as the preferred means of communication. |  |
| CAND_EMAIL_ID | NUMBER |  | 18 |  | Foreign Key to PER_EMAIL_ADDRESSES table. If the candidate has specified a preferred Email, this column is used to store a pointer to the Email address row. |  |
| PHONE_VERIFIED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether the candidate's preferred phone number is verified or not. |  |
| PHONE_PREFERRED_FLAG | VARCHAR2 | 1 |  |  | This flag indicates whether the candidate requested phone as the preferred means of communication. |  |
| CAND_PHONE_ID | NUMBER |  | 18 |  | Foreign Key to PER_PHONES table. If the candidate has specified a preferred Phone, this column is used to store a pointer to the Phone row. |  |
| PHONE_CHANNEL_TYPE | VARCHAR2 | 30 |  |  | Indicates the type of phone channel. |  |
| REHIRE_RECOMMENDATION | VARCHAR2 | 30 |  |  | Indicates whether candidate is recommendated for being rehired. This is a denormalized column derived from PER_PERIODS_OF_SERVICE.REHIRE_RECOMMENDATION. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CANDIDATES_FK2 | Non Unique | Default | CAND_EMAIL_ID |
| IRC_CANDIDATES_FK3 | Non Unique | Default | CAND_PHONE_ID |
| IRC_CANDIDATES_N1 | Non Unique | Default | DELETION_QUALIFIER |
| IRC_CANDIDATES_N2 | Non Unique | Default | CAND_LAST_MODIFIED_DATE |
| IRC_CANDIDATES_N3 | Non Unique | Default | UPPER("CANDIDATE_NUMBER") |
| IRC_CANDIDATES_PK | Unique | Default | PERSON_ID |
| IRC_CANDIDATES_UK1 | Unique | Default | CANDIDATE_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
