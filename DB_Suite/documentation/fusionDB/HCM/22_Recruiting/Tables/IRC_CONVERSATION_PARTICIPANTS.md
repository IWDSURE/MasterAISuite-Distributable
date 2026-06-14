# IRC_CONVERSATION_PARTICIPANTS

This table stores the participants of a conversation between recruiters & hiring managers and the candidate on an interaction. Different participants can span different email messages, so this table stores all of the individuals who are part of the entire conversation on an interaction.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircconversationparticipants-20591.html#ircconversationparticipants-20591](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircconversationparticipants-20591.html#ircconversationparticipants-20591)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CONV_PARTICIPANTS_PK | CONVERSATION_PARTICIPANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONVERSATION_PARTICIPANT_ID | NUMBER |  | 18 | Yes | Primary key for IRC_CONVERSATION_PARTICIPANTS table. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key into PER_PERSONS. PersonId for the candidate or recruiter/ hiring manager that is part of the conversation. |
| INTERACTION_ID | NUMBER |  | 18 | Yes | Foreign key into IRC_INTERACTIONS. Unique identifier for the interaction (and thus conversation) that is taking place. Filtering by this column will give us the participants/persons that are part of a conversation. |
| IS_CANDIDATE_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether this person is the candidate in the conversation. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CONV_PARTICIPANTS_FK1 | Non Unique | Default | PERSON_ID |
| IRC_CONV_PARTICIPANTS_FK2 | Non Unique | Default | INTERACTION_ID |
| IRC_CONV_PARTICIPANTS_PK | Unique | Default | CONVERSATION_PARTICIPANT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
