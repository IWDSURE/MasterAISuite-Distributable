# PER_LDAP_ROLE_MEMBERSHIPS

Table for storing one record for each Role Membership to be processed in OIM when creating new users, maintaining the roles allocated to a user or terminating a users employment

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldaprolememberships-14723.html#perldaprolememberships-14723](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldaprolememberships-14723.html#perldaprolememberships-14723)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDAP_ROLE_MEMBERSHIPS_PK | LDAP_ROLE_MEMBERSHIP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDAP_ROLE_MEMBERSHIP_ID | NUMBER |  | 18 | Yes | Mandatory primary key. Updatable while new key generation. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LDAP_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign key to LDAP request. Mandatory. Updatable while new mandatory foreign key generation. |
| REQUEST_TYPE | VARCHAR2 | 30 |  | Yes | The type of request to perform: ADD, REMOVE |
| REQUEST_STATUS | VARCHAR2 | 30 |  | Yes | The current status of role membership portion request: REQUEST, IN PROGRESS, COMPLETE, REJECTED |
| ROLE_GUID | VARCHAR2 | 64 |  | Yes | The role Guid of the role to be added/removed from the user |
| METHOD_CODE | VARCHAR2 | 30 |  | Yes | Whether the role membership request is automatic or manual |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REQUESTOR_USER_GUID | VARCHAR2 | 64 |  |  | The user Guid of the user who is making the LDAP request (if available) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MEMBERSHIP_TYPE | VARCHAR2 | 30 |  |  | MEMBERSHIP_TYPE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LDAP_ROLE_MBRSHPS_FK1 | Non Unique | FUSION_TS_TX_DATA | LDAP_REQUEST_ID |
| PER_LDAP_ROLE_MBRSHPS_N1 | Non Unique | FUSION_TS_TX_DATA | REQUEST_ID |
| PER_LDAP_ROLE_MBRSHPS_PK | Unique | FUSION_TS_TX_DATA | LDAP_ROLE_MEMBERSHIP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
