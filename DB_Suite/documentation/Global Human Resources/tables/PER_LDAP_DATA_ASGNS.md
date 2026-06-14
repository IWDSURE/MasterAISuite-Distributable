# PER_LDAP_DATA_ASGNS

Table for storing one record for each data access assignment to be processed

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldapdataasgns-21178.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldapdataasgns-21178.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDAP_DATA_ASGNS_PK | LDAP_DATA_ASGNS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDAP_DATA_ASGNS_ID | NUMBER |  | 18 | Yes | Mandatory primary key. Updatable while new key generation. |
| LDAP_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign key to LDAP request. Mandatory. Updatable while new mandatory foreign key generation. |
| REQUEST_TYPE | VARCHAR2 | 30 |  | Yes | The type of request to perform: ADD, REMOVE |
| REQUEST_STATUS | VARCHAR2 | 30 |  | Yes | The current status of role membership portion request: REQUEST, IN PROGRESS, COMPLETE, REJECTED |
| ROLE_CODE | VARCHAR2 | 240 |  | Yes | The role code of the role to be added/removed from the user |
| METHOD_CODE | VARCHAR2 | 30 |  | Yes | Whether the role membership request is automatic or manual |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| SECURITY_CONTEXT | VARCHAR2 | 256 |  | Yes | Data asscess assignment security context |
| SECURITY_CONTEXT_VALUE | NUMBER |  | 18 | Yes | Data access assignment security context value |
| REQUESTOR_USER_GUID | VARCHAR2 | 64 |  |  | The user Guid of the user who is making the LDAP request (if available) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LDAP_DATA_ASGNS_FK1 | Non Unique | FUSION_TS_TX_DATA | LDAP_REQUEST_ID |
| PER_LDAP_DATA_ASGNS_N1 | Non Unique | FUSION_TS_TX_DATA | REQUEST_ID |
| PER_LDAP_DATA_ASGNS_PK | Unique | FUSION_TS_TX_DATA | LDAP_DATA_ASGNS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
