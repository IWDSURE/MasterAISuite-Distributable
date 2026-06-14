# IRC_ONBOARDING_OSN

Table for the OSN discussion opened with the candidate onboarding

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irconboardingosn-29837.html#irconboardingosn-29837](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irconboardingosn-29837.html#irconboardingosn-29837)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ONBOARDING_OSN_PK | ONBOARDING_OSN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ONBOARDING_OSN_ID | NUMBER |  | 18 | Yes | Primary key for the OSN Discussion |
| CONVERSATION_TITLE | VARCHAR2 | 250 |  | Yes | Conversation title in OSN |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| START_DATE | DATE |  |  |  | Start Date for a discussion, setting the discussion effectiveness. |
| END_DATE | DATE |  |  |  | End Date for the discussion, invalidating the discussion effectiveness |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ONBOARDING_OSN_U1 | Unique | Default | ONBOARDING_OSN_ID |
| IRC_ONBOARDING_OSN_U2 | Unique | Default | CONVERSATION_TITLE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
