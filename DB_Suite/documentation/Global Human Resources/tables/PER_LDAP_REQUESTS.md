# PER_LDAP_REQUESTS

Table for storing one record per OIM request made by the calling system.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldaprequests-14119.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldaprequests-14119.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDAP_REQUESTS_PK | LDAP_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDAP_REQUEST_ID | NUMBER |  | 18 | Yes | Mandatory Primary Key Updatable While New Key Generation |
| ACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | Flag to identify if the request is active and therefore either due to be processed or in progress within the SOA composite |
| REQUESTING_PRODUCT | VARCHAR2 | 30 |  |  | The product performing the LDAP requesting (HCM or TCA) |
| REQUESTING_REFERENCE_ID | NUMBER |  | 18 |  | The Person Id of the requesting product is HCM. The Party Id if the requesting product is TCA |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| REQUESTOR_USER_GUID | VARCHAR2 | 64 |  |  | The user Guid of the user who is making the LDAP request (if available) |
| REQUEST_STATUS | VARCHAR2 | 30 |  |  | The current status of the request: REQUEST, IN PROGRESS, COMPLETE, PART-COMPLETE |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| REQUEST_DATE | DATE |  |  |  | The date that the request should be or was processed. |
| LDAP_POLICY_FILE | VARCHAR2 | 80 |  |  | The name of the policy file that should be used to process this request |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ERROR_DESCRIPTION | VARCHAR2 | 4000 |  |  | Displayed error that comes back from OIM |
| ERROR_CODE | VARCHAR2 | 230 |  |  | Error code that corresponds to MESSAGE_NAME attribute from the FND_MESSAGES table |
| SOD_ERROR_DESCRIPTION | VARCHAR2 | 4000 |  |  | Segregation of duties error description |
| REQUESTING_SOURCE | VARCHAR2 | 30 |  |  | REQUESTING_SOURCE- INTERNAL or EXTERNAL |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LDAP_REQUESTS_N1 | Non Unique | FUSION_TS_TX_DATA | REQUESTING_REFERENCE_ID |
| PER_LDAP_REQUESTS_N2 | Non Unique | FUSION_TS_TX_DATA | REQUEST_ID |
| PER_LDAP_REQUESTS_N3 | Non Unique | FUSION_TS_TX_DATA | ACTION_OCCURRENCE_ID |
| PER_LDAP_REQUESTS_N4 | Non Unique | FUSION_TS_TX_DATA | LDAP_REQUEST_ID, REQUEST_STATUS, LDAP_POLICY_FILE |
| PER_LDAP_REQUESTS_N5 | Non Unique | FUSION_TS_TX_DATA | REQUEST_STATUS |
| PER_LDAP_REQUESTS_PK | Unique | FUSION_TS_TX_DATA | LDAP_REQUEST_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
