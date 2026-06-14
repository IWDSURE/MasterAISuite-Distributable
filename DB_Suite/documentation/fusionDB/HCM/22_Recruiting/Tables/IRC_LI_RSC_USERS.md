# IRC_LI_RSC_USERS

Stores the recruiter mapping between ORC and LinkedIn

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscusers-8315.html#irclirscusers-8315](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirscusers-8315.html#irclirscusers-8315)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_RSC_USERS_PK | RSC_USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RSC_USER_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_PERSONS |
| LI_PERSON_URN | VARCHAR2 | 100 |  | Yes | LinkedIn Person Identifier, used to find user by foreign Id. |
| LI_SEAT_URN | VARCHAR2 | 100 |  |  | LinkedIn Recruiter Seat Identifier, used to find user by foreign Id. |
| LI_FIRST_NAME | VARCHAR2 | 150 |  |  | First name of the LinkedIn Recruiter |
| LI_LAST_NAME | VARCHAR2 | 150 |  |  | Last name of the LinkedIn Recruiter |
| LI_ACTIVE_FLAG | VARCHAR2 | 1 |  |  | Indicates if the recruiter is active in LinkedIn |
| LI_ADMIN_FLAG | VARCHAR2 | 1 |  |  | Indicates if the recruiter is a admin among recuiter seatholders |
| LI_PERSON_EMAIL | VARCHAR2 | 240 |  |  | Email address of the recruiter in LinkedIn |
| CONTRACT_ID | NUMBER |  | 18 |  | Foreign key to IRC_LI_CONTRACTS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_INMAIL_SYNC_DATE | TIMESTAMP |  |  |  | Indicates the date and time linkedin inmail was last received. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_RSC_USERS_FK1 | Non Unique | Default | PERSON_ID |
| IRC_LI_RSC_USERS_FK2 | Non Unique | Default | CONTRACT_ID |
| IRC_LI_RSC_USERS_N1 | Non Unique | Default | LI_SEAT_URN |
| IRC_LI_RSC_USERS_N2 | Non Unique | Default | LI_PERSON_URN |
| IRC_LI_RSC_USERS_PK | Unique | Default | RSC_USER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
