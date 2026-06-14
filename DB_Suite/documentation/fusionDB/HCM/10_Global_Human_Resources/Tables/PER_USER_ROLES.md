# PER_USER_ROLES

Table for storing one record for each Role Membership that the user has been provisioned in LDAP.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peruserroles-22200.html#peruserroles-22200](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peruserroles-22200.html#peruserroles-22200)

## Primary Key

| Name | Columns |
|------|----------|
| PER_USER_ROLES_PK | USER_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_ROLE_ID | NUMBER |  | 18 | Yes | Identifies the role for the user. |
| USER_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_USERS table. |
| ROLE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ROLES_DN table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ROLE_GUID | VARCHAR2 | 64 |  | Yes | Denormalized Role Guid |
| METHOD_CODE | VARCHAR2 | 30 |  | Yes | Automatic, Manually or Externally provisioned |
| ACTIVE_FLAG | VARCHAR2 | 30 |  | Yes | Flag to mark when a user role is active. |
| TERMINATED_FLAG | VARCHAR2 | 30 |  | Yes | Flag to identify that this role belongs to a user that has had their employment terminated (used if reverse termination process is initiated to re-provision roles) |
| START_DATE | DATE |  |  | Yes | the date that the user role is active from |
| END_DATE | DATE |  |  |  | The date that the user role will cease to be active from |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_USER_ROLES_FK2 | Non Unique | FUSION_TS_TX_DATA | ROLE_ID |
| PER_USER_ROLES_U1 | Unique | FUSION_TS_TX_DATA | USER_ROLE_ID |
| PER_USER_ROLES_U2 | Unique | Default | USER_ID, ROLE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
