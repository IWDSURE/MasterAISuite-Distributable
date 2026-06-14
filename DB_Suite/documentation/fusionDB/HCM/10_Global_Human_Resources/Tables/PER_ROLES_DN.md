# PER_ROLES_DN

Stores the roles that are used in the system.  Data normally denormalized from LDAP via the Identity Governance Framework apis (IGF).

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolesdn-19780.html#perrolesdn-19780](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolesdn-19780.html#perrolesdn-19780)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ROLES_DN_PK | ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ROLE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| ROLE_GUID | VARCHAR2 | 64 |  | Yes | ?Globally Unique Identifier for the Role | Active |
| ABSTRACT_ROLE | VARCHAR2 | 30 |  |  | ?Flag to Indicate it is an Abstract Role | Active |
| JOB_ROLE | VARCHAR2 | 30 |  |  | ?Flag to Indicate it is an Job Role | Active |
| DATA_ROLE | VARCHAR2 | 30 |  |  | ?Flag to Indicate it is an Data Role | Active |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | ?Flag to Indicate it is an Active Role | Active |
| ROLE_COMMON_NAME | VARCHAR2 | 4000 |  |  | The Common Name (CN) defined within LDAP. |  |
| MULTITENANCY_COMMON_NAME | VARCHAR2 | 4000 |  |  | The Multitenancy Common Name Defined in LDAP |  |
| ROLE_DISTINGUISHED_NAME | VARCHAR2 | 4000 |  |  | The Distinguished Name (DN) defined within LDAP - Contains group information etc. to provide a unique name. |  |
| BUSINESS_GROUP_ID | NUMBER |  |  | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| DELEGATION_ALLOWED | VARCHAR2 | 30 |  |  | ?Flag to Indicate it is the Role can be delegated |  |
| EXTERNAL_ID | VARCHAR2 | 64 |  |  | EXTERNAL_ID |  |
| EXTERNAL_ROLE | VARCHAR2 | 30 |  |  | ?Flag to Indicate it is an External Role |  |
| DUTY_ROLE | VARCHAR2 | 30 |  |  | DUTY_ROLE |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ROLES_DN_N1 | Non Unique | FUSION_TS_SEED | ROLE_COMMON_NAME |
| PER_ROLES_DN_N2 | Non Unique | FUSION_TS_SEED | EXTERNAL_ID |
| PER_ROLES_DN_N3 | Non Unique | FUSION_TS_SEED | UPPER("ROLE_COMMON_NAME") |
| PER_ROLES_DN_PK | Unique | FUSION_TS_SEED | ROLE_ID |
| PER_ROLES_DN_U1 | Unique | FUSION_TS_SEED | BUSINESS_GROUP_ID, ROLE_GUID |
| PER_ROLES_DN_U2 | Unique | FUSION_TS_SEED | ROLE_GUID |
| PER_ROLES_DN_U3 | Unique | FUSION_TS_SEED | UPPER("ROLE_GUID") |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
