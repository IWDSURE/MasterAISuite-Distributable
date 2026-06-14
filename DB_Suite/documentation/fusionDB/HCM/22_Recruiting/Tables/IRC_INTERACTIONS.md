# IRC_INTERACTIONS

This table stores the interaction for a person in the context of a Submission, Candidate Pool and Candidate General Profile.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircinteractions-4284.html#ircinteractions-4284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircinteractions-4284.html#ircinteractions-4284)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_INTERACTIONS_PK | INTERACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERACTION_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| PERSON_ID | NUMBER |  | 18 |  | Stores ID of the person for whom the Interaction note is added |
| ADDED_BY_PERSON_ID | NUMBER |  | 18 | Yes | Stores ID of the person creating the interaction |
| CONTEXT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the context. Submission, Pool, General Profile etc. Lookup type is ORA_IRC_INTERACTION_CTXT_TYPE |
| CONTEXT_ID | NUMBER |  | 18 | Yes | Stores the ID of the context object ??? Reference to SUBMISSION_ID or POOL_ID or PERSON_ID(In case of General Profile) etc |
| SUB_CONTEXT_ID | VARCHAR2 | 100 |  |  | added for tracking LinkedIn InMail session.  Every session will have the same SubContextId so they could be displayed together as interactions. |
| INTERACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the interaction type. Email, Phone, In Person etc. This is a lookup. Lookup type ORA_IRC_INTERACTION_TYPE |
| INTERACTION_DATE | DATE |  |  | Yes | Stores the date when the interaction happened. |
| TEXT | CLOB |  |  |  | Stores the text for this interaction. |
| MASKED_BODY_TEXT | CLOB |  |  |  | Store the body text without PII data |
| HIRING_TEAM_INTR_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate whether the current interaction entry was sent to hiring team |
| SUBJECT | VARCHAR2 | 1000 |  |  | Stores the subject for this interaction. |
| MESSAGE_IDENTIFIER | VARCHAR2 | 400 |  |  | Contains the message identifier for both email and SMS. For email stores the UMS SMTP message id and for SMS stores the id sent by the provider. |
| MESSAGE_STATUS | VARCHAR2 | 100 |  |  | Stores the status of the message |
| CONTENT_LIBRARY_ITEM_CODE | VARCHAR2 | 30 |  |  | The Recruiting Content Library's DESCRIPTION_CODE that points to the table IRC_DESCRIPTIONS_B. |
| RESEND_ALLOWED_STATUS | VARCHAR2 | 1 |  |  | Status controls the resend ability of the interaction |
| CONTENT_LIBRARY_ITEM_ID | NUMBER |  | 18 |  | Contains the content library item identifier associated to the interaction. Foreign key to the table irc_descriptions_b |
| CHANNEL_TEMPLATE_ID | NUMBER |  | 18 |  | Contains the channel specific template identifier associated to the interaction |
| INTERACTION_SUB_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores additional details about the interaction type, such as whether the interaction was initiated by the user or the agent/system. |
| REFERENCE_INFORMATION | VARCHAR2 | 240 |  |  | Stores additional reference information, such as a candidate's phone number, for the visitor use case. |
| REFERENCE_ID | NUMBER |  | 18 |  | Stores an additional reference ID, such as a visitor ID, for the visitor use case. |
| SUB_REFERENCE_ID | VARCHAR2 | 240 |  |  | Stores additional sub-reference information, such as an agent conversation id. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_INTERACTIONS_FK2 | Non Unique | Default | ADDED_BY_PERSON_ID |
| IRC_INTERACTIONS_FK3 | Non Unique | Default | CONTENT_LIBRARY_ITEM_ID |
| IRC_INTERACTIONS_N1 | Non Unique | Default | PERSON_ID, CONTEXT_ID, CONTEXT_TYPE_CODE |
| IRC_INTERACTIONS_N2 | Non Unique | Default | SUB_CONTEXT_ID |
| IRC_INTERACTIONS_N3 | Non Unique | Default | CONTEXT_TYPE_CODE, CONTEXT_ID |
| IRC_INTERACTIONS_N4 | Non Unique | Default | MESSAGE_IDENTIFIER |
| IRC_INTERACTIONS_N5 | Non Unique | Default | INTERACTION_DATE, INTERACTION_TYPE_CODE |
| IRC_INTERACTIONS_N6 | Non Unique | Default | PERSON_ID, INTERACTION_TYPE_CODE, INTERACTION_SUB_TYPE_CODE, ADDED_BY_PERSON_ID |
| IRC_INTERACTIONS_N7 | Non Unique | Default | REFERENCE_INFORMATION, INTERACTION_TYPE_CODE, INTERACTION_SUB_TYPE_CODE, ADDED_BY_PERSON_ID |
| IRC_INTERACTIONS_N8 | Non Unique | Default | REFERENCE_ID, INTERACTION_TYPE_CODE, INTERACTION_SUB_TYPE_CODE, ADDED_BY_PERSON_ID |
| IRC_INTERACTIONS_PK | Unique | Default | INTERACTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
