# WLF_LI_HIERARCHIES_F

Table to store learning item hierarchies.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflihierarchiesf-29870.html#wlflihierarchiesf-29870](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflihierarchiesf-29870.html#wlflihierarchiesf-29870)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_HIERARCHIES_F_PK | HIERARCHY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HIERARCHY_ID | VARCHAR2 | 20 |  | Yes | System generated unique identifier. |
| HIERARCHY_NUMBER | VARCHAR2 | 30 |  |  | HIERARCHY_NUMBER |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| FEATURED_FLAG | VARCHAR2 | 30 |  |  | Featured learning items recommended by Admin |
| FEATURED_DATE | DATE |  |  |  | FEATURED_DATE |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| CHILD_LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Reference to child content entity. |
| POSITION | NUMBER |  | 38 |  | Position of the item in collection identified by PARENT_CONENT_ID. |
| MANDATORY_FLAG | VARCHAR2 | 1 |  |  | Mandatory Flag |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CHILD_LEARNING_ITEM_TYPE | VARCHAR2 | 32 |  |  | This column represents learning item type of child learning itemid  like ORA_COURSE,ORA_VIDEO and ORA_TUTORIAL etc |
| CHILD_LI_RELATED_OBJECT_TYPE | VARCHAR2 | 30 |  |  | Represents the related object type of the child learning item , will contain course for specialization section activities. |
| CHILD_LI_RELATED_OBJECT_ID | NUMBER |  | 18 |  | Represents the related object id of the child learning item , will contain course learning item id for specialization section activities. |
| HIERARCHY_TYPE | VARCHAR2 | 64 |  |  | Represents the learning item type and child learning item type of the hierarchy row |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_HIERARCHIES_F_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_HIERARCHIES_F_N2 | Non Unique | Default | CHILD_LEARNING_ITEM_ID |
| WLF_LI_HIERARCHIES_F_N3 | Non Unique | Default | HIERARCHY_NUMBER |
| WLF_LI_HIERARCHIES_F_U1 | Unique | Default | HIERARCHY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
