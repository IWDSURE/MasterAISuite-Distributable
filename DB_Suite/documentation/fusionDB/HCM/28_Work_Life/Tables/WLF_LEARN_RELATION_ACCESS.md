# WLF_LEARN_RELATION_ACCESS

Table to store learn organization relation access information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelationaccess-27668.html#wlflearnrelationaccess-27668](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelationaccess-27668.html#wlflearnrelationaccess-27668)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_RELATION_ACCESS_PK | RELATION_ACCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RELATION_ACCESS_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| RELATION_ID | NUMBER |  | 18 | Yes | Learn organization relation id |
| RELATION_ROLE_TYPE | VARCHAR2 | 30 |  | Yes | Relation role type. |
| STATUS | VARCHAR2 | 64 |  | Yes | This column represents status of the learn relation access {ACTIVE,DELETED}. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Indicates the learn relation access active on date |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Indicates the learn relation removed on date |
| ACCESS_PERMISSION_ID | NUMBER |  | 18 | Yes | Learn organization level access permission id |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_RELATION_ACCESS_N1 | Non Unique | Default | ACCESS_PERMISSION_ID |
| WLF_LEARN_RELATION_ACCESS_N2 | Non Unique | Default | RELATION_ROLE_TYPE |
| WLF_LEARN_RELATION_ACCESS_U1 | Unique | Default | RELATION_ACCESS_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
