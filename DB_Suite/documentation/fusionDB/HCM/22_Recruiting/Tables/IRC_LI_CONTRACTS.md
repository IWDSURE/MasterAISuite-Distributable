# IRC_LI_CONTRACTS

Stores the contract details for LinkedIn integrations in Recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclicontracts-6891.html#irclicontracts-6891](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclicontracts-6891.html#irclicontracts-6891)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_CONTRACTS_PK | CONTRACT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTRACT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| LI_CONTRACT_ID | VARCHAR2 | 100 |  | Yes | Stores the identifier representing the contract in LinkedIn |
| LI_CONTRACT_NAME | VARCHAR2 | 500 |  |  | Stores the name of the contract in LinkedIn |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_NOTE_SYNC_DATE | TIMESTAMP |  |  |  | Indicates the date and time prospect notes were last received from LinkedIn on this recruiter contract |
| LAST_INMAIL_SYNC_DATE | TIMESTAMP |  |  |  | Indicates the date and time InMails were last received from LinkedIn on this recruiter contract |
| LAST_INMAIL_PROF_SYNC_DATE | TIMESTAMP |  |  |  | Indicates the date and time InMail Stub Profiles were last received from LinkedIn on this recruiter contract |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_CONTRACTS_PK | Unique | Default | CONTRACT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
