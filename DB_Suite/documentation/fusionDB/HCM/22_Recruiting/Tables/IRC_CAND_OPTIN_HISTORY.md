# IRC_CAND_OPTIN_HISTORY

Stores history of marketing/job alerts optin by candidates and associated consent data for GDPR compliance.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandoptinhistory-4515.html#irccandoptinhistory-4515](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandoptinhistory-4515.html#irccandoptinhistory-4515)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_OPTIN_HISTORY_PK | HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HISTORY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Candidate who opted for marketing/job alerts. Foreign Key to PER_PERSONS. |
| SITE_NUMBER | VARCHAR2 | 2000 |  |  | Stores the list of sites where the candidate opted for job alerts, pipe delimited. |
| OPT_IN_MKT_EMAILS_FLAG | VARCHAR2 | 1 |  |  | Flag indicating whether the candidate opted for marketing emails. |
| OPT_IN_TC_EMAILS_FLAG | VARCHAR2 | 1 |  |  | Flag indicating whether the candidate opted for job alerts at a site. |
| CAND_TERRITORY_CODE | VARCHAR2 | 2 |  |  | Territory code indicating candidate's country of residence. |
| DOI_EMAIL_SENT_FLAG | VARCHAR2 | 1 |  |  | Flag indicating whether double optin email has been sent to candidate. |
| CONSENT_SUBJECT | CLOB |  |  |  | Stores the subject of the Double Opt-In message sent to the candidate. |
| CONSENT_MESSAGE | CLOB |  |  |  | CONSENT_MESSAGE |
| IP_ADDRESS | VARCHAR2 | 100 |  |  | IP_ADDRESS |
| CONSENT_DATE | TIMESTAMP |  |  |  | Indicates the date and time when the candidate confirmed his Opt-In preferences. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_OPTIN_HISTORY_FK1 | Non Unique | Default | PERSON_ID |
| IRC_CAND_OPTIN_HISTORY_PK | Unique | Default | HISTORY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
