# IRC_TNETWORK_AGENCY_REQ_INFO

This is the table for storing requisition information requests by an talent network agency on FA/Customer POD.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnetworkagencyreqinfo-14895.html#irctnetworkagencyreqinfo-14895](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnetworkagencyreqinfo-14895.html#irctnetworkagencyreqinfo-14895)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TNETWORK_AGENCY_REQ_PK | REQ_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_INFO_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| AGENCY_ACCEPTANCE_STATUS | VARCHAR2 | 30 |  |  | To store the status of ORA_COMPLETE/ ORA_PENDING_INFO or ORA_REJECTED |
| REDIRECT_URL | VARCHAR2 | 1000 |  |  | Stores the URL for partner owned service |
| COMMENTS | VARCHAR2 | 4000 |  |  | Stores comments added by the Agency. |
| TN_AGENCY_ID | NUMBER |  | 18 | Yes | Stores the AGENCY_ID of the Agent. Reference to Talent network Agency Id. |
| TN_AGENCY_NAME | VARCHAR2 | 240 |  | Yes | Column to store Name for Agency. |
| TN_AGENT_ID | NUMBER |  | 18 | Yes | Stores the AGENT_ID of the Agent. Reference to Talent network Agent id. |
| TN_AGENT_NAME | VARCHAR2 | 240 |  | Yes | Column to store Name for Agent. |
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
| IRC_TNETWORK_AGENCY_REQ_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_TNETWORK_AGENCY_REQ_FK2 | Non Unique | Default | TN_AGENCY_ID |
| IRC_TNETWORK_AGENCY_REQ_FK3 | Non Unique | Default | TN_AGENT_ID |
| IRC_TNETWORK_AGENCY_REQ_PK | Unique | Default | REQ_INFO_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
