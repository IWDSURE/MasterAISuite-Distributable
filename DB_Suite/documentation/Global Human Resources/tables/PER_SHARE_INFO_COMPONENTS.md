# PER_SHARE_INFO_COMPONENTS

This table records the items of personal, employment etc., information that is shared for a given instance.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pershareinfocomponents-26043.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pershareinfocomponents-26043.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SHARE_INFO_COMPONENTS_PK | SHARE_INFO_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHARE_INFO_COMPONENT_ID | NUMBER |  | 18 | Yes | Primary Key column |
| SHARE_INSTANCE_ID | NUMBER |  | 18 | Yes | FK to parent record on PER_SHARE_INFORMATION. |
| SHARE_ENTITY | VARCHAR2 | 240 |  | Yes | Name of Entity to include in the particular instance of information to be shared. |
| SHARE_ENTITY_ID | NUMBER |  | 18 |  | Foreign key ID of the entity included in the particular instance of information to be shared. |
| SHARE_ENTITY_GROUP | VARCHAR2 | 256 |  |  | Name of lookup code of the entity included in the particular instance of information to be shared. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SHARE_INFO_COMPONENTS_PK | Unique | Default | SHARE_INFO_COMPONENT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
