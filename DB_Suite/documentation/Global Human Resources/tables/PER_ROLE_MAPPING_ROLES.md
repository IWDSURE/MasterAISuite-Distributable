# PER_ROLE_MAPPING_ROLES

Stores the reference between Roles and Role Mappings

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolemappingroles-29510.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolemappingroles-29510.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ROLE_MAPPING_ROLES_PK | ROLE_MAPPING_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ROLE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ROLE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ROLES_DN table. |
| ROLE_MAPPING_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ROLE_MAPPINGS table. |
| USE_FOR_AUTO_PROVISIONING_FLAG | VARCHAR2 | 1 |  | Yes | ?Flag to Indicate that the role can be used in autoprovisioning |
| SELF_REQUESTABLE_FLAG | VARCHAR2 | 1 |  | Yes | ? Flag to Indicate that the role can be self assigned by the logged in user |
| REQUESTABLE_FLAG | VARCHAR2 | 1 |  | Yes | ? Flag to Indicate that the role can be assigned to other users by the logged in user |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ROLE_MAPPING_ROLES_FK1 | Non Unique | FUSION_TS_TX_DATA | ROLE_MAPPING_ID |
| PER_ROLE_MAPPING_ROLES_U1 | Unique | FUSION_TS_TX_DATA | ROLE_MAPPING_ROLE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
