# PER_SRM_ROLE_MEMBERSHIPS

The table stores the role membership mappings to product offerings, options and features that are processed by Generate Role Hierarchy process.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persrmrolememberships-27060.html#persrmrolememberships-27060](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persrmrolememberships-27060.html#persrmrolememberships-27060)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SRM_ROLE_MEMBERSHIPS_PK | MEMBERSHIP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MEMBERSHIP_ID | NUMBER |  | 18 | Yes | MEMBERSHIP_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 38 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ROLE_NAME | VARCHAR2 | 240 |  | Yes | ROLE_NAME |
| ROLE_DISTINGUISHED_NAME | VARCHAR2 | 4000 |  |  | ROLE_DISTINGUISHED_NAME |
| ROLE_COMMON_NAME | VARCHAR2 | 4000 |  |  | ROLE_COMMON_NAME |
| ROLE_TYPE | VARCHAR2 | 240 |  | Yes | ROLE_TYPE |
| MEMBER_ROLE | VARCHAR2 | 240 |  |  | MEMBER_ROLE |
| MEMBER_ROLE_TYPE | VARCHAR2 | 240 |  |  | MEMBER_ROLE_TYPE |
| MAPPED_TO | VARCHAR2 | 240 |  |  | MAPPED_TO |
| MAPPING_TYPE | VARCHAR2 | 240 |  |  | MAPPING_TYPE |
| APP_NAME | VARCHAR2 | 64 |  |  | APP_NAME |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SRM_ROLE_MEMBERSHIPS_PK | Unique | Default | MEMBERSHIP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
