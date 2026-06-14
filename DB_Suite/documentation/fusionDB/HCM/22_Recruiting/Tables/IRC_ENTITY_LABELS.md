# IRC_ENTITY_LABELS

Table contains relationship between entity (e.g. candidate) and the labels.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircentitylabels-26335.html#ircentitylabels-26335](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircentitylabels-26335.html#ircentitylabels-26335)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ENTITY_LABELS_PK | ENTITY_LABEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTITY_LABEL_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| ENTITY_ID | NUMBER |  | 18 | Yes | Id of the entity with which this label is being tagged. |
| LABEL_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_SEARCH_LABELS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ENTITY_LABELS_FK1 | Non Unique | Default | ENTITY_ID |
| IRC_ENTITY_LABELS_PK | Unique | DEFAULT | ENTITY_LABEL_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
