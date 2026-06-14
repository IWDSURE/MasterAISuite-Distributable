# IRC_CX_CNDT_EMAIL_TKNS

Details of the sites which is used to publish the jobs.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxcndtemailtkns-22893.html#irccxcndtemailtkns-22893](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxcndtemailtkns-22893.html#irccxcndtemailtkns-22893)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_CNDT_EMAIL_TKNS_PK | TOKEN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOKEN_ID | NUMBER |  | 18 | Yes | Identifier of the verification token. System generated value. |
| OFFER_ID | NUMBER |  | 18 |  | The offer a user can view when accessing the resource using value of ACCESS_CODE. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TOKEN_VALIDATED | VARCHAR2 | 1 |  |  | The flag field that determines if token has been already validated. |
| ACCESS_CODE | VARCHAR2 | 200 |  |  | Access code to validate that candidate owns e-mail address.  In validation response system returns accessCode that can be used to authorise the REST services for candidate, attachment and submission creation |
| VERIFICATION_TOKEN | VARCHAR2 | 200 |  | Yes | Unique code for the verification token. Generated in the application. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  | Yes | User's email address for whom token was generated. |
| LAST_NAME | VARCHAR2 | 240 |  |  | Last name of a candidate for whom token was generated. |
| TOKEN_EXPIRATION_DATE | TIMESTAMP |  |  | Yes | Date till generated token is valid. |
| ACCESS_CODE_EXP_DATE | TIMESTAMP |  |  |  | Expiration date and time for the acesss code. |
| CANDIDATE_NUMBER | VARCHAR2 | 240 |  |  | Unique readable number generated for Candidate. |
| NEXT_PERSON_ID | NUMBER |  | 18 |  | Identifier of the Candidate record that will be created. System generated value. |
| SUBMISSION_COUNT | NUMBER |  | 18 |  | Count the number of submissions made with the Access Code. |
| AF_VERSION_ID | NUMBER |  | 18 |  | Identifier of the version of the Apply Flow configuration for the Access Code. |
| LEGAL_DESC_VERSION_ID | NUMBER |  | 18 |  | Identifier of the version of the Legal Description for the Access Code. |
| ESIGN_DESC_VERSION_ID | NUMBER |  | 18 |  | Identifier of the version of the Esign Description for the Access Code. |
| SOURCE_TRACKING_ID | NUMBER |  | 18 |  | Identifier of the combination of source tracking attributes for the related Access Code. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_CNDT_EMAIL_TKNS_FK1 | Non Unique | Default | OFFER_ID |
| IRC_CX_CNDT_EMAIL_TKNS_N2 | Non Unique | Default | ACCESS_CODE, ACCESS_CODE_EXP_DATE |
| IRC_CX_CNDT_EMAIL_TKNS_PK | Unique | Default | TOKEN_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
