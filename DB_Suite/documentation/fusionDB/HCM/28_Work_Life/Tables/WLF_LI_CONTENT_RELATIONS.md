# WLF_LI_CONTENT_RELATIONS

Table to store learning item to content relationships

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** WLF_LI_CONTENT_RELATIONS

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicontentrelations-13568.html#wlflicontentrelations-13568](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicontentrelations-13568.html#wlflicontentrelations-13568)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_CONTENT_RELATIONS_PK | LI_CONTENT_RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LI_CONTENT_RELATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| OBJECT_ID | NUMBER |  | 18 | Yes | Learning Item or Content Id |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | ORA_WLF_LEARNING_ITEM or ORA_WLF_CONTENT |
| RELATED_OBJECT_ID | NUMBER |  | 18 | Yes | Related Learning Item or Content Id |
| RELATED_OBJECT_TYPE | VARCHAR2 | 30 |  |  | ORA_WLF_LEARNING_ITEM or ORA_WLF_CONTENT |
| RELATIONSHIP_TYPE | VARCHAR2 | 30 |  |  | Relationship type |
| STATUS | VARCHAR2 | 30 |  |  | Relationship Status |
| IS_PRIMARY | VARCHAR2 | 30 |  |  | is primary relation |
| POSITION | NUMBER |  | 10 |  | Position of related learning item |
| CONTENT_LOCATION | VARCHAR2 | 4000 |  |  | De-normalized content location |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_CONTENT_RELATIONS_N1 | Non Unique | WLF_LI_CONTENT_RELATIONS_N1 | OBJECT_ID, RELATED_OBJECT_ID |
| WLF_LI_CONTENT_RELATIONS_N2 | Non Unique | WLF_LI_CONTENT_RELATIONS_N2 | OBJECT_ID, IS_PRIMARY |
| WLF_LI_CONTENT_RELATIONS_U1 | Unique | Default | LI_CONTENT_RELATION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
