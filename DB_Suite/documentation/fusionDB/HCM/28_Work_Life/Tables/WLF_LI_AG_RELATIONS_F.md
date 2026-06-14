# WLF_LI_AG_RELATIONS_F

Table to store Access Group Relations.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliagrelationsf-17784.html#wlfliagrelationsf-17784](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliagrelationsf-17784.html#wlfliagrelationsf-17784)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_AG_RELATIONS_F_PK | LI_AG_RELATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LI_AG_RELATION_ID | NUMBER |  | 18 | Yes | Surrogate Key identifying the row |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CATALOG_LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Foreign Key to WLF_LEARNING_ITEM_F table. This is the Learning Item Id for Course, Offering, Specialization that are going to be associated with the access group |
| ACCESS_LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Foreign Key to WLF_LEARNING_ITEM_F table. This is the learning Item id of the access group. This can be accessed via WLF_EVENT_ASSIGNMENTS and WLF_EVENTS. This is denormalized on to this table for fast access. |
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Foreign Key to WLF_EVENT_ASSIGNMENTS_F , Access Profile |
| PRIORITY | NUMBER |  | 18 |  | Priority of the access group with in the list of access groups for a given catalog learning item |
| PRICING_RULE_ID | NUMBER |  | 18 |  | Pricing rule for the combination of Catalog Learning Item and Access Group Learning Item |
| ACCESS_PERMISSION_ID | NUMBER |  | 18 | Yes | Foreign Key to WLF_ACCESS_PERMISSIONS_F for storing permissions |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the relation |
| FOLLOW_LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | This column will be populated only on adhoc access groups with one of the destinations as a learning_item_id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| FOLLOW_AG_RELATION_ID | NUMBER |  | 18 |  | FOLLOW_AG_RELATION_ID |
| PAYMENT_RULE_ID | NUMBER |  | 18 |  | Identifier of pricing rule payment type. Foreign key to  WLF_PAYMENT_RULES_F. |
| LI_AG_RELATION_NUMBER | VARCHAR2 | 30 |  |  | UserKey to uniquely identify Access Group Relation. |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Indicates if access group is processed to security index or not |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_AG_RELATIONS_F_N1 | Non Unique | Default | CATALOG_LEARNING_ITEM_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| WLF_LI_AG_RELATIONS_F_N2 | Non Unique | Default | ACCESS_LEARNING_ITEM_ID |
| WLF_LI_AG_RELATIONS_F_N3 | Non Unique | Default | EVENT_ASSIGNMENT_ID |
| WLF_LI_AG_RELATIONS_F_N4 | Non Unique | Default | EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, CATALOG_LEARNING_ITEM_ID, PRIORITY |
| WLF_LI_AG_RELATIONS_F_N5 | Non Unique | Default | IN_ELASTIC |
| WLF_LI_AG_RELATIONS_F_U1 | Unique | Default | LI_AG_RELATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
