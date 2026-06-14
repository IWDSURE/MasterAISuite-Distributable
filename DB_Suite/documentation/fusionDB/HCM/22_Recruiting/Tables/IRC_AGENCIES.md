# IRC_AGENCIES

The IRC_AGENCIES will store the external Agency information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircagencies-20166.html#ircagencies-20166](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircagencies-20166.html#ircagencies-20166)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AGENCIES_PK | AGENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENCY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| AGENCY_NAME | VARCHAR2 | 240 |  |  | Column to store Name for Agency. |
| AGENCY_EMAIL | VARCHAR2 | 240 |  |  | Stores Email contact of the Agency. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the Agency as a lookup code. The corresponding lookup type is ORA_IRC_AGENCY_STATUS. |
| AGENCY_CONTACT | VARCHAR2 | 240 |  |  | Stores contact details of the Agency. |
| AGENCY_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of the Agency as a lookup code. The corresponding lookup type is ORA_IRC_AGENCY_TYPE. |
| CONTRACT_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the contact type of the Agency as a lookup code. The corresponding lookup type is ORA_AG_CONTRACT_TYPE. |
| AGENCY_NOTES | VARCHAR2 | 1000 |  |  | Stores additional notes for the Agency. |
| EMBARGO_PERIOD_CODE | VARCHAR2 | 30 |  |  | Stores the Embargo Period of the Agency as a lookup code. The corresponding lookup type is ORA_IRC_EMBARGO_PERIOD. |
| INACTIVATION_DATE | DATE |  |  |  | Stores inactivation date of the Agency. |
| DELETION_DATE | DATE |  |  |  | Stores deletion date of the Agency. |
| CREATE_JA_FLAG | VARCHAR2 | 1 |  |  | Flag to determine if the Agent can create a Job application for Candidate. |
| CAND_INTERNAL_SEARCH_FLAG | VARCHAR2 | 1 |  |  | Flag to determine if the Agent can search for the internal candidates. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AGENCIES_U1 | Unique | Default | AGENCY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
