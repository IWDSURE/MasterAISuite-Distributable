# PER_USER_HISTORY

Table for storing the history of a user record (changes to username and GUID over time)

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peruserhistory-31152.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peruserhistory-31152.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_USER_HISTORY_PK | USER_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_HISTORY_ID | NUMBER |  | 18 | Yes | Mandatory primary key updatable while new key generation |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| USER_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_USERS table. |
| USERNAME | VARCHAR2 | 100 |  | Yes | The latest username of the user active between the start and end dates. |
| USER_GUID | VARCHAR2 | 64 |  | Yes | The userGuid of the user active between the start and end dates. |
| START_DATE | DATE |  |  | Yes | The date that the user Guid/username combination is active from. |
| END_DATE | DATE |  |  |  | The date that the user Guid/username combination is active to. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PERSON_ID | NUMBER |  | 18 |  | The latest person_id of the user active between the start and end dates. |
| PARTY_ID | NUMBER |  | 18 |  | The latest party_id of the user active between the start and end dates. |
| LAST_UPDATE_COMPONENT | VARCHAR2 | 64 |  |  | The Component that last modified the user history record. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_USER_HISTORY_FK1 | Non Unique | FUSION_TS_TX_DATA | USER_ID |
| PER_USER_HISTORY_N1 | Non Unique | FUSION_TS_TX_DATA | USER_GUID |
| PER_USER_HISTORY_N2 | Non Unique | FUSION_TS_TX_DATA | USERNAME |
| PER_USER_HISTORY_N3 | Non Unique | FUSION_TS_TX_DATA | SUBSTR("USERNAME", 1, 64) |
| PER_USER_HISTORY_U1 | Unique | FUSION_TS_TX_DATA | USER_HISTORY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
