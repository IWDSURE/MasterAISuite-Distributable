# PER_LDAP_ROLES

Table for storing one record for each Role Addition or Removal to be processed in OIM

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldaproles-22715.html#perldaproles-22715](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldaproles-22715.html#perldaproles-22715)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDAP_ROLES_PK | LDAP_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LDAP_ROLE_ID | NUMBER |  | 18 | Yes | Mandatory Primary Key. Updatable while new key generation. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LDAP_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign Key to LDAP request |  |
| REQUEST_TYPE | VARCHAR2 | 30 |  | Yes | The type of request to perform: ADD, REMOVE |  |
| REQUEST_STATUS | VARCHAR2 | 30 |  | Yes | The current status of this part of the request: REQUEST, IN PROGRESS, COMPLETE, REJECTED |  |
| ROLE_GUID | VARCHAR2 | 64 |  |  | The role Guid of the role that is to be added as a member of another role (is renamed from PARENT_ROLE_GUID). |  |
| PARENT_ROLE_GUID | VARCHAR2 | 64 |  |  | The role Guid of the role that is the parent of the role to be added. | Obsolete |
| ROLE_NAME | VARCHAR2 | 80 |  | Yes | The name of the role being added |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | The description of the role being added |  |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ROLE_COMMON_NAME | VARCHAR2 | 240 |  |  | Role common name |  |
| EXTERNAL_ID | VARCHAR2 | 64 |  |  | EXTERNAL_ID |  |
| ROLE_TYPE | VARCHAR2 | 30 |  |  | ROLE_TYPE |  |
| APPLICATION | VARCHAR2 | 255 |  |  | APPLICATION |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LDAP_ROLES_FK1 | Non Unique | FUSION_TS_TX_DATA | LDAP_REQUEST_ID |
| PER_LDAP_ROLES_U1 | Unique | FUSION_TS_TX_DATA | LDAP_ROLE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
