# WLF_LEARN_RELATIONS

Table to store relation information of learning item to learning organization.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelations-25487.html#wlflearnrelations-25487](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelations-25487.html#wlflearnrelations-25487)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_RELATIONS_PK | LEARN_RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARN_RELATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARN_RELATION_NUMBER | VARCHAR2 | 30 |  | Yes | Learn Relation Number |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Reference to source object id |
| SOURCE_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Source object type. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Learning organization reconcile job processing date |
| RELATED_OBJECT_ID | NUMBER |  | 18 | Yes | Reference to related object id |
| RELATED_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Related object type. |
| RELATION_TYPE | VARCHAR2 | 30 |  | Yes | Relation Type |
| STATUS | VARCHAR2 | 64 |  | Yes | This column represents status of the relation object {ACTIVE, DELETED}. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Indicates the relation object active date |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Indicates the relation object removed date |
| POSITION | NUMBER |  | 18 | Yes | Position sequence |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Indentifier to indicate the row needs processing for elastic index |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_RELATIONS_N1 | Non Unique | Default | SOURCE_OBJECT_ID, SOURCE_OBJECT_TYPE |
| WLF_LEARN_RELATIONS_N2 | Non Unique | Default | RELATED_OBJECT_ID, RELATED_OBJECT_TYPE |
| WLF_LEARN_RELATIONS_N3 | Non Unique | Default | RELATION_TYPE |
| WLF_LEARN_RELATIONS_U1 | Unique | Default | LEARN_RELATION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
