# IRC_ACCESS_TOKENS

This table contains Access Codes for external candidates accessing their information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaccesstokens-26208.html#ircaccesstokens-26208](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaccesstokens-26208.html#ircaccesstokens-26208)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCESS_TOKEN_ID | NUMBER |  | 18 | Yes | Identifier of the token or access code. System generated value. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIRMED_FLAG | VARCHAR2 | 1 |  |  | The flag field that identifies if the access code is for a confirmed candidate. |
| ACCESS_CODE | VARCHAR2 | 200 |  |  | Access code to validate that candidate owns e-mail address. |
| ACCESS_CODE_EXP_DATE | TIMESTAMP |  |  |  | Expiration date and time for the access code |
| TOKEN | VARCHAR2 | 1024 |  |  | Encrypted verification token, stored to log that it has been used. |
| TOKEN_EXP_DATE | TIMESTAMP |  |  |  | Expiration date extracted from the token |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Candidate's email address for whom the access code was generated. |
| PHONE_NUMBER | VARCHAR2 | 240 |  |  | Candidate's phone number for whom the Access Code was generated. |
| PROPOSED_CAND_NUM | VARCHAR2 | 30 |  |  | Proposed number to be used for the new candidate. |
| PERSON_ID | NUMBER |  | 18 |  | Identifier of the candidate to whom Access Code refers. |
| SUBMISSION_COUNT | NUMBER |  | 18 |  | Counts the number of submissions made with the access code. |
| SOURCE_TRACKING_ID | NUMBER |  | 18 |  | Identifier of the source tracking information related to the Access Code. |
| URL_SHORT_CODE | VARCHAR2 | 10 |  |  | Short representation of the URL fragment found in TARGET column. |
| URL_START_DATE | TIMESTAMP |  |  |  | Start date and time of validity for the URL. |
| SIGNIN_START_DATE | TIMESTAMP |  |  |  | Start date and time of validity for the login attempt. |
| URL_EXP_DATE | TIMESTAMP |  |  |  | End date and time of validity for the URL. |
| TARGET | VARCHAR2 | 1000 |  |  | Full URL fragment represented by the URL_SHORT_CODE. |
| CONSUMER_ATTRIBUTES | VARCHAR2 | 1000 |  |  | Name and value pairs needed by the consumer of the Short URL. |
| CHALLENGE_REQUIRED | VARCHAR2 | 30 |  |  | Indicates what kind of challenge will be required for visitor to the URL. |
| CONSUMER | VARCHAR2 | 30 |  |  | Indicates which Consumer feature is using this URL. |
| SHORT_CODE | NUMBER |  | 6 |  | The Short Code sent to the candidate for further verification. |
| SHORT_CODE_EXP_DATE | TIMESTAMP |  |  |  | Expiration date and time for the Short Code. |
| FAILED_VALIDATION_COUNT | NUMBER |  | 2 |  | Counts the number of failed attempts at verifying the Short Code |
| FAILED_SIGNIN_COUNT | NUMBER |  | 2 |  | Counts the number of failed attempts to login. |
| DEVICE | VARCHAR2 | 64 |  |  | An identifier for the browser associated to the row. |
| PERSISTENT_ACCESS_FLAG | VARCHAR2 | 1 |  |  | Indicates if the row can be used to provide recurring access. |
| LAST_ACCESS_REAUTH_DATE | TIMESTAMP |  |  |  | The last date the user authenticated to the system for persisted access. |
| LAST_ACCESS_REFRESH_DATE | TIMESTAMP |  |  |  | The last date the user renewed their access to the system for persisted access. |
| PHONE_CHANNEL_TYPE | VARCHAR2 | 30 |  |  | Indicates if the phone login uses WhatsApp or another communication channel |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_ACCESS_TOKENS_N1 | Non Unique | Default | ACCESS_CODE |  |
| IRC_ACCESS_TOKENS_N2 | Non Unique | FUSION_TS_TX_DATA | TOKEN |  |
| IRC_ACCESS_TOKENS_N3 | Non Unique | Default | URL_SHORT_CODE, SHORT_CODE |  |
| IRC_ACCESS_TOKENS_N4 | Non Unique | Default | PERSON_ID |  |
| IRC_ACCESS_TOKENS_N6 | Non Unique | Default | PHONE_NUMBER |  |
| IRC_ACCESS_TOKENS_N7 | Non Unique | Default | UPPER("PROPOSED_CAND_NUM"), URL_SHORT_CODE |  |
| IRC_ACCESS_TOKENS_N8 | Non Unique | Default | UPPER("EMAIL_ADDRESS") |  |
| IRC_ACCESS_TOKENS_N9 | Non Unique | Default | LAST_UPDATE_DATE |  |
| IRC_ACCESS_TOKENS_PK | Unique | FUSION_TS_TX_DATA | ACCESS_TOKEN_ID |  |
| IRC_ACCESS_TOKENS_UK1 | Unique | Default | ACCESS_CODE, ACCESS_CODE_EXP_DATE, PERSON_ID, URL_SHORT_CODE, SHORT_CODE, SHORT_CODE_EXP_DATE | Obsolete |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
