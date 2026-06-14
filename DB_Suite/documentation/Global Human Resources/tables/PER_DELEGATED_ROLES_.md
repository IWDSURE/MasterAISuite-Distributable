# PER_DELEGATED_ROLES_

Table for storing role delegation.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdelegatedroles-13349.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdelegatedroles-13349.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DELEGATED_ROLES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DELEGATED_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DELEGATED_ROLE_ID | NUMBER |  | 18 | Yes | Primary key |
| DELEGATION_CREATED_BY | NUMBER |  | 18 |  | The Person Id of the creator of on behalf delegation |
| START_DATE | DATE |  |  |  | Start date of delegation period |
| END_DATE | DATE |  |  |  | End date of delegation period |
| ROLE_ID | NUMBER |  | 18 |  | Role Id |
| DELEGATOR_PERSON_ID | NUMBER |  | 18 |  | The Person Id of the delegator |
| PROXY_PERSON_ID | NUMBER |  | 18 |  | The Person Id of the proxy |
| ADD_LDAP_REQUEST_ID | NUMBER |  | 18 |  | Ldap request id of role grant request |
| REMOVE_LDAP_REQUEST_ID | NUMBER |  | 18 |  | Ldap request id of role revoke request |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_DELEGATED_ROLESN1_ | Non Unique | Default | DELEGATED_ROLE_ID, LAST_UPDATE_DATE |
| PER_DELEGATED_ROLES_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DELEGATED_ROLE_ID |
| PER_DELEGATED_ROLES_U2_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, START_DATE, ROLE_ID, DELEGATOR_PERSON_ID, PROXY_PERSON_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
