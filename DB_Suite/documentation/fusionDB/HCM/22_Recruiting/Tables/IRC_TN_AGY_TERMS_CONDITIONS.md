# IRC_TN_AGY_TERMS_CONDITIONS

This is the table for storing terms and condition details accepted by the agent of the agencies.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnagytermsconditions-28307.html#irctnagytermsconditions-28307](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnagytermsconditions-28307.html#irctnagytermsconditions-28307)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_AGY_TERMS_CONDITIONS_PK | AGENCY_TC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENCY_TC_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| DESC_VERSION_ID | NUMBER |  | 18 | Yes | Stores the description version id. Foreign key to IRC_DESC_VERSIONS_B table. |
| AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agency. Foreign key to IRC_AGENCIES table. |
| AGENT_ID | NUMBER |  | 18 | Yes | Stores the AGENT_ID of the Agency.Foreign key to IRC_AGENTS table. |
| ACCEPTED_DATE | TIMESTAMP |  |  | Yes | Stores the date when agency accepted the terms and conditions. |
| IP_ADDRESS | VARCHAR2 | 30 |  | Yes | Stores the ip address from which agency accepted. |
| ACCEPTED_BY | VARCHAR2 | 240 |  |  | This column stores the name who accepted the terms and conditions. |
| OBJECT_STATUS | VARCHAR2 | 30 |  | Yes | Indicates the status of the object. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_AGY_TERMS_CONDITIONS_PK | Unique | Default | AGENCY_TC_ID |
| IRC_TN_AGY_TERMS_CONDITION_FK1 | Non Unique | Default | DESC_VERSION_ID |
| IRC_TN_AGY_TERMS_CONDITION_FK2 | Non Unique | Default | AGENCY_ID |
| IRC_TN_AGY_TERMS_CONDITION_FK3 | Non Unique | Default | AGENT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
