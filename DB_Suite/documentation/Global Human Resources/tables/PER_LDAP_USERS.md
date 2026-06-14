# PER_LDAP_USERS

Table for storing one record for each user to be processed in OIM when creating new users or maintaining user details (including username and preferred language)

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldapusers-23101.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldapusers-23101.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDAP_USERS_PK | LDAP_USER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDAP_USER_ID | NUMBER |  | 18 | Yes | Mandatory primary key updatable while new key generation |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LDAP_REQUEST_ID | NUMBER |  | 18 | Yes | Foreign Key to LDAP request. Mandatory. Updatable while new mandatory FK association. |
| REQUEST_TYPE | VARCHAR2 | 30 |  | Yes | The type of request to perform: CREATE, UPDATE, SUSPEND, ACTIVATE |
| REQUEST_STATUS | VARCHAR2 | 30 |  | Yes | The current status of the user portion of the request: REQUEST, IN PROGRESS, COMPLETE |
| USER_GUID | VARCHAR2 | 64 |  |  | The user Guid of the user the request is for (if available) |
| USERNAME | VARCHAR2 | 80 |  |  | The username of the user the request is for (if not auto generated) |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REQUESTOR_USER_GUID | VARCHAR2 | 64 |  |  | The user Guid of the user who is making the LDAP request (if available) |
| PREFERRED_LANGUAGE | VARCHAR2 | 30 |  |  | The preferred language of the user the request is for. Default taken if not provided. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEND_CREDENTIALS_EMAIL | VARCHAR2 | 30 |  | Yes | Indicates whether credential emails will be sent for the user |
| CREDENTIALS_EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Set this column If you want to send the credentials email to another email address |
| EXTERNAL_ID | VARCHAR2 | 64 |  |  | EXTERNAL_ID |
| ATOMPUB_ID | VARCHAR2 | 2000 |  |  | ATOMPUB_ID |
| LAST_NAME | VARCHAR2 | 150 |  |  | LAST_NAME |
| FIRST_NAME | VARCHAR2 | 150 |  |  | FIRST_NAME |
| EMAIL | VARCHAR2 | 240 |  |  | EMAIL |
| COMMONNAME | VARCHAR2 | 150 |  |  | COMMONNAME |
| USER_CATEGORY | VARCHAR2 | 240 |  |  | USER_CATEGORY |
| TWO_FACTOR_AUTH | VARCHAR2 | 30 |  |  | TWO_FACTOR_AUTH |
| MFA_PHONE | VARCHAR2 | 150 |  |  | MFA_PHONE |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LDAP_USERS_FK1 | Non Unique | FUSION_TS_TX_DATA | LDAP_REQUEST_ID |
| PER_LDAP_USERS_N1 | Non Unique | FUSION_TS_TX_DATA | REQUEST_ID |
| PER_LDAP_USERS_N2 | Non Unique | FUSION_TS_TX_DATA | USER_GUID |
| PER_LDAP_USERS_N3 | Non Unique | Default | UPPER("USERNAME") |
| PER_LDAP_USERS_N4 | Non Unique | Default | USERNAME |
| PER_LDAP_USERS_N5 | Non Unique | FUSION_TS_TX_DATA | REQUEST_STATUS, REQUEST_TYPE, LDAP_REQUEST_ID |
| PER_LDAP_USERS_U1 | Unique | FUSION_TS_TX_DATA | LDAP_USER_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
