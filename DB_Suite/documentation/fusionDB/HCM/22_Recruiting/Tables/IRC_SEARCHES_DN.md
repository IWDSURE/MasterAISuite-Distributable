# IRC_SEARCHES_DN

The denomalised table for IRC_SEARCHES to be used for the purpose of reporting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchesdn-11077.html#ircsearchesdn-11077](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchesdn-11077.html#ircsearchesdn-11077)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCHES_DN_PK | SEARCHDN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCHDN_ID | NUMBER |  |  | Yes | The primary key of the table. Foreign referenced to IRC_SEARCHES. |
| FILTER_REHIRE_RECOMMENDATION | VARCHAR2 | 200 |  |  | The filter type values selected for rehire recommendation during candidate search. |
| FILTER_ASSESSMENT_PACKAGE | VARCHAR2 | 2000 |  |  | The filter type values selected for assessment package during candidate search. |
| FILTER_ASSESSMENT_RESULT | VARCHAR2 | 200 |  |  | The filter type values selected for assessment result during candidate search. |
| FILTER_ASSESSMENT_PERCENTILE | VARCHAR2 | 200 |  |  | The filter type values selected for assessment percentile during candidate search. |
| FILTER_ASSESSMENT_SCORE | VARCHAR2 | 1000 |  |  | The filter type values selected for assessment score during candidate search. |
| FILTER_ASSESSMENT_BAND | VARCHAR2 | 1000 |  |  | The filter type values selected for assessment band during candidate search. |
| FILTER_CITIZENSHIP | VARCHAR2 | 1000 |  |  | The filter type values selected for citizenship during candidate search. |
| SEARCH_ID | NUMBER |  |  | Yes | The foregin reference search ID from IRC_SEARCHES. |
| SEARCH_KEYWORDS | VARCHAR2 | 4000 |  |  | The search keyword or search string that was entered by the user. |
| SEARCH_BY_RESUME_FLAG | VARCHAR2 | 1 |  |  | Stores whether search is performed includes resume. |
| SEARCH_BY_EMAIL_FLAG | VARCHAR2 | 1 |  |  | Stores whether search is performed using email contact info or not. |
| SEARCH_MODE | VARCHAR2 | 200 |  |  | Stores the mode selected during candidate search. |
| SEARCH_BY_PHONE_FLAG | VARCHAR2 | 1 |  |  | Stores whether search is performed using phone contact info or not. |
| FILTER_LABEL | VARCHAR2 | 800 |  |  | The filter type values selected for label during candidate search. |
| FILTER_OPT_IN_MKT_EMAILS_PREF | VARCHAR2 | 300 |  |  | The filter type values selected for Marketing Emails Preference during candidate search. |
| FILTER_CANDIDATE_TYPE | VARCHAR2 | 200 |  |  | The filter type values selected for candidate type during candidate search. |
| FILTER_LOCATIONS | VARCHAR2 | 800 |  |  | The filter type values selected for locations during candidate search. |
| FILTER_DEGREES | VARCHAR2 | 800 |  |  | The filter type values selected for degrees during candidate search. |
| FILTER_COMPANIES | VARCHAR2 | 800 |  |  | The filter type values selected for companies during candidate search. |
| FILTER_YEARS_OF_EXP | VARCHAR2 | 200 |  |  | The filter type values selected for years of experience during candidate search. |
| FILTER_LAST_UPDATED_DATE | VARCHAR2 | 200 |  |  | The filter type values selected for candidate last updated date during candidate search. |
| PRECRITERIA_CAND_DETAILS | VARCHAR2 | 1000 |  |  | The pre criteria values selected for details during candidate search. |
| PRECRITERIA_LOCATION | VARCHAR2 | 1000 |  |  | The pre criteria values selected for location during candidate search. |
| PRECRITERIA_EDUCATION | VARCHAR2 | 1000 |  |  | The pre criteria values selected for education during candidate search. |
| PRECRITERIA_EXPERIENCE | VARCHAR2 | 1000 |  |  | The pre criteria values selected for experience during candidate search. |
| PRECRITERIA_COMPANY | VARCHAR2 | 1000 |  |  | The pre criteria values selected for company during candidate search. |
| FILTER_BASIC_INFO | VARCHAR2 | 1000 |  |  | The filter type values selected for basic info during candidate search. |
| FILTER_SOURCE | VARCHAR2 | 1000 |  |  | The filter type values selected for source during candidate search. |
| FILTER_SOURCE_MEDIUM | VARCHAR2 | 1000 |  |  | The filter type values selected for source medium during candidate search. |
| FILTER_POOL | VARCHAR2 | 1000 |  |  | The filter type values selected for pool during candidate search. |
| FILTER_LANGUAGE | VARCHAR2 | 1000 |  |  | The filter type values selected for language during candidate search. |
| FILTER_LICENSE | VARCHAR2 | 1000 |  |  | The filter type values selected for license during candidate search. |
| FILTER_JOB | VARCHAR2 | 1000 |  |  | The filter type values selected for job during candidate search. |
| FILTER_SKILL | VARCHAR2 | 1000 |  |  | The filter type values selected for skill during candidate search. |
| FILTER_REQUISITION | VARCHAR2 | 1000 |  |  | The filter type values selected for the requisition during candidate search. |
| FILTER_INTERACTIONS_TYPE | VARCHAR2 | 1000 |  |  | The filter type values selected for the interactions type code during candidate search. |
| FILTER_INTERACTIONS_DATE | VARCHAR2 | 200 |  |  | The filter type values selected for the interactions date during candidate search. |
| FILTER_EVENT | VARCHAR2 | 1000 |  |  | The filter type values selected for the events during candidate search. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCHES_DN_N1 | Non Unique | Default | SEARCH_ID |
| IRC_SEARCHES_DN_U1 | Unique | Default | SEARCHDN_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
