# PER_DELEGATED_ROLES

Table for storing role delegation.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdelegatedroles-26261.html#perdelegatedroles-26261](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdelegatedroles-26261.html#perdelegatedroles-26261)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DELEGATED_ROLES_PK | DELEGATED_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DELEGATED_ROLE_ID | NUMBER |  | 18 | Yes | Primary key |
| DELEGATION_CREATED_BY | NUMBER |  | 18 |  | The Person Id of the creator of on behalf delegation |
| START_DATE | DATE |  |  | Yes | Start date of delegation period |
| END_DATE | DATE |  |  |  | End date of delegation period |
| ROLE_ID | NUMBER |  | 18 | Yes | Role Id |
| DELEGATOR_PERSON_ID | NUMBER |  | 18 | Yes | The Person Id of the delegator |
| PROXY_PERSON_ID | NUMBER |  | 18 | Yes | The Person Id of the proxy |
| ADD_LDAP_REQUEST_ID | NUMBER |  | 18 | Yes | Ldap request id of role grant request |
| REMOVE_LDAP_REQUEST_ID | NUMBER |  | 18 |  | Ldap request id of role revoke request |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_DELEGATED_ROLES_N1 | Non Unique | Default | DELEGATOR_PERSON_ID |
| PER_DELEGATED_ROLES_N2 | Non Unique | Default | PROXY_PERSON_ID |
| PER_DELEGATED_ROLES_N3 | Non Unique | Default | ADD_LDAP_REQUEST_ID |
| PER_DELEGATED_ROLES_N4 | Non Unique | Default | REMOVE_LDAP_REQUEST_ID |
| PER_DELEGATED_ROLES_U1 | Unique | Default | DELEGATED_ROLE_ID |
| PER_DELEGATED_ROLES_U2 | Unique | Default | START_DATE, ROLE_ID, DELEGATOR_PERSON_ID, PROXY_PERSON_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
