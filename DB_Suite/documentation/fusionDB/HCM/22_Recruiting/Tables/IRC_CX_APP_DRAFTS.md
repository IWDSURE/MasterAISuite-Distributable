# IRC_CX_APP_DRAFTS

Details of the site themes which is used to customize the look of a site.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxappdrafts-15291.html#irccxappdrafts-15291](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxappdrafts-15291.html#irccxappdrafts-15291)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_APP_DRAFTS_PK | APP_DRAFT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APP_DRAFT_ID | NUMBER |  | 18 | Yes | Identifier of the application draft. System generated value. |
| DRAFT_SOURCE | VARCHAR2 | 240 |  |  | Indicates the source of draft data |
| LAST_ACCESSED_ON | VARCHAR2 | 1000 |  |  | Last user agent used by user to access application draft |
| LEGAL_DESC_VERSION_ID | NUMBER |  | 18 |  | LEGAL_DESCRIPTION_VERSION_ID to save legal description id in rest |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Foreign key to the IRC_CX_SITES_B table. |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REQUISITION_NUMBER | VARCHAR2 | 512 |  | Yes | Requisition number used to identify application draft requisition. |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | Telephone number. Not marked as mandatory in order to always allow creation of a first phone row for every person even when phone number is not provided. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Candidate email address used to identify candidate. |
| COUNTRY_CODE | VARCHAR2 | 30 |  |  | Country code of the Phone Number. |
| AREA_CODE | VARCHAR2 | 30 |  |  | The Area Code of the Phone Number. |
| CONTENT | CLOB |  |  |  | JSON payload with the application draft. |
| CANDIDATE_NUMBER | VARCHAR2 | 240 |  |  | Candidate Number used to get last modified date from Candidates |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_JOB_EXECUTION_DATE | TIMESTAMP |  |  |  | Last execution date of the ESS job needed for idempotency. |
| CONTENT_LANGUAGE | VARCHAR2 | 30 |  |  | Indicates the code of the language into which the contents of the translatable columns are translated. |
| PROPOSED_CAND_NUM | VARCHAR2 | 30 |  |  | Candidate number of the candidate who does not have entry in IRC_CANDIDATES. Needed for Inline Assessments. |
| PREFERRED_CHANNEL | VARCHAR2 | 30 |  |  | Preferred Communication channel for the candidate. It can be E-mail, phone or something else. |
| MODIFICATION_DATE | TIMESTAMP |  |  |  | Date of modification of the record done by the draft REST Service it is not the same as LAST_UPDATE_DATE as we don't want it to be updated every time row is changed. |
| JOB_STATUS | VARCHAR2 | 40 |  | Yes | Status of the row after ESS job was executed it is enumeration of different statuses for example ORA_INVALID, ORA_FIRST_NOTIF_SENT. |
| APPLY_FLOW_ID | NUMBER |  | 18 |  | Identifier of the Request Information Flow. Reference to the IRC_APPLY_FLOWS_B table. |
| SUBMISSION_ID | NUMBER |  | 18 |  | Identifier of the Submission on which Request Information Flow is needed. Reference to the IRC_JA_SECONDARY_FLOWS table. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 |  | Identifier of the Request Information Flow Action Id. Reference to the IRC_JA_SECONDARY_FLOWS table. |
| EXTRA_INFO1 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| EXTRA_INFO2 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| EXTRA_INFO3 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| EXTRA_INFO4 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |
| EXTRA_INFO5 | VARCHAR2 | 1000 |  |  | Attribute to store additional information. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_APP_DRAFTS_FK1 | Non Unique | Default | SITE_NUMBER |
| IRC_CX_APP_DRAFTS_FK2 | Non Unique | Default | SUBMISSION_ID, APPLY_FLOW_ID, STEP_ACTION_USAGE_ID |
| IRC_CX_APP_DRAFTS_FK3 | Non Unique | Default | REQUISITION_NUMBER |
| IRC_CX_APP_DRAFTS_N1 | Non Unique | Default | EMAIL_ADDRESS |
| IRC_CX_APP_DRAFTS_N2 | Non Unique | Default | JOB_STATUS, LAST_JOB_EXECUTION_DATE, MODIFICATION_DATE |
| IRC_CX_APP_DRAFTS_N3 | Non Unique | Default | MODIFICATION_DATE |
| IRC_CX_APP_DRAFTS_N4 | Non Unique | Default | UPPER("REQUISITION_NUMBER") |
| IRC_CX_APP_DRAFTS_N5 | Non Unique | Default | UPPER("EMAIL_ADDRESS") |
| IRC_CX_APP_DRAFTS_N6 | Non Unique | Default | UPPER("CANDIDATE_NUMBER") |
| IRC_CX_APP_DRAFTS_N7 | Non Unique | Default | UPPER("PHONE_NUMBER"), UPPER("COUNTRY_CODE") |
| IRC_CX_APP_DRAFTS_N8 | Non Unique | Default | UPPER("PROPOSED_CAND_NUM") |
| IRC_CX_APP_DRAFTS_N9 | Non Unique | Default | TRANSLATE("COUNTRY_CODE"\|\|"AREA_CODE"\|\|"PHONE_NUMBER",'0123456789'\|\|TRANSLATE("COUNTRY_CODE"\|\|"AREA_CODE"\|\|"PHONE_NUMBER",'x0123456789','x'),'0123456789') |
| IRC_CX_APP_DRAFTS_PK | Unique | Default | APP_DRAFT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
