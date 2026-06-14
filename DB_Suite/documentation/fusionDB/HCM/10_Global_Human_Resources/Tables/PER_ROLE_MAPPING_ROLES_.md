# PER_ROLE_MAPPING_ROLES_

Stores the reference between Roles and Role Mappings

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolemappingroles-31573.html#perrolemappingroles-31573](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolemappingroles-31573.html#perrolemappingroles-31573)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ROLE_MAPPING_ROLES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ROLE_MAPPING_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ROLE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ROLE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ROLES_DN table. |
| ROLE_MAPPING_ID | NUMBER |  | 18 |  | Foreign Key to PER_ROLE_MAPPINGS table. |
| USE_FOR_AUTO_PROVISIONING_FLAG | VARCHAR2 | 1 |  |  | ?Flag to Indicate that the role can be used in autoprovisioning |
| SELF_REQUESTABLE_FLAG | VARCHAR2 | 1 |  |  | ? Flag to Indicate that the role can be self assigned by the logged in user |
| REQUESTABLE_FLAG | VARCHAR2 | 1 |  |  | ? Flag to Indicate that the role can be assigned to other users by the logged in user |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ROLE_MAPPING_ROLESN1_ | Non Unique | Default | ROLE_MAPPING_ROLE_ID |
| PER_ROLE_MAPPING_ROLESU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ROLE_MAPPING_ROLE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
