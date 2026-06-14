# IRC_CAMP_MSTEAMS_INTG_USERS

Table to store the MS Teams Integration user details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampmsteamsintgusers-30192.html#irccampmsteamsintgusers-30192](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampmsteamsintgusers-30192.html#irccampmsteamsintgusers-30192)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_MSTEAMS_INTG_USERS_PK | CAMP_MSTEAMS_INTG_USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_MSTEAMS_INTG_USER_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| APPLICATION_NAME | VARCHAR2 | 255 |  | Yes | Stores the application name for the integration user. |
| USERNAME | VARCHAR2 | 255 |  | Yes | Stores the identifier for the integration user, which may be a username, UPN, or service principal. |
| TENANT_ID | VARCHAR2 | 100 |  | Yes | Stores customer tenant guid of Microsoft azure. |
| APP_ID | VARCHAR2 | 100 |  | Yes | Stores the Microsoft Azure app registration ID (client ID). |
| APP_AUTHENTICATION_TYPE | VARCHAR2 | 30 |  | Yes | Stores the authentication method used by the application |
| APP_CREDENTIAL_REF | VARCHAR2 | 255 |  | Yes | Reference to credential in Recruiting credential store |
| USER_STATUS | VARCHAR2 | 30 |  | Yes | Indicate the User deleted from FSM. either ORA_ACTIVE or ORA_DELETE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_MSTEAMS_INTG_USERS_PK | Unique | Default | CAMP_MSTEAMS_INTG_USER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
